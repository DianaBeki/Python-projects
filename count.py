from email.mime import text
from string import whitespace


text = 'I love python and javascript'

# remove whitespace using split()
word_list = text.split()

# number of words
number_of_words = len(word_list)

# print the result

print(number_of_words)

