import unittest

import sys
import os



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# current test file is in ./test folder. But the stackoverflow_data_collection.py is in ../source folder
sys.path.append(os.path.join(file_dir, '../source'))

from stackoverflow_data_collection import *

class TestStackoverflowDataCollection(unittest.TestCase):
    # test get_file_name method
    def test_get_file_name(self):
        self.assertEqual(get_file_name(), "stackoverflow_gson.csv")

    # test collect_data method
    def test_collect_data(self):
        myresult = collect_data()
        self.assertEqual(len(myresult), 50)

if __name__ == '__main__':
    unittest.main()