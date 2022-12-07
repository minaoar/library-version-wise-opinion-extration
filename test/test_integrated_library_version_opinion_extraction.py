#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import unittest

import sys
import os

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# current test file is in ./test folder. But the library_version_opinion_extraction.py is in ../source folder
sys.path.append(os.path.join(file_dir, '../source'))

from library_version_opinion_extraction import *

class TestLibraryVersionOpinionExtraction(unittest.TestCase):
    # test extract_opinions_with_library_version method
    def test_extract_opinions_with_library_version(self):
        opinion_list_pd = extract_opinions_with_library_version()
        self.assertEqual(len(opinion_list_pd), 9)

        target_sentence = '<supports> Google Gson supports generics and nested beans.'

        # asssert that the target sentence is in the dataframe
        self.assertTrue(target_sentence in opinion_list_pd['sentence'].values)

        # get the index of the target sentence
        index = opinion_list_pd[opinion_list_pd['sentence'] == target_sentence].index[0]

        # check the version of the target sentence
        self.assertEqual(opinion_list_pd.iloc[index]['gson_version'], ['2.8', '2.6', '2.7'])

        
if __name__ == '__main__':
    unittest.main()