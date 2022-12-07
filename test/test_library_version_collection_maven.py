import unittest

import sys
import os



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# current test file is in ./test folder. But the library_version_collection_maven.py is in ../source folder
sys.path.append(os.path.join(file_dir, '../source'))

from library_version_collection_maven import *

class TestLibraryVersionCollectionMaven(unittest.TestCase):
        
        # write unit tests for get_artifact_page in library_version_collection_maven.py
        def test_get_artifact_page(self):
            # test for jackson
            library_name = "jackson"
            site_url = "https://mvnrepository.com/search?q="+library_name
            response = get_site_content(site_url)
            artifact_page = get_artifact_page(response, "jackson")
            self.assertEqual(artifact_page, "/artifact/com.fasterxml.jackson.core/jackson-databind", 'mvnrepository.com cannot be scraped')
    
            # test for gson
            library_name = "gson"
            site_url = "https://mvnrepository.com/search?q="+library_name
            response = get_site_content(site_url)
            artifact_page = get_artifact_page(response, "gson")
            self.assertEqual(artifact_page, "/artifact/com.google.code.gson/gson", 'mvnrepository.com cannot be scraped')
    
            # test for spring-orm
            library_name = "spring-orm"
            site_url = "https://mvnrepository.com/search?q="+library_name
            response = get_site_content(site_url)
            artifact_page = get_artifact_page(response, "spring-orm")
            self.assertEqual(artifact_page, "/artifact/org.springframework/spring-orm", 'mvnrepository.com cannot be scraped')
    
            # test for hibernate
            library_name = "hibernate"
            site_url = "https://mvnrepository.com/search?q="+library_name
            response = get_site_content(site_url)
            artifact_page = get_artifact_page(response, "hibernate")
            self.assertEqual(artifact_page, "/artifact/org.hibernate/hibernate-core", 'mvnrepository.com cannot be scraped')
    
        # write unit tests for get_version_rows in library_version_collection_maven.py
        def test_get_version_rows(self):
            # test for jackson
            library_name = "jackson"
            site_url = "https://mvnrepository.com/search?q="+library_name
            response = get_site_content(site_url)
            artifact_page = get_artifact_page(response, "jackson")
            artifact_page_url = "https://mvnrepository.com" + artifact_page
            response = get_site_content(artifact_page_url)
            artifact_info_table, version_info_table = parse_library_details_page(response)
            self.assertEqual(len(artifact_info_table), 5, 'mvnrepository.com cannot be scraped')
            self.assertEqual(len(version_info_table), 178, 'mvnrepository.com cannot be scraped')

            

if __name__ == '__main__':
    unittest.main()