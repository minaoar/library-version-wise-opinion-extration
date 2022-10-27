from process_post_text import read_word_list

def test_read_word_list():
    POSITIVE_WORD_FILE = "../data/positive-words.txt"
    NEGATIVE_WORD_FILE = "../data/negative-words.txt"

    assert read_word_list(POSITIVE_WORD_FILE) == 1
    assert read_word_list(NEGATIVE_WORD_FILE) == 1

    #pass

def test_remove_code_snippet():
    remove_code_snippet(body_soup)

def test_process_raw_text():
    process_raw_text(body)

def test_breakdown_sentences():
    breakdown_sentences(body)

def test_extract_sentence_with_keywords():
    extract_sentence_with_keywords(sentence_list, keywords, minimum_presence=1, add_keyword = False)

def test_extract_sentence_with_adjectives():
    extract_sentence_with_adjectives(sentence_list)
