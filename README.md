# ICR-linguistics
Repository for various research files.

Working research question: 
In what ways has the use of metaphor in poetry changed over time, and how can these possible changes be modeled by a computer?

"Abstract":
The current goal of my project is to plot the use of metaphor in poetry using a combination of rule-based and statistical machine-learning models in order to analyze the differences in "metaphoricity" across various poetic eras. Unlike similar projects that focused on the use of computational linguistics in poetry as a means of interpretation, my project aims to use computer models to analyze the evolution of poetic style without regards to poetic understanding. By combining various methods of semantic extraction (e.g., parsing, tagging, etc.) with more advanced machine learning techniques like word embedding and cosine similarity, I hope to model the changes in poetic metaphor use across time.

(Brief) "Introduction":
In the words of Aurelie Herbelot (2015), poetry is not a typical focus of linguistic research because it "is expected to defy the accepted rules of ordinary language, and thus is not a particularly good example of the efficient medium we use to communicate in everyday life." However, this does not mean that poetry is a complete departure from everyday speech, since it is still widely read and understood across multiple cultures, locations, languages, and time periods. In addition, poetry, like everyday speech, differs across time and place and thus needs to be analyzed accordingly. Metaphor, too, is often overlooked in linguistic research due to the higher-level connections that must be made in order to understand the connection between two apparently unrelated things--and yet, we humans frequently use and understand metaphor in our use of language. As a result, it is important for metaphor, specifically poetic metaphor, to be understood by a computational model in the same way that ordinary language is understood. Additionally, it is important to understand not only the use of metaphor in poetry, but how that use has altered over time, and to investigate the possible shifts in metaphor use from the epics and sonnets of old to the contemporary, idiosyncratic poetry of today. The purpose of my research is to utilize pre-existing technology in order to better understand the evolution of metaphor in poetic style across time and culture.

"Background":
The broader topic of my project--computational linguistics--can essentially be defined as the use of computers to study and expand the field of linguistics. While linguistics is an incredibly broad field involving a variety of methods and branches, the field I am focusing on in my project is semantics, which is the study of meaning. Semantics itself also has a variety of varying sub-branches, views, and methods used to study it. A few methods I am using include tagging, which is the process of marking the words in a corpus with their corresponding part of speech; parsing, which enables one to gain a better understanding of a text by breaking it down into different syntactic parts and associations; and word embedding, which is the process of transforming the words that are more easily understood by humans into numerical vectors that are more easily understood by computers. The idea for my project is primarily based on previous models that attempted to identify metaphor not only through vectors and machine learning, but also through methods like visual representation, text annotation, and more (Shutova et al, Kesarwani*). My project is essentially a simplified version of previous related works, removing visual representation and manual corpus annotation in favor of a simpler approach.
*These citations are incomplete--just a temporary reminder for myself.

"Methodology":
1. Building and sorting the corpus

For now, I am including all poetry together as a single corpus, rather than sorting by period, region, genre, etc., although it should be noted that all of the poems in use were written in (or translated to) English. For now, the best corpus I can find is the Kaggle collection of Poetry Foundation poems, sorted by title, author, and theme and licensed under the GNU Affero General Public License 3.0. I chose this corpus over the Project Gutenberg corpus, among others, due to its organization, which separated individual poems where other corpora lumped them all together (presumably because machine learning models would not require the separation of poems while training). In addition, the title, poem, and theme are each separated by a quoted comma (","), which will be simple for a Python program to identify if necessary.

2. Extracting and isolating metaphors based on POS tag sequences and dependency parsers

I am using the approach taken by Neuman (2013) and Kesarwani (2018, p.70). rather than annotating poetry line by line in order to identify metaphor, I chose to use the various POS tag sequences described by Kesarwani to automatically extract the majority of metaphorical phrases and sentences from the corpus. This is an important step towards extracting all of the metaphors used in the corpus, and relies on simple, rule-based directions, making it a relatively fast and efficient process. Then, in line with Kesarwani (2018) and Shutova (2016), I use a dependency parser--in my case, SpaCy--in order to identify the various associations and connections (e.g., nsubj, dobj, etc.) within the tagged sentences, and remove the sentences that do not feature metaphors. As Kesarwani pointed out, however, POS tagging can sometimes result in incomprehensible word pairs; in the event of this happening, I plan to use the Berkeley Neural Parser (integrated in SpaCy) in order to identify the surrounding context. My choice to use SpaCy rather than the Stanford Parser and Dependency Parser chosen by Kesarwani is due to the fact that SpaCy is both open-source, an important aspect of the project, and pre-trained, significantly reducing the time and cost of this step. Additionally, SpaCy operates much faster than Stanford GloVe, which is my primary reason for choosing SpaCy. 

