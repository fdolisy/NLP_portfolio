"""
 >>> Author: Fanny Dolisy
 >>> Title: Web Crawler
 >>> Portfolio Link: https://fdolisy.github.io/NLP_portfolio/
 >>> To run: `[your systems python keyword] webcrawler.py`
 >>> *this program uses sqlite to create a db knowledge base
"""
from bs4 import BeautifulSoup
import urllib.request
from pip._vendor import requests
import re
import nltk
from nltk import sent_tokenize, word_tokenize
from collections import Counter
import ssl
import pickle
import datetime
import sqlite3


def is_recent_link(link: str) -> bool:
    """
    Determines if a link is from at least 2020
    Args: link
       the link to be checked
    Returns: bool
       T/F if the link is from 2020 or later
    """
    year_match = re.search(r'\b(20[2-9][0-9])\b', link)
    if year_match is None:
        return False
    year = int(year_match.group(1))
    
    # Check if year is 2020 or later
    now = datetime.datetime.now()
    if year >= now.year - 3:
        return True
    else:
        return False


def get_links(starter_url: str) -> list:
    """
    Gets links based off certain criteria, in this case for Jeff Bezos links
    Args: str
        starter_url: the starting link for the crawler
    Returns: list
       the list of links from the crawler, to be scraped
    """
    links = set()
    links.add(starter_url)
    request = requests.get(starter_url)
    soup = BeautifulSoup(request.text, features='html.parser')

    forbidden_sites = [ 
                        'wiki', 
                        'nytimes', 
                        'ir.aboutamazon.com', 
                        'archive', 
                        'upi', 
                        'obama']
    forbidden_sites_regex = r'(?:{})'.format('|'.join(forbidden_sites))

    for link in soup.find_all('a'):
        link_str = str(link.get('href'))
        if 'bezos' or 'amazon' in link_str.casefold():
            if '&' in link_str:
                i = link_str.find('&')
                link_str = link_str[:i]
            if (link_str.startswith('http') and
                re.search(forbidden_sites_regex, link_str) is None and
                is_recent_link(link_str)):
                    links.add(link_str)
    return list(links)


def preprocess_page_text(text: str) -> str:
    """
    Cleans up page text prior to processing, removes new lines, tabs, etc.
    Args: str
        text: the text to be cleaned
    Returns: str
      the cleaned up text
    """
    text = text.replace("\n", "").replace("\t", "").replace("[", "").replace("]","")
    text = re.sub('\s+', ' ', text)

    return text


def scrape_page_data(links: list) -> None:
    """
    scrapes page data to a file
    Args: list
        links: the list of links to scrape
    """
    # ssl certificate
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    count = 1
    for link in links:
        print(f"[{count}] - {link}")
        html = urllib.request.urlopen(link, context=context)
        soup = BeautifulSoup(html, features='html.parser')
        f = open("fileIn"+str(count)+ ".txt", 'w', encoding="utf-8")
        allowed_tags = ['p'] # p is the paragraph tag
        scraped_text = [t for t in soup.find_all(string=True) if t.parent.name in allowed_tags]
        f.write(' '.join(scraped_text))
        f.close()
        count += 1


def validate_sentence_length(sentences: list):
    """
    Removes "sentences" that skew the scraped data (one word sentences, lables, etc)
    Args: list
        sentences: the sentences to be validated
    Returns: list
      the valid sentences
    """
    for sent in sentences:
        num_words= len(re.findall(r'\w+', sent))
        if num_words < 7:
            sentences.remove(sent)
    return sentences


def write_sentences(num_files: int) -> None:
    """
    Extracts sentences from scraped data and puts them into a file
    Args: int
        num_files: the number of files that were scraped
    """
    for file in range(1, num_files + 1):
        f = open("fileIn"+str(file)+".txt", 'r', encoding="utf-8")
        text = f.read()
        f.close()

        sentences = sent_tokenize(preprocess_page_text(text))
        #sentences = validate_sentence_length(sentences)
        f = open("fileOut"+str(file)+".txt", 'w', encoding="utf-8")
        f.write('\n'.join(sentences))
        f.close()


