import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The boy plays cricket. The girl reads a book."

# 1. Sentence Segmentation
sentences = nltk.sent_tokenize(text)
print("Sentences:", sentences)

# 2. Word Tokenization
words = nltk.word_tokenize(sentences[0])
print("Words:", words)

# 3. POS Tagging
tags = nltk.pos_tag(words)
print("POS Tags:", tags)

# 4. Syntactic Parsing
grammar = r"""
NP: {<DT>?<NN.*>+}
VP: {<VB.*><NP>?}
"""

parser = nltk.RegexpParser(grammar)
tree = parser.parse(tags)

print("Parse Tree:")
print(tree)
