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
import percent_match
import suggestions
from PyPDF2 import PdfReader
import os
# assign directory

directory = 'files'
job =  "txt"


f = os.path.join(directory, filename)
scores ={} 
# extract text and do the search
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        reader = PdfReader('filename')
        page = reader.pages[0]
        resume = page.extract_text()
        scores[filename] = percent_match(resume,job)


scores = sorted(scores)

    

        
