"""
 >>> Author: Fanny Dolisy
 >>> Title: ngram_program1
 >>> Portfolio Link: https://fdolisy.github.io/NLP_portfolio/
 >>> To run: `[your systems python keyword] ngram_program1.py`
"""

from nltk import word_tokenize
import pickle
from nltk.util import ngrams
from typing import Tuple
import os

def build_language_dicts(file_name: str)  -> Tuple[dict, dict]:
    """
        Builds the unigram and bigrams dicts given a corpus
        Args: str
            file_name: the corpus
        Returns: dict, dict
            the unigram dict, the bigram dict
    """
    with open(file_name, 'r', encoding='latin1') as file:
        text = file.read().splitlines()
        text = " ".join(text)
    file.close()

    tokens = word_tokenize(text)
    unigrams = list(ngrams(tokens, 1))
    bigrams =  list(ngrams(unigrams, 2))

    unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}
    return unigram_dict, bigram_dict

def get_data_filepath(filepath: str) -> str:
    """
    Gets the cross platform filepath of the data file
    Returns: string
        the file path
    """
    current_dir = os.getcwd()
    return os.path.join(current_dir, filepath)

def main():
    """
    pickels unigram and bigram dicts for each language corpus
    """
    en_unigram, en_bigram = build_language_dicts(get_data_filepath('data\LangId.train.English'))
    fr_unigram, fr_bigram = build_language_dicts(get_data_filepath('data\LangId.train.French'))
    it_unigram, it_bigram = build_language_dicts(get_data_filepath('data\LangId.train.Italian'))

    pickle.dump(en_unigram, open('en_uni.p', 'wb')) 
    pickle.dump(en_bigram, open('en_bi.p', 'wb')) 
    pickle.dump(fr_unigram, open('fr_uni.p', 'wb')) 
    pickle.dump(fr_bigram, open('fr_bi.p', 'wb')) 
    pickle.dump(it_unigram, open('it_uni.p', 'wb')) 
    pickle.dump(it_bigram, open('it_bi.p', 'wb')) 


if __name__ == "__main__":
    main()



