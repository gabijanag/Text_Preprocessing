from prep_techniques import *
import numpy as np


'''Load data'''
neg_reviews = [line.rstrip('\n') for line in open('rt-polarity.neg')]

'''Preprocess data'''
prepped_data = []
def data_prep(data):
    for line in range(0, len(data)):

        # Replace contractions to their equivalents
        review = expand_contractions(str(data[line]))

        # Remove all single characters
        review = re.sub(r'\b[a-zA-Z]\b', ' ', review)

        # Remove punctuation and numbers
        review = re.sub('[^a-zA-Z ]', ' ', review)

        # Replace multiple spaces with a single space
        review = re.sub(' +', ' ', review)

        # Replace slang words and abbreviations with their equivalents
        review = replace_slang(review)

        # Replace not and the next word with the antonym
        tokens = nltk.word_tokenize(review)
        tokens = replace_negations(tokens)

        review = ' '.join(tokens)
        prepped_data.append(review + "\n")
    return prepped_data

neg_reviews = data_prep(neg_reviews)


# See the results of prepped data in a txt file
with open ("test", "w") as file:
    for line in neg_reviews:
        file.write(line)
