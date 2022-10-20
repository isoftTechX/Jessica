import numpy as np
import nltk 
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenize(sentence):
    """split the sentence into words"""
    return nltk.word_tokenize(sentence)

def stem(word):
    """Split the word into letters"""
    return Stemmer.stem(word.lower())

def wordCollection(tokenizedSentence, words):
    sentenceWord = [stem(word) for word in tokenizedSentence]
    collection = np.zeros(len(words), dtype = np.float32)

    for idx, w in enumerate(words):
        if w in sentenceWord:
            collection[idx] = 1

    return collection