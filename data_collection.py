#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

# Connect to mysql database and select all rows from table
import pwd
import mysql.connector
from mysql.connector import errorcode

import sys

import os
import logging

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from process_post_text import *

keywords =  ["slf4j", "log4j"]
keywords =  ["memcpy", "memmove"]
keywords = ['pandas', 'numpy']

# query = ("SELECT id, body FROM Posts where body like '%mysql%connector%' LIMIT 2")
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%') order by ViewCount Desc LIMIT 0, 5;"
# query = "SELECT id, body FROM stackoverflow.Posts where (Tags like '%<slf4j>%' and Tags like '%<log4j2>%')  LIMIT 0, 50;"
query = "SELECT id, body FROM stackoverflow.Posts where (body like '%memcpy%' and body like '%memmove%')  LIMIT 0, 50;"
query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%memcpy%' OR text like '%memmove%')  LIMIT 0, 50;"
query = "SELECT id, text as body FROM stackoverflow.Comments where (text like '%pandas%' and text like '%numpy%')  LIMIT 0, 50;"

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Started program: '+os.path.basename(__file__))


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
   
#print value of body column

s = 1
for (id, body) in myresult:
    #print(id)
    #print(body)
    #print('---------------------')
    # parse stackoverflow post body by removing xml tags
    
    sentences = process_raw_text(body)
    sentences_with_keywords = extract_sentence_with_keywords(sentences, keywords)
    sentences_with_adjectives = extract_sentence_with_adjectives(sentences_with_keywords)

    # print each sentence in one line with sentence counter
    for i, sentence in enumerate(sentences_with_adjectives):
        print(i+s, sentence)

    s = s + len(sentences_with_adjectives)
    #print('#####################')

    

cursor.close()
cnx.close()

logging.info('Finished program: '+os.path.basename(__file__))
