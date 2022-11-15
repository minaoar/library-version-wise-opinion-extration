#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import pandas as pd

import sys

import os
import logging

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from process_post_text import *
from library_version_info_processor import *


data_dir = "../data/"

# keywords =  ["slf4j", "log4j"]
# keywords =  ["memcpy", "memmove"]
# keywords = ['pandas', 'numpy']
#keywords = ['lxml', 'beautifulsoup']
keywords = ['gson', 'jackson']
#keywords = ['gson', '2.8']

# query = ("SELECT id, body FROM Posts where body like '%mysql%connector%' LIMIT 2")
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%') order by ViewCount Desc LIMIT 0, 5;"
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%')  LIMIT 0, 50;"
# query = "SELECT id, body FROM stackoverflow.Posts where (body like '%memcpy%' and body like '%memmove%')  LIMIT 0, 50;"
# query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%memcpy%' OR text like '%memmove%')  LIMIT 0, 50;"
# query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%pandas%' and text like '%numpy%')  LIMIT 0, 50;"
#query = "SELECT id, body, creationdate FROM stackoverflow.Posts where (body like '%lxml%' and body like '%beautifulsoup%')  LIMIT 0, 50;"

query = "SELECT id, body, creationdate, lasteditdate FROM stackoverflow.Posts where (body like '%" +keywords[0]+ "%' and body like '%" +keywords[1]+ "%')  LIMIT 0, 50;"
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Started program: '+os.path.basename(__file__))

def get_file_name():
    file_name = "stackoverflow_"
    for keyword in keywords:
        file_name += keyword + "_"
    file_name = file_name[:-1] + ".csv"
    return file_name

def store_data(myresult, column_names):
    # create a dataframe from the result set after processing body with process_raw_text method and merge the returned sentences array from process_raw_text
    df = pd.DataFrame(myresult, columns=column_names)
    df['body'] = df['body'].apply(process_raw_text_body)

    # add a new date column to the dataframe which will store latest date of creation and last edit
    df['date'] = df[['creationdate', 'lasteditdate']].max(axis=1)


    # write the dataframe to a csv file with name of the keywords
    df.to_csv(data_dir+get_file_name(), index=False)
    #print(df.head())
    logging.info('Data stored in file: '+get_file_name())
    return df

CACHED_DATA = True

if CACHED_DATA == False:
    # Connect to mysql database and select all rows from table
    import pwd
    import mysql.connector
    from mysql.connector import errorcode
    DB_NAME = 'stackoverflow'

    userid = 'root'
    pwd = '11111111'

    print("Connecting to database...")
    cnx = mysql.connector.connect(user=userid, password=pwd, database=DB_NAME)
    print("Connected to database")


    cursor = cnx.cursor()

    cursor.execute(query)

    # print the result
    myresult = cursor.fetchall()

    #print column names
    print(cursor.column_names)

    myresult = store_data(myresult, cursor.column_names)
else:
    # load myresult dataframe from stored data file. 
    # This is to avoid connecting to mysql database everytime
    myresult = pd.read_csv(data_dir+get_file_name())
    #print(myresult.head)

# convert myresult to list of tuples
myresult = [tuple(x) for x in myresult.values]

opinion_list = []

s = 1
for (id, body, creationdate, lasteditdate, date) in myresult:
    #print(id, creationdate)
    #print(body)
    #print('---------------------')
    # parse stackoverflow post body by removing xml tags
    
    sentences = process_raw_text(body)
    sentences_with_keywords = extract_sentence_with_keywords(sentences, keywords)
    sentences_with_adjectives = extract_sentence_with_adjectives(sentences_with_keywords)

    # print each sentence in one line with sentence counter
    for i, sentence in enumerate(sentences_with_adjectives):
        print(i+s, sentence)
        opinion_list.append((id, sentence, date, get_tentative_versions(keywords[0], date), get_tentative_versions(keywords[1], date)))

    s = s + len(sentences_with_adjectives)

    #print('#####################')

    
opinion_list_pd = pd.DataFrame(opinion_list, columns=['id', 'sentence', 'date', keywords[0]+'_version', keywords[1]+'_version'])
opinion_list_pd.to_csv(data_dir+get_file_name()[:-4]+"_opinion.csv", index=False)

if CACHED_DATA == False:
    cursor.close()
    cnx.close()

logging.info('Finished program: '+os.path.basename(__file__))
