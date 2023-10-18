import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """As we journey deeper into space, it is essential to remember that our planet, the Earth,
 is a unique and precious oasis in the vast cosmos.
 Space exploration not only expands our understanding of the universe but also reminds us of the fragility of our own home.
 The insights we gain from space exploration can inform our efforts to protect and preserve the Earth for future generations.

In conclusion, space exploration is an endeavor that unites humanity in the pursuit of knowledge,
 adventure, and the quest to reach the stars. From the early days of the space race to the collaborative
   efforts of the International Space Station and the pioneering spirit of private space companies,
 our journey into space continues to inspire and push the boundaries of what is possible.
 The universe is vast, and our potential is limitless; it's a journey that promises to be as breathtaking 
 as the stars themselves."""

stopwords = list(STOP_WORDS)
#print(stopwords)

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
#print(doc)

tokens = [token.text for token in doc]
#print(tokens)

word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text] = 1
        else:
            word_freq[word.text] +=1

#print(word_freq)

max_freq = max(word_freq.values())
print(max_freq)

