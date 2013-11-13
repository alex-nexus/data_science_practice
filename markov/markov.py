import random
import re

class Markov(object):
	def __init__(self, file_name='bible.txt'):
		self.cache = {}
		self.open_file = open(file_name, 'r')

		self.words = []
		for i in range(5):
			self.words.extend(self.file_to_words())
			self.word_size = len(self.words)
			print i, self.word_size
		self.database()
			
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		words = filter(lambda w: not re.match('\d+:\d+', w), words)
		return words
			
	def triples(self):
		if len(self.words) < 3:
			return		
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, size=30):
		seed = random.randint(0, self.word_size-3)
		seed_word, next_word = self.words[seed], self.words[seed+1]
		seed_word, next_word = 'Jesus', 'Christ'

		w1, w2 = seed_word, next_word
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)
			
			
m = Markov()
for i in range(5):
	print m.generate_markov_text().title()