# Moment, Meaning, and Metaphor: A computational comparison of metaphor use and semantic evolution between modern and Renaissance English poetry across the themes of love, nature, and mythology

## Installing and Implementing my Code

1. Setting up the repository
In your terminal, type or copy-paste:
```
git clone https://github.com/paigetomkins/ICR-PoeticMetaphorAnalysis.git
```
and press Enter. You should now have a local clone of this repository.



## Working research question: 
Between Old English and modern poetry, in what ways has the use of metaphor in poetry changed over time, and how can these changes be quantified and modeled by a computer program?

## "Abstract":
The current goal of my project is to plot the use of metaphor in poetry using a combination of rule-based and statistical machine-learning models in order to analyze the differences in "metaphoricity" between Old English and modern poetry. Unlike similar projects that focused on the use of computational linguistics in poetry as a means of interpretation, my project aims to use computer models to analyze the evolution of poetic style without regards to poetic understanding. By combining various methods of semantic extraction (e.g., parsing, tagging, etc.) with more advanced machine learning techniques like word embedding and cosine similarity, I hope to model the changes in poetic metaphor use across time.

## "Introduction":
In the words of Aurelie Herbelot (2015), poetry is not a typical focus of linguistic research because it "is expected to defy the accepted rules of ordinary language, and thus is not a particularly good example of the efficient medium we use to communicate in everyday life." However, this does not mean that poetry is a complete departure from everyday speech, since it is still widely read and understood across multiple cultures, locations, languages, and time periods. In addition, poetry, like everyday speech, differs across time and place and thus needs to be analyzed accordingly. Metaphor, too, is often overlooked in linguistic research due to the higher-level connections that must be made in order to understand the connection between two apparently unrelated things--and yet, we humans frequently use and understand metaphor in our use of language. As a result, it is important for metaphor, specifically poetic metaphor, to be understood by a computational model in the same way that ordinary language is understood. Additionally, it is important to understand not only the use of metaphor in poetry, but how that use has altered over time, and to investigate the possible shifts in metaphor use from the epics and sonnets of old to the contemporary, idiosyncratic poetry of today. The purpose of my research is to utilize pre-existing technology in order to better understand the evolution of metaphor in poetic style across time and culture.

## "Background":
The broader topic of my project--computational linguistics--can essentially be defined as the use of computers to study and expand the field of linguistics. While linguistics is an incredibly broad field involving a variety of methods and branches, the field I chose to focus on is semantics, which is the study of meaning in language. Semantics itself also has a variety of varying sub-branches, views, and methods of study. A few common methods of analysis used in semantics include: 

Tagging: The process of marking the words in a corpus with their corresponding part of speech. Tagging was first used on a serious corpus with the Brown Corpus, the first major structured corpus of English literature, first developed in the 1960s by Henry Kucera and W. Nelson Francis at Brown University (cn). Since then, multiple different kinds of supervised and unsupervised tagging models have been developed. The most common type of POS tagging today is likely the Penn tag set developed in the Penn-Treebank project, and is the tagging system used by the YCOEP corpus. 

Parsing: A method of semantic analysis which enables one to gain a better understanding of a text by breaking it down into different syntactic parts and associations. Parsing is a particularly difficult task for computers to perform due to the multitude of ambiguities in human language, yet an understanding of syntax in language is essential to create meaning (for instance, the sentence "The bird is in the tree" is very different from "The tree is in the bird," despite identical vocabulary usage). Additionally, different researchers choose to train their models in different ways, with grammar, training data, and statistical models altering from person to person. Most models, despite advancements in machine learning, still require some form of manual parsing before they are able to perform or understand parsing themselves, increasing the resources necessary for parsing. Thankfully, there are a number of open-source software programs that can perform complex dependency parsing quickly, allowing me to easily and efficiently parse my own dataset without much difficulty.

Word embedding, which is the process of transforming the words that are more easily understood by humans into numerical vectors that are more easily understood by computers based on the context surrounding the word. The idea behind word embedding, that "a word is characterized by the company it keeps," was first suggested by the linguist John Firth in his 1957 article "A Synopsis of Linguistic Theory, 1930-55." 

The idea for my project is primarily based on previous models that attempted to identify metaphor not only through vectors and machine learning, but also through methods like visual representation, text annotation, and more (Shutova et al, 2016; Kesarwani, 2018). My project is essentially a simplified version of previous related works, removing visual representation and manual corpus annotation in favor of a simpler approach.


## "Methodology":
### 1. Dataset Selection

