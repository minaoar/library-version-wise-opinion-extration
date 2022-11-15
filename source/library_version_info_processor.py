import pandas as pd


data_dir = '../data/'

def fancy_print(string):
    print("")
    print(string)
    print("===============================================")

    
def process_version_info(library_name):
    fancy_print(library_name)
    # load version info csv files
    version_info = pd.read_csv(data_dir+library_name+"_version_info.csv")
    #print(version_info)

    # remove the rows with empty values in usage column
    version_info = version_info[version_info['usage'].notna()]

    # format usage column to int by removing commas
    version_info['usage'] = version_info['usage'].astype(str).str.replace(',', '').astype(int)

    # convert the date column to datetime
    version_info['date'] = pd.to_datetime(version_info['date'])

    # sample version text 3.3.1.GA. We shall have to extract the major version number x.xx
    version_info['version'] = version_info['version'].str.split('.').str[0:2].str.join('.')
    #print(version_info)

    # group by version and sum the usage.  
    # Add a new column with oldest and latest date.
    # sort by min date  
    version_info = version_info.groupby(['version']).agg({'usage':'sum', 'date':['min', 'max']}).reset_index()
    version_info.columns = ['version', 'usage', 'date_min', 'date_max']

    # sort by date_min
    version_info = version_info.sort_values(by=['date_min'], ascending=True)
    
    # find the difference in days between the oldest and latest date and add as a new column 'days'
    version_info['days'] = (version_info['date_max'] - version_info['date_min']).dt.days

    # move the days column immediately after the usage column
    version_info = version_info[['version', 'usage', 'days', 'date_min', 'date_max']]

    print(version_info)



if __name__ == "__main__":
    process_version_info("gson")
    process_version_info("jackson")
    process_version_info("spring-orm")
    process_version_info("hibernate")