# Text preprocessing

There is a whole suite of text preparation methods that you may need to use, and the choice of methods really depends on your task. 

Let’s take a very simple example, let’s say you are trying to discover commonly used words in a dataset. If your pre-processing step involves removing stop words because some other task used it, then you are probably going to miss out on some of the common words as you have already eliminated it. So really, it’s not a one-size-fits-all approach. 


# Data processing techniques

Generally, there are 3 main components to go about doing text preprocessing:
- Tokenization
- Noise removal
- Normalization

In a nutshell, **tokenization** is about splitting strings of text into smaller pieces, or “tokens”. Paragraphs can be tokenized into sentences and sentences can be tokenized into words. **Noise removal** cleans up the text, e.g., removes extra whitespaces. **Normalization** aims to put all text on a level playing field, e.g., converting all characters to lowercase. 


## Tokenization

Tokenization refers to dividing text into a sequence of words or sentences.  Further processing is generally performed after a piece of text has been appropriately tokenized. Tokenization is also referred to as text segmentation or lexical analysis. Sometimes segmentation is used to refer to the breakdown of a large chunk of text into pieces larger than words (e.g. paragraphs or sentences), while tokenization is reserved for the breakdown process which results in words.
This can be done using NTLK's ```word_tokenize()``` function. After tokenization, we are no longer working at a text level, but now at a word level.


## Noise Removal 

Noise removal is about removing characters digits and pieces of text  that can interfere with your text analysis. Noise removal is one of the most essential text preprocessing steps. It is also highly domain dependent. For example, in Tweets, noise could be all special characters except hashtags as it signifies concepts that can characterize a Tweet. 

Noise removal is one of the first things you should be looking into when it comes to Text Mining and NLP. There are various ways to remove noise. This includes punctuation removal, special character removal, numbers removal, html formatting removal, domain specific keyword removal (e.g. ‘RT’ for retweet), source code removal, header removal and more. It all depends on which domain you are working in and what entails noise for your task.


### Removing HTML

If the data is web scraped, chances are it will contain some HTML tags. Since these tags are not useful for NLP tasks, it is better to remove them. 

```remove_html()``` strips away HTML markup.

```remove_between_square_brackets()```  removes open and close double brackets and anything in between them.


### Deduplication

For a model to have good test accuracy, it must be fitted with data having high variance. Providing the model similar data might give a high training accuracy but might not work properly on future data. Hence it is an usual assumption that the data given is independent and identically distributed. 

```remove_dupes()``` detects and removes exactly identical duplicate rows.


### Replacing Accented characters

Words with accent marks like “latté” and “café” can be converted and standardized to just “latte” and “cafe”, else the NLP model will treat “latté” and “latte” as different words even though they are referring to same thing. 

```convert_accented_chars()``` converts accented characters into standard text.



### Removing puctuation

Punctuation doesn’t necessarily add any extra information while treating text data. Therefore removing all instances of puctuation helps reduce the size of the training data.  

```remove_punctuation()``` removes punctuation from a list of tokenized words.

```remove_non_ascii()``` removes non-ASCII characters from list of tokenized words


## Normalization:  

Normalization generally refers to a series of related tasks meant to put all text on a level playing field: converting all text to the same case (upper or lower), removing punctuation, converting numbers to their word equivalents, and so on.
Normalization puts all words on equal footing, and allows processing to proceed uniformly.

Text normalization includes:
- converting all letters to lower or upper case
- converting numbers into words or removing them
- removing stop words, sparse terms, and particular words


### Normalizing case

It is common to convert all words to one case.
This means that the vocabulary will shrink in size, but some distinctions are lost (e.g. “Apple” the company vs “apple” the fruit is a commonly used example).

```to_lowercase()```  converts all characters to lowercase from list of tokenized words.


### Dealing with numbers

Removing numbers may make sense for sentiment analysis since numbers contain no information about sentiments. However, if the task is to extract the number of tickets ordered in a message to our chatbot, we will definitely not want to remove numbers.

```remove_numbers()``` strips digits from a list of tokenized words

```replace_numbers()``` replaces all interger occurrences in list of tokenized words with textual representation.


### Contraction replacement

