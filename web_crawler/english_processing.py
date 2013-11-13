from pattern.en import referenced, article
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme, tenses, PAST, PL
from pattern.en import quantify
from pattern.en import ngrams
from pattern.en import parse, tag, pprint
from pattern.en import sentiment, polarity, subjectivity, modality
from pattern.en import Sentence

#Indefinite article
print article('university')
print article('hour')

print referenced('university')
print referenced('hour')


#singularity
print pluralize('child')
print singularize('wolves')

#
print 
print lexeme('run')
print lemma('running')
print conjugate('purred', '3sg')
print PAST in tenses('purred') # 'p' in tenses() also works.
print (PAST, 1, PL) in tenses('purred') 

print 'Quantification'

print quantify(['goose', 'goose', 'duck', 'chicken', 'chicken', 'chicken'])
print quantify('carrot', amount=90)
print quantify({'carrot': 100, 'parrot': 20})

print 'ngrams'
print ngrams("I am eating a pizza.", n=2)


#parse
s = parse('I eat pizza with a fork.')
pprint(s)

#tag
for word, t in tag('The cat felt happy.'):
    print word +' is ' +t     
    
s = "The movie attempts to be surreal by incorporating various time paradoxes, but it's presented in such a ridiculous way it's seriously boring."    
print sentiment(s)     
print polarity(s)
print subjectivity(s)

#The modality() function returns a value between -1.0 and +1.0, expressing the degree of certainty
s2 = "Some amino acids tend to be acidic while others may be basic." # weaseling
se = Sentence(parse(s, chunks=False, lemmata=True))
print modality(se)