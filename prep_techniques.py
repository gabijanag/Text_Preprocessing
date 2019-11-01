import re, unicodedata, unidecode
from functools import partial
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import wordnet, stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import inflect


##################
## Remove Noise ##
##################

def remove_html(text):
    """Strips away HTML markup"""
    soup = BeautifulSoup(text, 'lxml')
    html_free = soup.get_text()
    return html_free


def remove_between_square_brackets(text):
    """Removes open and close double brackets and anything in between them"""
    return re.sub('\[[^]]*\]', '', text)


def remove_accented_chars(text):
    """Converts accented characters from text, e.g. café to cafe"""
    text = unidecode.unidecode(text)
    return text


def remove_punctuation(words):
    """Removes punctuation from a list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def remove_non_ascii(words):
    """Removes non-ASCII characters from a list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


###################
## Deduplication ##
###################

def remove_dupes(text):
    """Removes duplicate rows"""
    seen = set()
    result = []
    for item in text:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


###################
## Normalization ##
###################

def to_lowercase(words):
    """Converts all characters to lowercase from a list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """Replaces all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    number_counter = 0
    new_words = []
    for word in words:
        if word.isdigit():
            number_counter += 1
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    print(f"Converted {number_counter} numbers to words.")
    return new_words


def remove_numbers(words):
    """Strips digits from a list of tokenized words"""
    no_digits = []
    for i in words:
        if not i.isdigit():
            no_digits.append(i)
    result = ''.join(no_digits)
    return result


def remove_stopwords(words):
    """Removes stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


def stem_words(words):
    """Stems words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_words(words):
    """Lemmatizes verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def stem_and_lemmatize(words):
    """Creates and prints a list of stemmed and lemmatized verbs"""
    stems = stem_words(words)
    lemmas = lemmatize_words(words)
    print('Stemmed:\n', stems)
    print('\nLemmatized:\n', lemmas)
    return stems, lemmas


#####################################
## Replace Negations with Antonyms ##
#####################################

def replace(word, pos=None):
    """Creates a set of all antonyms for the word and if there is only one antonym, it returns it """
    antonyms = set()
    for syn in wordnet.synsets(word, pos=pos):
        for lemma in syn.lemmas():
            for antonym in lemma.antonyms():
                antonyms.add(antonym.name())
    if len(antonyms) >= 1:
        return antonyms.pop()
    else:
        return None


def detect_negations(text):
    """Counts how many negations are found and displays a list of them"""
    negation_counter = 0
    negations_found = []
    for word in text:
        if "'" in word:
            negations_found.append(word)
            negation_counter += 1
    return negation_counter, negations_found


def replace_negations(text):
    """Replaces "not" and the next word with the antonym """
    i, l = 0, len(text)
    words = []
    while i < l:
        word = text[i]
        if word == 'not' and i+1 < l:
            ant = replace(text[i+1])
            if ant:
                  words.append(ant)
                  i += 2
                  continue
        words.append(word)
        i += 1
    return words


##########################################
## Replace slang with their equivalents ##
##########################################

with open('slang.txt') as file:
    slang_map = dict(map(str.strip, line.partition('\t')[::2])
    for line in file if line.strip())


def detect_slang(text):
    """Input: string of text, Output: how many slang words and a list of found slangs """
    slangCounter = 0
    slangsFound = []
    tokens = nltk.word_tokenize(text)
    for word in tokens:
        if word in slang_words:
            slangsFound.append(word)
            slangCounter += 1
    return slangCounter, slangsFound


slang_words = sorted(slang_map, key=len, reverse=True) # longest first for regex
regex = re.compile(r"\b({})\b".format("|".join(map(re.escape, slang_words))))
replace_slang = partial(regex.sub, lambda m: slang_map[m.group(1)])


###############################################
## Replace contractions to their equivalents ##
###############################################

cList = {
  "ain't": "am not",
  "aren't": "are not",
  "can't": "cannot",
  "can't've": "cannot have",
  "'cause": "because",
  "could've": "could have",
  "couldn't": "could not",
  "couldn't've": "could not have",
  "didn't": "did not",
  "doesn't": "does not",
  "don't": "do not",
  "hadn't": "had not",
  "hadn't've": "had not have",
  "hasn't": "has not",
  "haven't": "have not",
  "he'd": "he would",
  "he'd've": "he would have",
  "he'll": "he will",
  "he'll've": "he will have",
  "he's": "he is",
  "how'd": "how did",
  "how'd'y": "how do you",
  "how'll": "how will",
  "how's": "how is",
  "i'd": "i would",
  "i'd've": "i would have",
  "i'll": "i will",
  "i'll've": "i will have",
  "i'm": "i am",
  "i've": "i have",
  "isn't": "is not",
  "it'd": "it had",
  "it'd've": "it would have",
  "it'll": "it will",
  "it'll've": "it will have",
  "it's": "it is",
  "let's": "let us",
  "ma'am": "madam",
  "mayn't": "may not",
  "might've": "might have",
  "mightn't": "might not",
  "mightn't've": "might not have",
  "must've": "must have",
  "mustn't": "must not",
  "mustn't've": "must not have",
  "needn't": "need not",
  "needn't've": "need not have",
  "o'clock": "of the clock",
  "oughtn't": "ought not",
  "oughtn't've": "ought not have",
  "shan't": "shall not",
  "sha'n't": "shall not",
  "shan't've": "shall not have",
  "she'd": "she would",
  "she'd've": "she would have",
  "she'll": "she will",
  "she'll've": "she will have",
  "she's": "she is",
  "should've": "should have",
  "shouldn't": "should not",
  "shouldn't've": "should not have",
  "so've": "so have",
  "so's": "so is",
  "that'd": "that would",
  "that'd've": "that would have",
  "that's": "that is",
  "there'd": "there had",
  "there'd've": "there would have",
  "there's": "there is",
  "they'd": "they would",
  "they'd've": "they would have",
  "they'll": "they will",
  "they'll've": "they will have",
  "they're": "they are",
  "they've": "they have",
  "to've": "to have",
  "wasn't": "was not",
  "we'd": "we had",
  "we'd've": "we would have",
  "we'll": "we will",
  "we'll've": "we will have",
  "we're": "we are",
  "we've": "we have",
  "weren't": "were not",
  "what'll": "what will",
  "what'll've": "what will have",
  "what're": "what are",
  "what's": "what is",
  "what've": "what have",
  "when's": "when is",
  "when've": "when have",
  "where'd": "where did",
  "where's": "where is",
  "where've": "where have",
  "who'll": "who will",
  "who'll've": "who will have",
  "who's": "who is",
  "who've": "who have",
  "why's": "why is",
  "why've": "why have",
  "will've": "will have",
  "won't": "will not",
  "won't've": "will not have",
  "would've": "would have",
  "wouldn't": "would not",
  "wouldn't've": "would not have",
  "y'all": "you all",
  "y'alls": "you alls",
  "y'all'd": "you all would",
  "y'all'd've": "you all would have",
  "y'all're": "you all are",
  "y'all've": "you all have",
  "you'd": "you had",
  "you'd've": "you would have",
  "you'll": "you you will",
  "you'll've": "you you will have",
  "you're": "you are",
  "you've": "you have"
}
c_re = re.compile('(%s)' % '|'.join(cList.keys()))


def count_contractions(text):
    """Counts how many contractions are there and displays a list of them"""
    contractions_counter = 0
    contractions_found = []
    for word in text:
        if "'" in word:
            contractions_found.append(word)
            contractions_counter += 1
    return contractions_counter, contractions_found


def expand_contractions(text, c_re=c_re):
    """Replaces contractions with their expansions"""
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)