For my dataset, I have selected the York-Helsinki Parsed Corpus of Old English Poetry (YCOEP), downloaded from the Oxford Text Archive (University of Oxford, 2001). The dataset is a collection of Old English poetry between the years 730 and 1710, taken from the Old English section of the Helsinki corpus of English texts and contains 71,490 words from "a range of dates and authors" (University of Oxford, 2001). The corpus is syntactically parsed and morphologically annotated, with an overall size of roughly 2.5 megabytes. The dataset is downloaded as a collection of fourteen files, each containing text data in the form of a digital bitstream. It is licensed under the Oxford Text Archive license, an open access license requiring citation and non-commerical use. Although thorough information was offered about creation dates and similar organizational details, none was offered regarding the exact number of poems or authors present in the corpus. I chose this corpus over similar Kaggle and Project Gutenberg corpora, among others, due to its more narrow scope of time and language, and because it had already been syntactically and morphologically annotated, thus reducing the time and cost of my own research. 
I have also selected the Kaggle open-source dataset "Poems from poetryfoundation.org," which is a collection of poems from Poetry Foundation assembled by the user ultra-jack and licensed under the CC0 Public Domain license, making it free for anyone to use. The collection is sorted based on general time period ("Renaissance" or "Modern"), author, and theme ("love," "nature," or "mythology and folklore"). For the purposes of my research, I am only analyzing the poems that are classified as "Modern," including all authors and themes. There are a total of 509 poems from 462 authors, with a relatively even distribution of time period. Since the poems were collected from Poetry Foundation, it can be assumed that they also cover a wide range of regions and possibly languages, though all of the poems are offered in English and no information is given regarding language or region. Although the theme of the poetry is skewed, with "Love" accounting for 57% of poems, this is unlikely to have a severe effect on my results as I am analyzing the use of metaphor across time, irrespective of theme, and because the skew appears to occur across both eras of poetry, allowing for an even distribution of theme between them. The dataset contains no linguistic annotation and is downloaded in the form of a single .csv file containing all of the poems. I have selected this dataset over similar Kaggle or Project Gutenberg corpora due to its organization of time period, simple format, and wide authorship distribution, all of which enable me to easily sort my data and have greater faith in my results.(Possible graph of authorship distribution to be added)

### 2. Importing and Processing the corpus

When downloading the Oxford corpus, it should be noted that although the files were originally given the extension .psd, none of them are Photoshop documents and as such could not be opened by image editing software; rather, the file extensions had to be manually changed to that of a text file. I selected .txt as my file extension of choice since the files used ASCII text, although .mv and similar text formats also enabled the files to open. For now, I am including all poetry together as a single corpus, rather than sorting by period, region, genre, etc., although it should be noted that all of the poems in use were written in English or Old English. 
With regards to the Kaggle dataset, the download was fast and uneventful. Due to the dataset being well-labeled yet lumped into a single file, I plan to use a simple text splitting function in Python to separate the poems based on age in order to keep track of them.

### 3. Extracting and isolating metaphors based on POS tag sequences and dependency parsers

I am using the approach taken by Neuman (2013) and Kesarwani (2018, p.70). Rather than annotating poetry line by line in order to identify metaphor, I chose to use the various POS tag sequences described by Kesarwani to automatically extract the majority of metaphorical phrases and sentences from the corpus. This is an important step towards extracting all of the metaphors used in the corpus, and relies on simple, rule-based directions, making it a relatively fast and efficient process. Then, in line with Kesarwani (2018) and Shutova (2016), I use a dependency parser--in my case, SpaCy--in order to identify the various associations and connections (e.g., nsubj, dobj, etc.) within the tagged sentences, and remove the sentences that do not feature metaphors. As Kesarwani pointed out, however, POS tagging can sometimes result in incomprehensible word pairs; in the event of this happening, I plan to use the Berkeley Neural Parser (integrated in SpaCy) in order to identify the surrounding context. My choice to use SpaCy rather than the Stanford Parser and Dependency Parser chosen by Kesarwani is due to the fact that SpaCy is both open-source, an important aspect of the project, and pre-trained, significantly reducing the time and cost of this step. Additionally, SpaCy is known to operate much faster than Stanford GloVe, which is my primary reason for choosing it. 

### 4. Create high-dimensional vectors using word embeddings

