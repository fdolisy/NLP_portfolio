# NLP_portfolio
This is a repository for natural language processing projects

## Overview of NLP
[Here](pdfs/Overview_of_NLP.pdf) is a brief overview about NLP!

## Program 1 - Text Processing in python :fountain_pen:

### Overview
[Here](Python_Text_Processing/Homework1_fcd180001.py) is a python program that does basic text processing with a [csv](Python_Text_Processing/data/data.csv) file

This program simply reads in a csv data file filled with data about people, normalizes this data and outputs this data in a clean format. The data normalization includes verifying the formats of various attributes, adding missing data and ensuring there are no duplicates for unique attributes.

To run this program in the command line run 
`[your systems python keyword] Homework1_fcd180001 data/data.csv`
>Your systems python keyword includes: py, python, python3, ex: `py Homework1_fcd180001.py data/data.csv`

### Strengths and Weaknessess of Text Processing in python

In my opinion, python has a lot of great libraries that can be used to make text processing very easy to process textual data. Though it can be much slower than other languages when using some of these libraries, python is still a wildly popular choice for text processing, as many people still use it for NLP based applications.

### What I learned
I have a large amount of work experience in python, so this assignment was a nice review for me. I did learn a few very specific things, such as how to make a “main” function in python, how to make file paths be cross platform and how to use pickle as a whole.

## Program 2 - Guessing Game :dart:
[Here](Guessing_Game/Hw2_fcd180001.py) is a python program that normalizes data and uses it in a guessing game. The data comes from [this](Guessing_Game/anat19.txt) text file containing a chapter of an anatomy textbook.

## Portfolio 3 - WordNet :goal_net:
[Here](pdfs/WordNet.pdf) is a pdf containing usage example of wordnet in NLTK. 

## Portfolio 4 - Sentence Parsing :page_with_curl:
[Here](pdfs/sentence_parsing.pdf) is a display of three different methods of sentence parsing. 

## Portfolio 5 - N-grams :balance_scale:
In order to create an ngram model for this [data](Ngram/data/wordLangId.out), two programs must be run:

1. [program 1](Ngram/ngram_program1.py) creates unigram and bigram dictionaries for the given corpus - in this case 3 documents one in english, french and italian
2. Using the resulting files from program 1, we can now run [program 2](Ngram/ngram_program2.py) to find the accuracy of the model we create, the results are written to [Identifications.txt](Ngram/Identifications.txt).

