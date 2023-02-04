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
reader = PdfReader('Resume-12.pdf')
page = reader.pages[0]
# extracting text from page
resume = page.extract_text()
#resume = "Nayan Menezes nayanmenezes2@gmail.com 847-769-9486 || Buffalo Grove, Illinois 60089 EDUCATION Iowa State University Bachelors of Science, Computer Science Expected Graduation: May 2026 GPA: 3.67/4.00 Courses Completed: Intro to Object Oriented Programming, Linear Algebra Courses In Progress: Introduction to Data Structures, Discrete Computational Structures Adlai E. Stevenson High School High School Diploma Graduated May 2022 GPA: 4.42/4.00 LEADERSHIP Adlai E. Stevenson High School Diversity Council Executive Activities Director (August 2020-May 2022) ● Led in arranging activities and events which fostered a sense of acceptance and appreciation for all cultures, religions, and personal identities within the school community and throughout the world, also helped raise $10,000 dollars for local charities through Diversity Council’s World’s Fair, which was an event which allow students of the school to express and share the culture from their country of origin Essential Items Donation Leader (October 2020-January 2021) ● Advertised and gathered essential items (i.e. soap, paper towels, shampoo, toothpaste etc.) from school community and local neighborhoods for school’s Rotary Youth Club, donated over 300 items to struggling individuals and families in local suburban area PROJECTS Dart Game (Java) ● Implemented the GUI for a functional dart game which allows two users to throw darts with permitted values from user ● Difficulties stemmed from specifications within the game of darts such as handling cases like doubling in, resolved through implementation of helper method which handled edge cases Lyne Game (Java) ● Accomplished the creation for the GUI of the Lyne Game in which users would connected different colored lines in a puzzle like manner ● Difficulties arose from which grid squares the user is allowed to enter through, resolved by creating a private square adjacency method  PROGRAMMING SKILLS Languages: Java, Python (beginner), HTML (beginner) Framework: BlueJ, Eclipse AWARDS ● AP Scholar w/Distinction (2021-2022) ● Adlai E. Stevenson High Honors (2018-2022) ● Illinois State Scholar (2021-2022) ● George Washington Carver Scholar (2022-Present) ● Liberal Arts and Sciences Dean’s Excellence Award (2022-Present) ● Iowa State Dean’s List (2022-Present)"
print("GIVE JOB DESCRIPTION")
#job = str(input())
job = "Minimum qualifications:  Currently enrolled in a Bachelor's degree in Computer Science, Linguistics, Statistics, Biostatistics, Applied Mathematics, Operations Research, Economics, or Natural Sciences. Experience in one area of computer science (e.g., Natural Language Understanding, Computer Vision, Machine Learning, Deep Learning, Algorithmic Foundations of Optimization, Quantum Information Science, Data Science, Software Engineering, etc.). Preferred qualifications:  Currently attending a degree program in the US. Currently enrolled in a full-time degree program and returning to the program after completion of the internship. Experience as a researcher, including internships, full-time, or at a lab. Experience contributing research to communities or efforts, including publishing papers in conferences or journals. Experience with one or more general purpose programming languages (e.g., C/C++, Java, MATLAB, Go, Python, etc.). Ability to speak and write in English fluently. About the job  The Student Researcher Program’s primary objective is to foster academic collaborations with students through research at Google. Join us for a paid Student Researcher position that offers the opportunity to work directly with Google research scientists and engineers on research projects.  The Student Researcher Program offers more opportunities for research students to work on critical research projects at Google in a less structured way. The program allows opportunities beyond the limitations of our traditional internship program on aspects such as duration, time commitment, and working location (with options for on-site or remote). The topics student researchers work on tend to be open-ended and exploratory, and don't always have a clear deliverable like a traditional internship would.  Google Research is building the next generation of intelligent systems for all Google products. To achieve this, we’re working on projects that utilize the latest computer science techniques developed by skilled software engineers and research scientists. Google Research teams collaborate closely with other teams across Google, maintaining the flexibility and versatility required to adapt new projects and foci that meet the demands of the world's fast-paced business needs.   The US base salary range for this full-time position is $90,000-$110,000. Our salary ranges are determined by role, level, and location. The range displayed on each job posting reflects the minimum and maximum target for new hire salaries for the position across all US locations. Within the range, individual pay is determined by work location and additional factors, including job-related skills, experience, and relevant education or training. Your recruiter can share more about the specific salary range for your preferred location during the hiring process.  Please note that the compensation details listed in US role postings reflect the base salary only, and do not include bonus, equity, or benefits. Learn more about benefits at Google."
#returns the match perecentage
matchPercentage = percent_match.percent_match(resume, job)

print(str(matchPercentage)+ "% match")
print(percent_match.rating(matchPercentage))

print("SUGGESTED WORDS TO INCLUDE IN YOUR RESUME")
#returns the suggested phrases
print(suggestions.suggestions(job,resume))



