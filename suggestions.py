import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import operator
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
set(stopwords.words('english'))
from nltk.probability import FreqDist
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import math

def UncommonWords(A, B):
 
    # count will contain all the word counts
    count = {}
 
    # insert words of string A to hash
    for word in A.split():
        count[word] = count.get(word, 0) + 1
 
    # insert words of string B to hash
    for word in B.split():
        count[word] = count.get(word, 0) + 1
 
    # return required list of words
    return [word for word in count if count[word] == 1]


def suggestions(job, resume):
    temp = UncommonWords(job, resume)
    temp = ' '.join([str(elem) for elem in temp])
    temp1 = UncommonWords(temp, resume)
    temp1 = ' '.join([str(elem) for elem in temp1])
    blob = TextBlob(temp1)
    return blob.noun_phrases