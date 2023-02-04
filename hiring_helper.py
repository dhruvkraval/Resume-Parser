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


for k in range(1,100):
    # open the pdf file
    reader = PdfReader('example.pdf')
    # extracting text from page
    # get number of pages

    # define keyterms
    scores ={} 
    # extract text and do the search
    for i in range(0, reader.pages):
        page = reader.pages[i]
        resume = page.extract_text()
        scores[i] = percent_match(resume)


print(scores)
    

        
