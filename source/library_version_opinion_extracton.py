#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import pandas as pd

import sys

import os
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Started program: '+os.path.basename(__file__))

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from process_post_text import *
from library_version_info_processor import *
from stackoverflow_data_collection import *


data_dir = "../data/"


stackoverflow_data = collect_data()

# convert myresult to list of tuples
stackoverflow_data = [tuple(x) for x in stackoverflow_data.values]

opinion_list = []

s = 1
for (id, body, creationdate, lasteditdate, date) in stackoverflow_data:
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

        # version of librar#1:
        version_librarary1 = get_tentative_versions(keywords[0], date)
        version_librarary2 = ''
        if dual_library_comparison == True:
            version_librarary2 = get_tentative_versions(keywords[1], date)
            opinion_list.append((id, sentence, date, version_librarary1, version_librarary2))
        else:
            opinion_list.append((id, sentence, date, version_librarary1))


    s = s + len(sentences_with_adjectives)

    #print('#####################')

if dual_library_comparison == True:
    opinion_list_pd = pd.DataFrame(opinion_list, columns=['id', 'sentence', 'date', keywords[0]+'_version', keywords[1]+'_version'])
else:
    opinion_list_pd = pd.DataFrame(opinion_list, columns=['id', 'sentence', 'date', keywords[0]+'_version'])
    
opinion_list_pd.to_csv(data_dir+get_file_name()[:-4]+"_opinion.csv", index=False)


logging.info('Finished program: '+os.path.basename(__file__))
