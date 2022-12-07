#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

from bs4 import BeautifulSoup
import cloudscraper
import pandas as pd
from tabulate import tabulate


import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from config import *

def get_site_content(site_url):

    scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
    response = scraper.get(site_url)
    return response

def get_artifact_page(response, library_name):
    #print(response.text)
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Getting artifact page for library: "+library_name)

    soup = BeautifulSoup(response.text, "html.parser")

    # parse all href links and texts from the lists
    for link in soup.find_all('a'):
        href = link['href']
        if '/artifact/' in href:
            # split the href by / and get the last item
            artifact_name = href.split('/')[-1]
            if library_name in artifact_name:
                #print(href)
                logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Artifact page found: "+href)
                return href


def get_version_rows(tables_all):
    version_rows = []
    # check all tables. The version table is the after the first table with more than 5 rows
    for table in tables_all[1:]:
        version_rows = table.find_all('tr')
        if len(version_rows) > 5:
            return version_rows
            
    return version_rows

def parse_library_version_rows(version_rows):
    version_list = []

    version_list = []

    for row in version_rows:
        version_info = {}

        # get the date of the version
        date_info = row.find_all('span', attrs={'class':'date'})
            
        if len(date_info) > 0:
            date_value = date_info[0].text
            version_info['date'] = str(date_value)

        usage_info = row.find_all('a')
        for item in usage_info:
            # Get href link
            href = item.get('href')
            # see if href contains usage
            if "usage" in href :
                # split the usage text by / and get the second item
                version = href.split('/')[1]
                #print(version, "->", item.text)

                version_info['version'] = str(version)
                version_info['usage'] = str(item.text)
                
        version_list.append(version_info.copy())

    return version_list

def parse_library_details_page(response):
    soup = BeautifulSoup(response.text, "html.parser")
    tables_all = soup.findAll('table')#, attrs={'id':'grid versions'})

    #load pandas dataframe from the introductory table
    artifact_info_table = pd.read_html(str(tables_all[0]))[0]
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Artifact Info:\n" + artifact_info_table.to_markdown(index=False))
    
    # Since the version details table contains merged cells, we need to parse the table manually
    # version_info_table = pd.read_html(str(table[1]))[0]
    # print("\n\nVersion Info:\n", version_info_table)

    version_rows = get_version_rows(tables_all)
    version_list = parse_library_version_rows(version_rows)

    # print("Version List:\n", version_list)

    # load dataframe from the string values of version list
    version_info_table = pd.DataFrame.from_dict(version_list)

    # remove empty rows
    version_info_table = version_info_table.dropna()
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Version Info [" + str(len(version_list))+"]:\n"+ version_info_table.to_markdown(index=False))

    return artifact_info_table, version_info_table



def get_library_results(library_name):
    site_url = "https://mvnrepository.com/search?q="+library_name
    response = get_site_content(site_url)
    artifact_page = get_artifact_page(response, library_name)
    # get the library details page
    library_details_page = "https://mvnrepository.com"+artifact_page
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Library Details Page: "+ library_details_page)
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "*"*100)

    # get the library details page content
    response = get_site_content(library_details_page)
    # parse the library details page
    artifact_info_table, version_info_table = parse_library_details_page(response)

    # save the tables to csv files
    artifact_info_table.to_csv(data_dir+library_name+"_artifact_info.csv", index=False)
    version_info_table.to_csv(data_dir+library_name+"_version_info.csv", index=False)
    
    
if __name__ == "__main__":
    get_library_results("gson")
    # get_library_results("jackson")
    # get_library_results("spring-orm")
    # get_library_results("hibernate")






