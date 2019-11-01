# Text preprocessing

There is a whole suite of text preparation methods that you may need to use, and the choice of methods really depends on your task. 

Text preprocessing is not directly transferable from task to task. Let’s take a very simple example, let’s say you are trying to discover commonly used words in a dataset. If your pre-processing step involves removing stop words because some other task used it, then you are probably going to miss out on some of the common words as you have already eliminated it. So really, it’s not a one-size-fits-all approach. 


# Data processing techniques

So how do we go about doing text preprocessing? Generally, there are 3 main components:
- Noise removal
- Tokenization
- Normalization

In a nutshell, **noise removal** cleans up the text, e.g., removes extra whitespaces. **Tokenization** is about splitting strings of text into smaller pieces, or “tokens”. Paragraphs can be tokenized into sentences and sentences can be tokenized into words. **Normalization** aims to put all text on a level playing field, e.g., converting all characters to lowercase. 


## Noise Removal 

**Noise removal** can be loosely defined as text-specific normalization tasks which often take place prior to tokenization. While the other 2 major steps of the preprocessing framework (tokenization and normalization) are less task-independent, noise removal is much more task-specific.

Sample noise removal tasks could include:
removing text file headers, footers
removing HTML, XML, etc. markup and metadata
extracting valuable data from other formats, such as JSON


### Remove HTML

If the data is web scraped, chances are it will contain some HTML tags. Since these tags are not useful for NLP tasks, it is better to remove them. 

```remove_html()``` strips away HTML markup.

```remove_between_square_brackets```  
Removes open and close double brackets and anything in between them.


### Contraction replacement

While not mandatory to do at this stage prior to tokenization (you'll find that this statement is the norm for the relatively flexible ordering of text data preprocessing tasks), **replacing contractions** with their expansions can be beneficial at this point, since our word tokenizer will split words like "didn't" into "did" and "n't." It's not impossible to remedy this tokenization at a later stage, but doing so prior makes it easier and more straightforward.

```count_contractions()``` counts how many contractions are there and displays a list of them.

```expand_contracions()``` replaces contractions to their equivalents.


### Deduplication:   

```remove_dupes()``` removes duplicate rows.


### Slang replacement:  

```count_slang()``` looks for any slang, if found displays a list of found slangs and total number of slangs in the text. 

```replace_slang()``` replaces slang words and abbreviations with their equivalents.


### Negation replacement:  

```count_negations()```  counts how many negations are found and displays a list of them. 

```replace_negations()```  replaces not and the following word with the antonym.


## Tokenization

Tokenization refers to dividing text into a sequence of words or sentences.  Further processing is generally performed after a piece of text has been appropriately tokenized. Tokenization is also referred to as text segmentation or lexical analysis. Sometimes segmentation is used to refer to the breakdown of a large chunk of text into pieces larger than words (e.g. paragraphs or sentences), while tokenization is reserved for the breakdown process which results in words.
This can be done using NTLK's ```word_tokenize()``` function. After tokenization, we are no longer working at a text level, but now at a word level.


## Normalization:  

Normalization generally refers to a series of related tasks meant to put all text on a level playing field: converting all text to the same case (upper or lower), removing punctuation, converting numbers to their word equivalents, and so on.
Normalization puts all words on equal footing, and allows processing to proceed uniformly.

Text normalization includes:
- converting all letters to lower or upper case
- converting numbers into words or removing numbers
- removing punctuations, accent marks and other diacritics
- removing white spaces
- removing stop words, sparse terms, and particular words


### Normalizing case

It is common to convert all words to one case.
This means that the vocabulary will shrink in size, but some distinctions are lost (e.g. “Apple” the company vs “apple” the fruit is a commonly used example).

```to_lowercase(tokens)```  converts all characters to lowercase from list of tokenized words.


### Removing puctuation

Punctuation doesn’t necessarily add any extra information while treating text data. Therefore removing all instances of puctuation helps reduce the size of the training data.  

```remove_punctuation(tokens)``` removes punctuation from a list of tokenized words.

```remove_non_ascii(words)``` removes non-ASCII characters from list of tokenized words


### Dealing with numbers

Remove numbers if they are not relevant to your analyses.

```remove_numbers()``` strips digits from a list of tokenized words

```replace_numbers(tokens)``` replaces all interger occurrences in list of tokenized words with textual representation.


### Dealing with stopwords

```remove_stopwords(tokens)``` removes stop words from a list of tokenized words.


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


References:  
[Cambridge University Press, Stemming and lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html);  
[Jiahao Weng, NLP Text Preprocessing] (https://towardsdatascience.com/nlp-text-preprocessing-a-practical-guide-and-template-d80874676e79);  
[Jason Brownlee, How to Clean Text for Machine Learning with Python](https://machinelearningmastery.com/clean-text-machine-learning-python/);  
[Kavita Ganesan, All you need to know about Text Preprocessing for Machine Learning & NLP](https://kavita-ganesan.com/text-preprocessing-tutorial/#.Xbw36ej7Q2x);  
[Matthew Mayo, Text Data Preprocessing: A Walkthrough in Python](https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html);  
[Matthew Mayo, A general Approach to Preprocessing Text Data](https://www.kdnuggets.com/2017/12/general-approach-preprocessing-text-data.html);  
