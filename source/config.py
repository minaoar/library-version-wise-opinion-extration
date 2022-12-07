#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import warnings
warnings.filterwarnings("ignore")

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


data_dir = "../data/"
POSITIVE_WORD_FILE = "../data/positive-words.txt"
NEGATIVE_WORD_FILE = "../data/negative-words.txt"

CACHED_DATA = True

DB_NAME = 'stackoverflow'
DB_USERID = 'root'
DB_PWD = '11111111'