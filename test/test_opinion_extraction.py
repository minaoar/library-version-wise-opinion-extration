import unittest

import sys
import os



file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

# current test file is in ./test folder. But the opinion_extraction.py is in ../source folder
sys.path.append(os.path.join(file_dir, '../source'))

from opinion_extraction import *

class TestOpinionExtraction(unittest.TestCase):
        
        # write unit tests for breakdown_sentences in opinion_extraction.py
        def test_breakdown_sentences(self):
            # test for jackson
            # get the latest three versions that were released before the date
            sentences = breakdown_sentences("I like this product. It is very good. I hate this product. It is very bad.")
            self.assertEqual(sentences, ['I like this product.', 'It is very good.', 'I hate this product.', 'It is very bad.'])
        
        # write unit tests for extract_sentence_with_keywords in opinion_extraction.py
        def test_extract_sentence_with_keywords(self):
            # test for jackson and gson.
            sentences = breakdown_sentences("I prefer jackson. It is faster than gson. I hate this product. It is very bad.")
            sentences = extract_sentence_with_keywords(sentences, ["jackson", "gson"])
            self.assertEqual(sentences, ['I prefer jackson.', 'It is faster than gson.'])

        # write unit tests for extract_sentence_with_adjectives in opinion_extraction.py
        def test_extract_sentence_with_adjectives(self):
            # test for jackson and gson.
            sentences = breakdown_sentences("I prefer jackson. It is faster than gson.")
            sentences = extract_sentence_with_adjectives(sentences)
            self.assertEqual(sentences,  ['<faster> It is faster than gson.'])

if __name__ == '__main__':
    unittest.main()