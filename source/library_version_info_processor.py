#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import pandas as pd


data_dir = '../data/'

def fancy_print(string):
    print("")
    print(string)
    print("===============================================")

    
def process_version_info(library_name):
    # fancy_print(library_name)
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

    # print(version_info)
    return version_info

def adjust_cool_down_period(date):
    date = pd.to_datetime(date)

    # add cool down period to the date
    # currently this is set to 0. We can change this to 30 days or 60 days if we think that 
    # a post in StackOverflow should only come after a release passes this designated cool down period.
    cool_down_period = 30 
    date = date - pd.Timedelta(days=cool_down_period)
    # print("Date after cool down period: " + str(date))

    return date

def get_tentative_versions(library, date):
    # adjust cool down period
    # date = adjust_cool_down_period(date)

    # convert the date to datetime
    date = pd.to_datetime(date)
    version_info = process_version_info(library)

    # get the latest three versions that were released before the date
    tentative_versions = version_info[version_info['date_min'] < date].tail(3)

    # sort the versions by usage
    tentative_versions = tentative_versions.sort_values(by=['usage'], ascending=False)

    # keep only the version text and convert the series to list
    tentative_versions = tentative_versions['version'].tolist()
    # fancy_print(tentative_versions)
    return tentative_versions


if __name__ == "__main__":
    #process_version_info("gson")
    # process_version_info("jackson")
    # process_version_info("spring-orm")
    # process_version_info("hibernate")

    get_tentative_versions("jackson", '2022-01-01')