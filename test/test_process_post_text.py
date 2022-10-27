from bs4 import BeautifulSoup
import spacy

from process_post_text import breakdown_sentences, extract_sentence_with_adjectives, extract_sentence_with_keywords, process_raw_text, read_word_list, remove_code_snippet

def test_read_word_list():
    
    #Arrange
    POSITIVE_WORD_FILE = "../data/positive-words.txt"
    NEGATIVE_WORD_FILE = "../data/negative-words.txt"

    #Act and Asert
    assert read_word_list(POSITIVE_WORD_FILE) == 1
    assert read_word_list(NEGATIVE_WORD_FILE) == 1

# POSITIVE_WORD_FILE = "../data/positive-words.txt"
# NEGATIVE_WORD_FILE = "../data/negative-words.txt"
# nlp = spacy.load("en_core_web_lg")

def test_remove_code_snippet():
    pass
    # soup = BeautifulSoup(body, 'html.parser')
    # remove_code_snippet(soup)
    # body = soup.get_text()

def test_process_raw_text():
    pass
    #process_raw_text(body)

def test_breakdown_sentences():
    pass
    #breakdown_sentences(body)

def test_extract_sentence_with_keywords():
    pass
    #extract_sentence_with_keywords(sentence_list, keywords, minimum_presence=1, add_keyword = False)

def test_extract_sentence_with_adjectives():
    pass
    #extract_sentence_with_adjectives(sentence_list)

def test_passed():
    pass