In order to calculate the vectors of the isolated metaphors, I plan to use gensim to find word-level embeddings. Although gensim was originally designed for topic modeling, it is good at training word vectors and adding them into SpaCy, which will allow me to take advantage of both libraries to maximize the speed and accuracy of the machine-learning section. I initially planned to use fasttext, but after memory problems and other malfunctions, gensim became a better choice. (more to be added later)
Fasttext uses, like its alternative word2vec, a skip-gram model, but unlike word2vec or Stanford GloVe (which was used by both Kesarwani and Shutova), fasttext first breaks the words into n-grams before feeding them into the neural network, which resolves the problem faced by GloVe and word2vec in which words out of the model's vocabulary cannot be encoded. I plan to use a 100-dimensional vector representation, as that was the number of dimensions used by both Kesarwani and Shutova, and because another person who tried to find the optimal number of dimensions for word embeddings concluded that close to 100 dimensions (85, to be exact) was optimal (Kwan, 2023). At the moment, I plan to train for three epochs; not only is this the number used by Shutova, but it was also the number used by Google, and is large enough to provide accuracy without the risk of overfitting or costing me too much time.

### 5. Rule-based metaphor detection?

Although I understand the purpose of this step, the implementation of it relies on my time management, and whether I am able to complete the previous steps quickly.

### 6. Use a pre-trained statistical-based machine learning model and cosine similarity to further detect metaphor in the selected sentences

Before calculating the cosine similarity, I first need to create a threshold at which a phrase is considered a metaphor; I plan to do this in a similar way to how Shutova (2016) did it in their research. I plan to use a small collection of phrases that have been manually annotated for whether they are metaphorical or literal, and then calculate the cosine similarity between the two parts of the metaphor (e.g., two nouns, a noun and a verb, etc.). By averaging those numbers, it is possible to create a threshold for what cosine value would classify a certain phrase as a metaphor, and thus discard the phrases that exceeded that threshold as likely being literal. For the manually annotated datasets, I am planning to use the dataset created by Mohammed et al (2016), in which verb-noun pairs were gathered from WordNet, a large database of English words maintained by Princeton University, and annotated for metaphoricity by annotators from a crowdsourcing platform. Only the tagged pairs that reached 70% or higher agreement across annotators were used in the final set. I also plan to use the Tsvetkov et al (2014) dataset of noun-adjective pairs . I chose both of these datasets because they each look at different word pairs (noun-adjective vs noun-verb), they include literal phrases in addition to metaphorical ones, and because they focus simply on annotating and identifying metaphors rather than interpreting them like other researchers (Zayed et al, 2020). 

### 7. Generating a plot

Finally, after using the various aforementioned methods to find the metaphors in the poetry corpus, I plan to generate a plot comparing the different numbers of metaphors found across different time periods (or whatever the final variables are). The X-axis will be a measure across time, presumably measured in decades; the Y-axis will be a measure of the number of metaphors present in the poems of that year within the corpus. I plan to use matplotlib in Python to create my plot; Seaborn was another option, but I opted for matplotlib since it works particularly well for basic visualizations like the one I will be making and is more compatible with the other libraries I am familiar with (Sial et al, 2021).

## Licensing and Usage:
I have used exclusively open-source software and materials to conduct my research; as such, all of my code, in addition to my paper and other associated files are open for public use, replication, and modification.

## "Results":
...


## Sources used* (alphabetized): 
### Author's Name. Title of paper. Relevance (or lack thereof).

Feng, Y. and Lapata, M. (2010). Visual information in semantic representation. Relevant.

Herbelot, A. (2014). The semantics of poetry: a distributional reading. Relevant.

Hermann, K. and Blunsom, P. (2014). Multilingual models for compositional distributed semantics. Fairly relevant but complicated.

Jones, M. and Mewhort, D. (2007). Representing word meaning and order information in a composite holographic lexicon. Relevant.

Kerarwari, V. (2018). Automatic poetry classification using natural language processing. Very relevant.

Mohammed et al (2016). Metaphor as a medium for emotion: An empirical study. Relevant.

Musaoglu et al (2017). Generic tool for visualizing patterns in poetry. Semi-relevant.

Plamodon, M. (2009). Poetic waveforms, discrete fourier transform analysis of phonemic accumulations, and love in the garden of Tennyson's Maud. Not relevant.

Shutova et al (2016). Black holes and white rabbits: Metaphor identification with visual features. Very relevant.

Sial et al (2021). Comparative analysis of data visualization libraries matplotlib and seaborn in python. Relevant. 

Zayed et al (2020). Figure me out: A gold standard dataset for metaphor interpretation. Not very relevant.

Zou et al (2013). Bilingual word embeddings for phrase-based machine translation. Not very relevant.based on the context surrounding the word

*I also used various articles and blog posts to quickly understand certain concepts, but most of them are not credible enough to cite and were not read in full.
