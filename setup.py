__author__ = 'TonySun'
# this file setup up some common path of external files used in this project

# path of the corpus file
corpus_file_path = "corpus/Flickr8k.lemma.token.txt"

# path of language model file used
lmodel_file_path = "lmodel/GoogleNews-vectors-negative300.bin"

# path of stanford corenlp python wrapper
corenlp_wrapper_path = "corenlp_python/stanford-corenlp-full-2015-04-20"

# terms which have these four POS (part-of-speech) tags are retained
# namely, Noun, Adjective, Adverb, Verb
# pos tags following the Penn Treebank Project
retained_pos_tags = ['NN', 'JJ', 'RB', 'VB']

# retain 11 types of word dependencies (defined in Stanford corenlp project)
# acomp: adjectival complement
# advmod: adverb modifier
# agent: complement of a passive verb
# amod: adjectival modifier
# appos: appositional modifier
# dobj: direct object
# iobj: indirect object
# nsubj: nominal subject
# nsubjpass: passive nominal subject
# vmod: reduced non-finite verbal modifier
# prt: phrasal verb particle e.g. shut down

retained_depend_types = ['acomp', 'advmod', 'agent', 'amod', 'appos', 'dobj',
                        'iobj', 'nsubj', 'nsubjpass', 'vmod', 'prt']

