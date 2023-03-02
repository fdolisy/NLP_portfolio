"""
 >>> Author: Fanny Dolisy
 >>> Title: ngram_program1
 >>> Portfolio Link: https://fdolisy.github.io/NLP_portfolio/
 >>> To run: `[your systems python keyword] ngram_program2.py`
 >>> *ensure that ngram_program1.py has been run first so the langauge dictionaries are available
"""
import pickle
from nltk.util import ngrams
from nltk import word_tokenize
import math

def compute_accuracy() -> int:
    """
        Calculate the accuracy of the predictictions my model produced
        Returns: int
            the accuracy of the model
    """
    test_file = open('data/LangId.sol', 'r')
    my_results = open('identifications.txt')
    test_file_data = test_file.readlines()
    my_results_data = my_results.readlines()
    i = 0
    num_correct = 0
    for i in range(len(test_file_data)):
        if test_file_data[i] != my_results_data[i]:
            print(f"Difference in Line {i + 1}")
            print(f"Expected: {test_file_data[i].strip()}")
            print(f"My result: {my_results_data[i]}")
        else:
            num_correct += 1
    
    test_file.close()
    my_results.close()
    return num_correct/i * 100

def calc_bigram_laplace_probability(bigram: list, unigram_dict: dict, bigram_dict: dict, v: int) -> int:
    """
    Calculates the laplace probability of one bigram 
    Args: list, dict, dict, int
        bigram: the bugram to be analzed
        unigram_dict: dictionary of unigrams in that lang
        bigram_dict: dictionary of bigrams in that lang
    Returns: int
        the probability of bigram
    """
    b = bigram_dict[bigram] if bigram in bigram_dict else 0
    u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
    return math.log(((b + 1) / (u + v)))

def main():
    output = open("Identifications.txt", "w")
    file = open('data/LangId.test', 'r', encoding='latin1')
    
    it_uni = pickle.load(open('it_uni.p', 'rb')) 
    it_bi = pickle.load(open('it_bi.p', 'rb'))  
    en_uni = pickle.load(open('en_uni.p', 'rb'))
    en_bi = pickle.load(open('en_bi.p', 'rb')) 
    fr_uni = pickle.load(open('fr_uni.p', 'rb'))
    fr_bi = pickle.load(open('fr_bi.p', 'rb')) 
    
    count = 1 
    while True:
        p_fr = p_it = p_en = 0
        text = file.readline()
        if not text:
            break
        if not text.strip():
            continue
        tokens = word_tokenize(text)
        unigrams_test = list(ngrams(tokens, 1))
        bigrams_test =  list(ngrams(unigrams_test, 2))

        v = len(it_uni) + len(en_uni) + len(fr_uni)

        for bigram in bigrams_test:
            # probability of language ident for the bigram
            p_fr +=  calc_bigram_laplace_probability(bigram,fr_uni,fr_bi,v)
            p_en +=  calc_bigram_laplace_probability(bigram,en_uni,en_bi,v)
            p_it +=  calc_bigram_laplace_probability(bigram,it_uni,it_bi,v)

        prob_dict = {"English":p_en,"Italian": p_it, "French": p_fr}
        predicted_lang = max(prob_dict, key=prob_dict.get)
        # line for debugging
        # print(f"{count} EN - {p_en}, IT - {p_it}, FR - {p_fr}")
        output.write(f"{count} {predicted_lang}\n")
        count += 1
        
    file.close()
    output.close()
    print(f"{compute_accuracy()}% accurate")
    
if __name__ == "__main__":
    main()