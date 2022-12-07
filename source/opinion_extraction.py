#  Copyright Minaoar Hossain Tanzil, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

from bs4 import BeautifulSoup
import spacy

## Coreference Resolution (replacing pronouns with the actual noun)
# import neuralcoref
# # load NeuralCoref and add it to the pipe of SpaCy's model
# coref = neuralcoref.NeuralCoref(nlp.vocab)
# nlp.add_pipe(coref, name='neuralcoref')

# import coreferee
# nlp = spacy.load("en_core_web_trf")
# nlp.add_pipe('coreferee')

POSITIVE_WORD_FILE = "../data/positive-words.txt"
NEGATIVE_WORD_FILE = "../data/negative-words.txt"

import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from config import *

# read word list from a text file. Each line contains a word
def read_word_list(file_name):
    word_list = []
    with open(file_name) as f:
        for line in f:
            word_list.append(line.strip())
    return word_list

positive_word_list = read_word_list(POSITIVE_WORD_FILE)
negative_word_list = read_word_list(NEGATIVE_WORD_FILE)


nlp = spacy.load("en_core_web_lg")



def remove_code_snippet(body_soup):
    for code in body_soup.find_all('code'):
        code.decompose()
    return body_soup

def process_raw_text_body(body):
    soup = BeautifulSoup(body, 'html.parser')
    remove_code_snippet(soup)
    body = soup.get_text()
    return body

def process_raw_text(body):
    body = process_raw_text_body(body)
    sentences = breakdown_sentences(body)
    return sentences

# def resolve_coreference(doc):
#     # use Spacy to resolve coreference
#     print(doc._.coref_chains.resolve(doc))
#     return doc


def breakdown_sentences(body):
    # use Spacy to break down sentences
    doc = nlp(body)

    # resolve coreference
    # doc = resolve_coreference(doc)

    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences

def extract_sentence_with_keywords(sentence_list, keywords, minimum_presence=1, add_keyword = False):
    # remove sentences that do not contain the keywords

    sentences = []
    for sent in sentence_list:
        presence = 0

        # use Spacy to break down sentences
        doc = nlp(sent)

        # count the number of keywords contained among the doc tokens
        for keyword in keywords:
            for token in doc:
                if token.text.lower() == keyword.lower():
                    presence += 1
                    if add_keyword:
                        sent ='<' + keyword + '> ' + sent
                    break
        
        # if the number of keywords is greater than the minimum presence, add the sentence to the list
        if presence >= minimum_presence:
            sentences.append(sent)
        
    
    return sentences

def extract_sentence_with_adjectives(sentence_list):
    # remove sentences that do not contain ajdective
    sentences = []
    for sent in sentence_list:
        doc = nlp(sent)
        for token in doc:
            if token.pos_ == 'ADJ':
                sentences.append(sent)
                break
    
    # keep sentences that contain positive or negative words
    sentences_with_positive_words = []
    sentences_with_negative_words = []
    
    sentences_with_positive_words = extract_sentence_with_keywords(sentences, positive_word_list, 1, True)
    sentences_with_negative_words = extract_sentence_with_keywords(sentences, negative_word_list, 1, True)

    # join unique sentences
    sentences = list(set(sentences_with_positive_words + sentences_with_negative_words))

    return sentences
    
if __name__ == "__main__":
    input = '<p>Hi, I am trying to connect to mysql database using mysql.connector. I am getting the following error:</p>'
    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Raw input text:\n"+ input)

    processed_sentences = process_raw_text(input)

    logging.log(LOG_LEVEL_APPLICATION_DEBUG, "Identified sentences:\n"+ str(processed_sentences))
