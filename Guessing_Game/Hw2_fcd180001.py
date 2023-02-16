"""
 >>> Author: Fanny Dolisy
 >>> Title: Guessing Game
 >>> Portfolio Link: https://fdolisy.github.io/NLP_portfolio/
"""

import sys
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import Tuple
import operator
from random import seed, randint
import re
import os

# seed for random
seed(1233)

def get_data_filepath(filepath: str) -> str:
    """
    Gets the cross platform filepath of the data file
    Returns: string
        the file path
    """
    current_dir = os.getcwd()
    print(f"{os.path.join(current_dir, filepath)}")
    return os.path.join(current_dir, filepath)


def read_in_raw_text(filepath: str)-> str:
    """
    Reads in the content of the file
    Args: str
        filepath: the sysarg file path
    Returns: str
        the content of the file as a string
    """
    with open(filepath , 'r') as reader:
        raw_text = reader.read()
    reader.close()
    return raw_text


def calculate_lexical_diversity(raw_text: str) -> str:
    """
    Calculates the lexical diversity of a text
    Args: str
        raw_text: the text to be analyzed
    Returns: str
        the lexical diversity to be displayed
    """
    tokens = word_tokenize(raw_text)
    total_num_tokens = len(tokens)
    num_unique_tokens = len(set(tokens))
    lexical_diversity = num_unique_tokens/total_num_tokens  
    return str(round(lexical_diversity, 2)) 


def preprocess_raw_text(text: str) -> Tuple[list, list]:
    """
    Normalizes the raw text recieved
    Args: str
        text: the text to be normalized
    Returns: list[str], list[str]
        the found lists of tokens and nouns
    """
    lower_text = text.lower()
    tokens = word_tokenize(lower_text)
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if not t in stop_words and len(t) > 5 and t.isalpha()]
    
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    unique_lemmas = set(lemmas)
    tags = pos_tag(unique_lemmas)
    tagged = [x for x in tags]
    print(f"First 20 tags")
    for tag in tagged[:20]:
        print(f"{tag[0]} - {tag[1]}")
    print()
    nouns = [x[0] for x in tags if x[1].startswith("N")]
    print(f"Number of tokens -> {len(tokens)}, Number of nouns -> {len(nouns)} ")
    return tokens, nouns


def generate_noun_list(tokens: list, nouns: list) -> list:
    """
    Generates the word list to be used in the guessing game
    Args: list, list
        tokens: the list of normalized tokens
        nouns: the list of nouns from the tokens
    Returns: list
        the top 50 most common nouns
    """
    noun_dict = {}
    for i in range(len(nouns)):
        noun_dict[nouns[i]] = tokens.count(nouns[i])

    sorted_noun_dict = dict(sorted(noun_dict.items(), key=operator.itemgetter(1), reverse=True))
    sorted_nouns = list(sorted_noun_dict.items())[:50]
    print("50 most common words")
    for noun, count in sorted_nouns:
        print(f"{noun} - {count}")
    return list(sorted_noun_dict.keys())[:50]


class GuessingGame:
    def __init__(self, word_list):
        """
        Constructor
        """
        self.word_list = word_list
        self.points = 5
    

    def select_word_from_list(self) -> str:
        """
        Randomly Selects a word from the list of most common words
        Returns: str
            the found word
        """
        word_choice_pos = randint(0, 49)
        return self.word_list[word_choice_pos]


    def replace_blank(self, display: str, guess: str , position: int) -> str:
        """
        Utility function to update the displayed word
        Args: str, str, int
            display: the display text that needs to be updated
            guess: the guessed char
            position: the position of the guessed char
        Returns: str
            the updated text to be displayed
        """
        return display[:position] + guess  + display[position+1:]


    def run_game(self) -> None:
        """
        The guessing game routine
        Returns: None
        """
        word = self.select_word_from_list()
        display = '_ ' * len(word)
        while self.points > 0:
            print(display)
            guess = input("Guess a letter ->").lower()
            if guess == '!':
                break
            if not guess.isalpha():
                print("That is an invalid guess, please guess again")
                continue
            if guess not in word:
                self.points -= 1
                print(f"Sorry, guess again. Score is {self.points}")
            elif (guess in word) and guess not in display:
                self.points += 1
                print(f"Right, Score is {self.points}")
                positions_to_update = [2 * i.start() for i in re.finditer(guess, word)]
                for i in positions_to_update:
                    display = self.replace_blank(display, guess, i)
                if display.replace(" ","") == word:
                    print(f"you solved it!")
                    print(f"Current score is {self.points}")
                    print(f"Guess Another Word")
                    return
        print(f"game over: the word was {word} - score {self.points}")
        exit()
    
                               
def main():
    """
    driver
    """
    if len(sys.argv) != 2:
        print(f"ERROR: have one system argument containing the file with the data")
        exit()
    else:
       inputted_file = sys.argv[1]
    filepath = get_data_filepath(inputted_file)
    raw = read_in_raw_text(filepath)
    print(f"Lexical Diversity: {calculate_lexical_diversity(raw)}")
    
    tokens, nouns = preprocess_raw_text(raw)
    word_list = generate_noun_list(tokens, nouns)
    print(f"Let's play a word guessing game!")
    game = GuessingGame(word_list)
    while True:
        game.run_game()

    

if __name__ == "__main__":
    main()