While not mandatory to do at this stage prior to tokenization (you'll find that this statement is the norm for the relatively flexible ordering of text data preprocessing tasks), **replacing contractions** with their expansions can be beneficial at this point, since our word tokenizer will split words like "didn't" into "did" and "n't." It's not impossible to remedy this tokenization at a later stage, but doing so prior makes it easier and more straightforward.

```count_contractions()``` counts how many contractions are there and displays a list of them.

```expand_contracions()``` replaces contractions to their equivalents.


### Slang replacement

One of the problems for nlp is shortened words and slang. For a task such as sentiment analysis, identifying slang and replacing it to the full sentence with attributed meaning can be an extraordinary advantage to accurately discovering sentiment hidden in tweets and customer reviews. 

```detect_slang()``` looks for any slang, if found displays a list of found slangs and total number of slangs in the text. 

```replace_slang()``` replaces slang words and abbreviations with their equivalents.


### Negation replacement

The negation words (not, nor, never) are considered to be stopwords in NLTK, spacy and sklearn, but we should pay different attention based on the NLP task. If your NLP task is context-relevant, for example, sentiment analysis, negation words should be kept as they bring crucial importance.

```detect_negations()```  counts how many negations are found and displays a list of them. 

```replace_negations()```  replaces not and the following word with the antonym.


### Dealing with stopwords

Stopwords are very common words. Words like “we” and “are” probably do not help in NLP tasks such as sentiment analysis or text classifications. Hence, stopwords are removed to save computing time and efforts in processing large volumes of text.

```remove_stopwords()``` removes stop words from a list of tokenized words.


### Stemming and lemmatization

For grammatical reasons, documents are going to use different forms of a word, such as organize, organizes, and organizing. Additionally, there are families of derivationally related words with similar meanings, such as democracy, democratic, and democratization. 

The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form.

**Stemming** usually refers to a process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes or suffices, like “ing”, “ly”, “s”, etc. For example “fishing,” “fished,” “fisher” all reduce to the stem “fish.”

Some applications, like document classification, may benefit from stemming in order to both reduce the vocabulary and to focus on the sense or sentiment of a document rather than deeper meaning.

```stem_words()``` stems words in list of tokenized words.

**Lemmatization** usually refers to doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma. In other words lemmatization converts the word into its root word, rather than just stripping the suffices. 

If confronted with the token saw, stemming might return just s, whereas lemmatization would attempt to return either see or saw depending on whether the use of the token was as a verb or a noun.

```lemmatize_words()``` lemmatizes verbs in list of tokenized words.

```stem_and_lemmatize()``` creates and prints a list of stemmed and lemmatized 
verbs.


## Do you need all the text preprocessing types?

Not really, but you do have to do some of it for sure if you want good, consistent results. To give you an idea of what the bare minimum should be, [Kavita Ganesan](https://kavita-ganesan.com/text-preprocessing-tutorial/#.XbxFguj7Q2w) broken it down to Must Do, Should Do and Task Dependent. Everything that falls under task dependent can be quantitatively or qualitatively tested before deciding you actually need it. Remember, less is more and you want to keep your approach as elegant as possible. The more overhead you add, the more layers you will have to peel back when you run into issues.

Must Do:
Noise removal

Lowercasing (can be task dependent in some cases)
Should Do:
Simple normalization – (e.g. standardize near identical words)
Task Dependent:
Advanced normalization (e.g. addressing out-of-vocabulary words)
Stop-word removal
Stemming / lemmatization
Text enrichment / augmentation
So, for any task, the minimum you should do is try to lowercase your text and remove noise. What entails noise depends on your domain (see section on Noise Removal). You can also do some basic normalization steps for more consistency and then systematically add other layers as you see fit.

General Rule of Thumb
Not all tasks need the same level of preprocessing. For some tasks, you can get away with the minimum. However, for others,  the dataset is so noisy that, if you don’t preprocess enough, it’s going to be garbage-in-garbage-out.


References:  
[Cambridge University Press, Stemming and lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) ;  
[Jiahao Weng, NLP Text Preprocessing: A Practical Guide and Template](https://towardsdatascience.com/nlp-text-preprocessing-a-practical-guide-and-template-d80874676e79) ;  
[Jason Brownlee, How to Clean Text for Machine Learning with Python](https://machinelearningmastery.com/clean-text-machine-learning-python/) ;  
[Kavita Ganesan, All you need to know about Text Preprocessing for Machine Learning & NLP](https://kavita-ganesan.com/text-preprocessing-tutorial/#.Xbw36ej7Q2x) ;  
[Matthew Mayo, Text Data Preprocessing: A Walkthrough in Python](https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html) ;  
[Matthew Mayo, A general Approach to Preprocessing Text Data](https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html) ;  
