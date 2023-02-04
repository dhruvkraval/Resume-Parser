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




print("GIVE RESUME")
reader = PdfReader('example.pdf')
page = reader.pages[0]
# extracting text from page
resume = page.extract_text()
print("GIVE JOB DESCRIPTION")
job = str(input())
job = "Minimum qualifications:  Currently enrolled in a Bachelor's degree in Computer Science, Linguistics, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics, or Natural Sciences. Experience in one area of computer science (e.g., Natural Language Understanding, Computer Vision, Machine Learning, Deep Learning, Algorithmic Foundations of Optimization, Quantum Information Science, Data Science, Software Engineering, etc.). Preferred qualifications:  Currently attending a degree program in the US. Currently enrolled in a full-time degree program and returning to the program after completion of the internship. Experience as a researcher, including internships, full-time, or at a lab. Experience contributing research to communities or efforts, including publishing papers in conferences or journals. Experience with one or more general purpose programming languages (e.g., C/C++, Java, MATLAB, Go, Python, etc.). Ability to speak and write in English fluently. About the job  The Student Researcher Program’s primary objective is to foster academic collaborations with students through research at Google. Join us for a paid Student Researcher position that offers the opportunity to work directly with Google research scientists and engineers on research projects.  The Student Researcher Program offers more opportunities for research students to work on critical research projects at Google in a less structured way. The program allows opportunities beyond the limitations of our traditional internship program on aspects such as duration, time commitment, and working location (with options for on-site or remote). The topics student researchers work on tend to be open-ended and exploratory, and don't always have a clear deliverable like a traditional internship would.  Google Research is building the next generation of intelligent systems for all Google products. To achieve this, we’re working on projects that utilize the latest computer science techniques developed by skilled software engineers and research scientists. Google Research teams collaborate closely with other teams across Google, maintaining the flexibility and versatility required to adapt new projects and foci that meet the demands of the world's fast-paced business needs.   The US base salary range for this full-time position is $90,000-$110,000. Our salary ranges are determined by role, level, and location. The range displayed on each job posting reflects the minimum and maximum target for new hire salaries for the position across all US locations. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.  Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google."
#returns the match perecentage
matchPercentage = percent_match.percent_match(resume, job)

print(str(matchPercentage)+ "% match")

print("SUGGESTED WORDS TO INCLUDE IN YOUR RESUME")
#returns the suggested phrases
print(suggestions.suggestions(job,resume))



