from nltk import word_tokenize

s1="I love@Coding and=ML+and-NLP"
s2=word_tokenize(s1)
print(s1)

s3=s1.split(" ")
print(s3)