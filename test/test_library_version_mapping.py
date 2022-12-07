#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import unittest

import sys
import os



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# current test file is in ./test folder. But the library_version_mapping.py is in ../source folder
sys.path.append(os.path.join(file_dir, '../source'))

from library_version_mapping import *


class TestLibraryVersionMapping(unittest.TestCase):
    
    # write unit tests for get_tentative_versions in library_version_mapping.py
    def test_get_tentative_versions(self):
        # test for jackson
        # get the latest three versions that were released before the date
        tentative_versions = get_tentative_versions("jackson", '2022-01-01')
        
        self.assertEqual(tentative_versions, ['2.13', '2.12', '2.11'])

        # test for gson
        tentative_versions = get_tentative_versions("gson", '2022-01-01')
        self.assertEqual(tentative_versions, ['2.8', '2.6', '2.7'])

        # test for spring-orm
        tentative_versions = get_tentative_versions("spring-orm", '2022-01-01')
        self.assertEqual(tentative_versions, ['5.3', '5.2', '5.1'])

        # test for hibernate
        tentative_versions = get_tentative_versions("hibernate", '2022-01-01')
        self.assertEqual(tentative_versions, ['5.6', '5.5', '6.0'])

    # write unit tests for process_version_info in library_version_mapping.py
    def test_process_version_info(self):
        # test for jackson
        version_info = process_version_info("jackson")
        self.assertEqual(version_info.shape, (15, 5))

        # test for gson
        version_info = process_version_info("gson")
        self.assertEqual(version_info.shape, (15, 5))

        # test for spring-orm
        version_info = process_version_info("spring-orm")
        self.assertEqual(version_info.shape, (13, 5))

        # test for hibernate
        version_info = process_version_info("hibernate")
        self.assertEqual(version_info.shape, (16, 5))
    

if __name__ == '__main__':
    unittest.main()
#unittest.main()
