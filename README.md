## Text preprocessing

There is a whole suite of text preparation methods that you may need to use, and the choice of methods really depends on your task. 

Text preprocessing is not directly transferable from task to task. Let’s take a very simple example, let’s say you are trying to discover commonly used words in a dataset. If your pre-processing step involves removing stop words because some other task used it, then you are probably going to miss out on some of the common words as you have already eliminated it. So really, it’s not a one-size-fits-all approach. 


## Data processing techniques

### Noise Removal 

Let's loosely define **noise removal** as text-specific normalization tasks which often take place prior to tokenization. While the other 2 major steps of the preprocessing framework (tokenization and normalization) are less task-independent, noise removal is much more task-specific.

Sample noise removal tasks could include:
removing text file headers, footers
removing HTML, XML, etc. markup and metadata
extracting valuable data from other formats, such as JSON

```remove_html()```  
Strips away HTML markup.

```remove_between_square_brackets```  
Removes open and close double brackets and anything in between them.

#### Contraction replacement

While not mandatory to do at this stage prior to tokenization (you'll find that this statement is the norm for the relatively flexible ordering of text data preprocessing tasks), **replacing contractions** with their expansions can be beneficial at this point, since our word tokenizer will split words like "didn't" into "did" and "n't." It's not impossible to remedy this tokenization at a later stage, but doing so prior makes it easier and more straightforward.

```count_contractions()``` counts how many contractions are there and displays a list of them.

```expand_contracions()``` replaces contractions to their equivalents.

#### Deduplication:   

```remove_dupes()```  
Removes duplicate rows.

#### Slang replacement:  

```count_slang()```  
Looks for any slang, if found displays a list of found slangs and total number of slangs in the text. 

```replace_slang()```  
Replaces slang words and abbreviations with their equivalents.

#### Negation replacement:  

```count_negations()```  
Counts how many negations are found and displays a list of them. 

```replace_negations()```  
Replaces not and the following word with the antonym.


### Normalization:  

Normalization puts all words on equal footing, and allows processing to proceed uniformly.

Tokenization refers to dividing the text into a sequence of words or sentences. 

#### Normalizing case
It is common to convert all words to one case.
This means that the vocabulary will shrink in size, but some distinctions are lost (e.g. “Apple” the company vs “apple” the fruit is a commonly used example).

```to_lowercase(tokens)```  
Converts all characters to lowercase from list of tokenized words.

#### Removing puctuation
Punctuation doesn’t necessarily add any extra information while treating text data. Therefore removing all instances of puctuation helps reduce the size of the training data.  

```remove_punctuation(tokens)```  
Removes punctuation from list of tokenized words.



```replace_numbers(tokens)```  
Replaces all interger occurrences in list of tokenized words with textual representation.

```remove_stopwords(tokens)```  
Removes stop words from a list of tokenized words.

#### Stemming

Stemming refers to the process of reducing each word to its root or base, or simply put, the removal of suffices, like “ing”, “ly”, “s”, etc. For example “fishing,” “fished,” “fisher” all reduce to the stem “fish.”

Some applications, like document classification, may benefit from stemming in order to both reduce the vocabulary and to focus on the sense or sentiment of a document rather than deeper meaning.

```stem_words()```  stems words in list of tokenized words.

#### Lemmatization

Lemmatization converts the word into its root word, rather than just stripping the suffices. It makes use of the vocabulary and does a morphological analysis to obtain the root word. 

```lemmatize_words()``` lemmatizes verbs in list of tokenized words.

```stem_and_lemmatize()```  
Creates and prints a list of stemmed and lemmatized verbs.