def create_tf_dict(doc: str, tf_dict: dict) -> Counter:
    """
    Create a term frequency dictionary for all terms that have been scraped, merges with previous dictionary 
    from previously scraped document
    Args: str, dict
        doc: the doc to get the term frequency of
        tf_dict: the current term frequency dictionary
    Return: dict
        the current tf_dict
    """
    text = re.sub(r'[.?!,:;()\-\n\d]',' ', doc.lower())
    tokens = word_tokenize(text)
    stopwords = nltk.corpus.stopwords.words('english')
    my_stop_words = ['one', 'would', 'like', 'later', 'us', 'said', 'also', 'could']
    tokens = [w for w in tokens if w.isalpha() and w not in stopwords and w not in my_stop_words]
     
    # get term frequencies
    for t in tokens:
        if len(t) == 1:
            continue
        if t in tf_dict:
            tf_dict[t] += 1
        else:
            tf_dict[t] = 1
            
    # get term frequencies in a more Pythonic way
    token_set = set(tokens)
    tf_dict = {t:tokens.count(t) for t in token_set}
    
    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)
        
    return Counter(tf_dict)


def get_overall_dict(num_files: int) -> dict:
    """
    Sorts the final term dictionary
    Args: int
        num_files: the number of files that were scraped
    Return: dict
        returns the term dict organized from most to least frequent term
    """
    tf_dict = Counter({})
    for file in range(1, num_files + 1):

        with open("fileOut"+str(file)+".txt", 'r', encoding="utf-8") as f:
            text =  f.read()
        f.close()
        tf_dict = tf_dict + create_tf_dict(text, tf_dict)
    
    return dict(sorted(tf_dict.items(), key=lambda item: item[1], reverse=True))


def build_knowledge_base(num_files: int, kb: dict) -> dict:
    """
    Builds a knowledge base by creating a dict with the form "term: sentences with the term present"

    Args: int
        num_files: the number of files that were scraped
        kb: the knowledge base with the keys inputted
    Returns
        the complete knowledge base
    """
    sentence_count = {"Jeff": 0, "Amazon": 0, "worth": 0, "billion": 0, "Blue": 0, "company": 0, "Washington": 0, "climate": 0, "CEO": 0, "announced": 0}
    for file in range(1, num_files + 1):
        with open("fileOut"+str(file)+".txt", 'r', encoding="utf-8") as f:
            text =  f.read()
        f.close()
        sents = sent_tokenize(text)
        sents = validate_sentence_length(sents)
        for sent in sents:
            for word in kb.keys():
                if word in sent and sentence_count[word] < 75:
                    kb[word] = kb[word] + " " + sent 
                    sentence_count[word] += 1 
    return kb


def reorganize_by_sentence_len(sentences: str) -> list:
    """
    Reorganizes a str of setences by the length of the sentence

    Args: str
        sentences: the str to reorganize
    Returns list
        the list of ordered sentences
    """
    sentences = sentences.split('.')
    sorted_sentences = sorted(sentences, key=lambda s: len(s))
    return sorted_sentences


def main():
    links = get_links("https://en.wikipedia.org/wiki/Jeff_Bezos")
    scrape_page_data(links)
    write_sentences(len(links))
    tf_dict = get_overall_dict(len(links))
    most_common = list(tf_dict.keys())[:40]

    count = 1
    for word in most_common:
        print(f"[{count}] {word}")
        count += 1
    
    # my manually selected words
    selected_words = {"announced":"", "Washington": "", "CEO":"", "Blue": "", "climate":"", "worth": "", "Jeff": "", "company": "", "billion": "", "Amazon": "",}
    
    # have a pickled knowledge base
    kb = build_knowledge_base(len(links), selected_words)
    pickle.dump(kb, open('knowledge_base.p', 'wb')) 

    # have a database knowledge base
    conn = sqlite3.connect('knowledge_base.db')
    cur = conn.cursor()

    # Create a table
    cur.execute("DROP table IF EXISTS knowledge_base")
    cur.execute('''CREATE TABLE knowledge_base
                (term VARCHAR(255) NOT NULL PRIMARY KEY,
                facts TEXT NOT NULL)''')
    for term, facts in kb.items():
        sql = "INSERT INTO knowledge_base (term, facts) VALUES (?, ?)"
        val = (term, facts)
        cur.execute(sql, val)
        conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
