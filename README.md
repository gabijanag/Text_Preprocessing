#### What is text preprocessing?
To preprocess your text simply means to bring your text into a form that is predictable and analyzable for your task. A task here is a combination of approach and domain. For example, extracting top keywords with tfidf (approach) from Tweets (domain) is an example of a Task.
One task’s ideal preprocessing, can become another task’s worst nightmare. So take note, text preprocessing is not directly transferable from task to task. Let’s take a very simple example, let’s say you are trying to discover commonly used words in a news dataset. If your pre-processing step involves removing stop words because some other task used it, then you are probably going to miss out on some of the common words as you have ALREADY eliminated it. So really, it’s not a one-size-fits-all approach.




#### Data processing techniques

* Noise Removal:  

Sample noise removal tasks could include:
removing text file headers, footers
removing HTML, XML, etc. markup and metadata
extracting valuable data from other formats, such as JSON

```remove_html()```  
Strips away HTML markup.

```remove_between_square_brackets```  
Removes open and close double brackets and anything in between them.

* Deduplication:  

```remove_dupes()```  
Removes duplicate rows.


* Normalization:  
Normalization puts all words on equal footing, and allows processing to proceed uniformly.

```to_lowercase()```  
Converts all characters to lowercase from list of tokenized words.

```remove_punctuation()```  
Removes punctuation from list of tokenized words.

```replace_numbers()```  
Replaces all interger occurrences in list of tokenized words with textual representation.

```remove_stopwords()```  
Removes stop words from list of tokenized words.

```stem_words()```  
Stems words in list of tokenized words.


* Contraction replacement:  

```expand_contracions()```  
Replaces contractions to their equivalents

* Slang replacement:  
```count_slang()```  
Looks for any slang, if found displays a list of found slangs and total number of slangs in the text. 

```replace_slang()```  
Replaces slang words and abbreviations with their equivalents

* Negation replacement:  

```replace_negations()```  
Replaces not and the following word with the antonym.

* Remove stopwords;
* Stemmimg. Reduce inflectional forms to a common base form;
* Tokenization.
* Remove punctuation and numbers;
* Remove all the single characters;
* Replace multiple spaces with a single space;
