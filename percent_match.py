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

def clean(txt):
     ## Cleans Text
     clean_txt = txt.lower()
     # remove punctuation
     clean_txt = re.sub(r'[^\w\s]', '', clean_txt)
     # remove trailing spaces
     clean_txt = clean_txt.strip()
     # remove numbers
     clean_txt = re.sub('[0-9]+', '', clean_txt)
     # tokenize 
     clean_txt = word_tokenize(clean_txt)
     # remove stop words
     stop = stopwords.words('english')
     clean_txt = [w for w in clean_txt if not w in stop] 
     return(' '.join([str(elem) for elem in clean_txt]))
def noun(txt):
     blob = TextBlob(txt)
     return blob.noun_phrases

def percent_match (resume, job):
    resume = (' '.join([str(elem) for elem in noun(clean(resume))]))
    job = (' '.join([str(elem) for elem in noun(clean(job))]))
    #resume = clean(resume)
    #job = clean(job)
    text = [resume, job]

    print(resume)
    print(job)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)



    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    #matchPercentage = math.sqrt(matchPercentage) *10 
    #matchPercentage = math.sqrt(matchPercentage) *10 
    return round(matchPercentage, 2)
