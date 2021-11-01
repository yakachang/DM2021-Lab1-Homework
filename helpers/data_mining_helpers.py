import nltk
import re

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    text = text.lower()
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            print(word)
            if word not in [',', '.', '!', '?']:
                tokens.append(word)
    return tokens


# if __name__ == '__main__':
#     test = [
#         'So there is no way for me to plug it in here in the US unless I go by a converter.',
#         'Good case, Excellent value.',
#         'Great for the jawbone.',
#         'So Far So Good!.',
#         'I advise EVERYONE DO NOT BE FOOLED!'
#     ]

#     for sent in test:
#         print(tokenize_text(sent))