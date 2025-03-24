import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Hello, this is a pull request example."
tokens = word_tokenize(text)

print("Tokens:", tokens)