3. Create high-dimensional vectors using word embeddings

In order to calculate the vectors of the isolated metaphors, I plan to use fasttext to find word-level embeddings. Fasttext uses, like its alternative word2vec, a skip-gram model, but unlike word2vec or Stanford GloVe (which was used by both Kesarwani and Shutova), fasttext first breaks the words into n-grams before feeding them into the neural network, which resolves the problem faced by GloVe and word2vec in which words out of the model's vocabulary cannot be encoded. I plan to use a 100-dimensional vector representation, as that was the number of dimensions used by both Kesarwani and Shutova, and because another person who tried to find the optimal number of dimensions for word embeddings concluded that close to 100 dimensions (85, to be exact) was optimal (Kwan, 2023). At the moment, I plan to train for three epochs; not only is this the number used by Shutova, but it was also the number used by Google, and is large enough to provide accuracy without the risk of overfitting.

4. Rule-based metaphor detection?

Although I understand the purpose of this step, I'm unsure of how necessary it is. How much extra time would it add to my research (and how much would I gain from this step)?

5. Use a pre-trained statistical-based machine learning model and cosine similarity to further detect metaphor in the selected sentences

Before calculating the cosine similarity, I first needed to create a threshold at which a phrase is considered a metaphor; I plan to do this in a similar way to how Shutova (2016) did it in their research. I plan to use a small collection of phrases that have been manually annotated for whether they are metaphorical or literal, and then calculate the cosine similarity between the two parts of the metaphor (e.g., two nouns, a noun and a verb, etc.). By averaging those numbers, it is possible to create a threshold for what cosine value would classify a certain phrase as a metaphor, and thus discard the phrases that exceeded that threshold as likely being literal. For the manually annotated datasets, I am planning to use the dataset created by Mohammed et al (2016), in which verb-noun pairs were gathered from WordNet, a large database of English words maintained by Princeton University, and annotated for metaphoricity by annotators from a crowdsourcing platform. Only the tagged pairs that reached 70% or higher agreement across annotators were used in the final set. I also plan to use the Tsvetkov et al (2014) dataset of noun-adjective pairs . I chose both of these datasets because they each look at different word pairs (noun-adjective vs noun-verb), they include literal phrases in addition to metaphorical ones, and because they focus simply on annotating and identifying metaphors rather than interpreting them like other researchers (Zayed et al, 2020). 

6. Generating a plot
Finally, after using the various aforementioned methods to find the metaphors in the poetry corpus, I plan to generate a plot comparing the different numbers of metaphors found across different time periods (or whatever the final variables are). The X-axis will be a measure across time, presumably measured in decades; the Y-axis will be a measure of the number of metaphors present in the poems of that year within the corpus. I plan to use matplotlib in Python to create my plot; Seaborn was another option, but I opted for matplotlib since it works particularly well for basic visualizations like the one I will be making and is more compatible with the other libraries I am familiar with (Sial et al, 2021).

"Results":
...


Sources used* (alphabetized): Author's Name. Title of paper. Relevance (or lack thereof).

Feng, Yansong and Lapata, Mirella. Visual information in semantic representation. Relevant.
Herbelot, Aurelie. The semantics of poetry: a distributional reading. Relevant.
Hermann, Karl and Blunsom, Phil. Multilingual models for compositional distributed semantics. Fairly relevant but complicated.
Jones, Michael and Mewhort, Douglas. Representing word meaning and order information in a composite holographic lexicon. Relevant.
Kerarwari, Vaibhav. Automatic poetry classification using natural language processing. Very relevant.
Mohammed et al. Metaphor as a medium for emotion: An empirical study. Relevant.
Musaoglu et al. Generic tool for visualizing patterns in poetry. Semi-relevant.
Plamodon, Marc. Poetic waveforms, discrete fourier transform analysis of phonemic accumulations, and love in the garden of Tennyson's Maud. Not relevant.
Shutova et al. Black holes and white rabbits: Metaphor identification with visual features. Very relevant.
Sial et al. Comparative analysis of data visualization libraries matplotlib and seaborn in python. Relevant. 
Zayed et al. Figure me out: A gold standard dataset for metaphor interpretation. Not very relevant. 
Zou et al. Bilingual word embeddings for phrase-based machine translation. Not very relevant.

*I also used various articles and blog posts to quickly understand certain concepts, but most of them are not credible enough to cite and were not read in full.
