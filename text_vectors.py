__author__ = 'TonySun'
# This file is used to test the text vectors using Google's
# Word2Vec and Doc2Vec tools in Gensim toolkit
# till now the text file used is from annotation of Flickr 8k annotation dataset
# Each image have 5 annotations
# All the annotations are manually done and each one appears as a single sentence
import re
import gensim
import numpy as np
import utilites
import setup


# time to do some NLP stuff. We need a function to do this
def annotation_to_wordlists(annotations, remove_stop_words = False):
    """
    Function to convert a whole sentence to a word list
    Common NLP techniques are applied, such as to lower case, tokenization
    Returns a words lists, each list contains a tokenized sentence
    :param annotations: raw sentences extracted from corpus file
    :param remove_stop_words: whether stop words should be removed
    :return: list of sentences, each sentence is a list contains split words
    """
    sentences = [sentence.replace('.', '').strip().decode("utf8").lower().split(" ") for
                 sentence in annotations]
    return sentences



def extractVecs(model):
    """
    :param model: a language model generated using Word2Vec
    :return: a dict contains pairs of term names and their associated feature vectors
    """
    print ("Extracting word vectors...")
    feature_vecs = []
    # Index2word is a list that contains the names of the words in
    for word in model.index2word:
        feature_vecs.append(model[word]) # now we extract all word vectors from the model

    # build a dictionary to use term name as index
    term_dict = dict(zip(model.index2word, np.array(feature_vecs)))
    print ("Done.")
    return term_dict


# return text vectors calculated using Word2Vec by gensim
def getTextVectors():
    """
    open the annotation text file and read content
    build word vectors using Word2Vec and then extract
    the term/vector pairs into a dictionary
    :return: the ultimate word vectors
    """
    raw_text_file = open(utilites.getAbsPath(setup.corpus_file_path))
    raw_text = raw_text_file.readlines()
    print("Corpus file " + raw_text_file.name + " was loaded.")
    # use re to split the raw text string and replace the original text
    # After this all the sentence are split into such format:
    # [0]filename, [1]order of annotation, [2]annotation text
    raw_text = [re.split('\t|#', singleLine.replace('\n', '')) for singleLine in raw_text]

    # now we only need the annotations
    annotations = [line[2] for line in raw_text]

    # Prepare the sentences
    sentences = annotation_to_wordlists(annotations)

    # Set values for Word2Vec
    num_features = 300  # Use a 300-dimension vector to represent a word
    min_word_count = 5  # Word appears less than 5 times will be ignored
    num_workers = 4     # Number of threads to run in parallel
    context = 5        # Sample 5 words as input for each iteration

    # initialize a model using parameters above
    word_model = gensim.models.Word2Vec(workers=num_workers,
                               size=num_features, min_count=min_word_count, window=context)

    word_model.build_vocab(sentences) # build vocabulary on split sentenced
    print("Language model established.")
    print("Loading pre-trained language model...")
    # initialize the network weights using pre-trained model
    word_model.intersect_word2vec_format(utilites.getAbsPath(setup.lmodel_file_path), binary=True)
    print("Loaded weights from pre-trained Google News language model.")
    print("Training models...")
    # train the model to get word vectors
    word_model.train(sentences)
    print("Training completed.")

    return extractVecs(word_model)




	

