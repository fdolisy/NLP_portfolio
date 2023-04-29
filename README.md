# NLP_portfolio
This is a repository for natural language processing projects. They are all split up by assignments.

==> [Skills Used](SKILLS.md)

==> [Assignment 1](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_1)

==> [Assignment 2](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_2)

==> [Assignment 3](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_3)

==> [Assignment 4](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_4)

==> [Assignment 5](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_5)

==> [Assignment 6](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_6)

==> [Assignment 7](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_7)

==> [Assignment 8](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_8)

==> [Assignment 10](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_10)

# Index Page
## Overview of NLP
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Overview_of_NLP.pdf) is a brief overview about NLP!

## Assignment 1 - Text Processing in python :fountain_pen:

### Overview
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_1/Homework1_fcd180001.py) is a python Assignment that does basic text processing with a [csv](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_1/data/data.csv) file

This program simply reads in a csv data file filled with data about people, normalizes this data and outputs this data in a clean format. The data normalization includes verifying the formats of various attributes, adding missing data and ensuring there are no duplicates for unique attributes.

To run this program in the command line run 
`[your systems python keyword] Homework1_fcd180001 data/data.csv`
>Your systems python keyword includes: py, python, python3, ex: `py Homework1_fcd180001.py data/data.csv`

### Strengths and Weaknessess of Text Processing in python

In my opinion, python has a lot of great libraries that can be used to make text processing very easy to process textual data. Though it can be much slower than other languages when using some of these libraries, python is still a wildly popular choice for text processing, as many people still use it for NLP based applications.

### What I learned
I have a large amount of work experience in python, so this assignment was a nice review for me. I did learn a few very specific things, such as how to make a “main” function in python, how to make file paths be cross platform and how to use pickle as a whole.

## Assignment 2 - Guessing Game :dart:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_2/Hw2_fcd180001.py) is a python program that normalizes data and uses it in a guessing game. The data comes from [this](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_2/anat19.txt) text file containing a chapter of an anatomy textbook.

## Assignment 3 - WordNet :goal_net:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_3/WordNet.pdf) is a pdf containing usage example of wordnet in NLTK. 

## Assignment 4 - Sentence Parsing :page_with_curl:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_4/sentence_parsing.pdf) is a display of three different methods of sentence parsing. 

## Assignment 5 - N-grams :balance_scale:
In order to create an ngram model for this [data](https://github.com/fdolisy/NLP_portfolio/tree/main/Assignment_5/data), two programs must be run:

1. [program 1](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_5/ngram_program1.py) creates unigram and bigram dictionaries for the given corpus - in this case 3 documents one in english, french and italian
2. Using the resulting files from program 1, we can now run [program 2](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_5/ngram_program2.py) to find the accuracy of the model we create, the results are written to `Identifications.txt`.
   
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_5/Ngrams_Narrative.pdf) is an overview of ngrams

## Assignment 6 - WebCrawler :bug:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_6/webcrawler.py) is a program that scraped the jeffrey bezos wikipedia page to build a knowledge base about him. The related report about the logistics of the code and a sample chatbot can be found [here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_6/Web_Scraper_Report.pdf) .

To run ensure that the modules `bs4` and `requests` are installed, otherwise this code will not run. To install run `pip install [module name]`

## Assignment 7 - Text Classification 1 :star:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_7/TextClassification1.pdf) is a pdf that shows a comparison of naive bayes, logistic regresesiona ndueral networks on a small dataset. The dataset contains two columns, in one is a movie review, the other indicating if that review is a positive or negative one.

## Assignment 8 - ACL Paper Summary :fr:
[Here](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_8/ACL_Overview.pdf) is a pdf that writes a summary and analysis on the paper [French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_8/French_CrowS-Pairs.pdf)

## Assignment 9 - Chatbot :speech_balloon:
In this assignment, I collaborated with @cadybaltz to create a travel guide chatbot. Further deatils/code can be found in this [repository](https://github.com/fdolisy/TravelAgent)


## Assignment 10 - Text Classification 2 :speaker:
In this assignment I created multiple models to learn whether someone was depressed based off a collection of reddit comments that were compressed into a simple classification [dataset](https://www.kaggle.com/datasets/infamouscoder/depression-reddit-cleaned). My models, results and analysis can be found in this [pdf](https://github.com/fdolisy/NLP_portfolio/blob/main/Assignment_10/TextClassification2_fcd180001.pdf).

## Closing Summary
Prior to this semester I had little to no experience with NLP, other than minimal text processing in prior machine learning classes. However, with all of these assignments as dicussed above, I have gained invaluable experience with various NLP techniques. From learning the basics of preprocessing and normalizing to creating actual models that can accurately predict various pieces of data once trained, I learned that NLP has become a crucial skill in todays modern world. I cannot wait to further use these techniques in my own specific interests. I personally have always enjoyed designing compilers and cannot wait to use these new learned techniques to further develope better compilers and sytnax parsers (such as github copilot).

This technology seems to be changing every day, we had so much to talk about in terms of news in this class relating to things such as Chat-GPT and other rapidly growing technologies. It seems hard to manage in terms of keeping up with whats new in this field, but I plan to continue reading research papers with topics that peak my interest to see where this field is headed. Though I may not have a career in this field at the moment, I cannot wait to further devleope my own skills with my own personal projects as explained in my opening paragraph.

