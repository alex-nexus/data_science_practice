import MySQLdb
import re, string
from BeautifulSoup import BeautifulSoup
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import nltk

class SeoKeywords:
    def __init__(self):
        self.connect_db()

        self.stemmer = LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()

        self.noun_dict = {}
        self.adj_dict ={}

        self.punctuation = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
        self.filter_occurrence_threshold = 2
        self.sample_rate = 10

    def connect_db(self):
        self.db = MySQLdb.connect(host="localhost", user="king_app_dev", passwd="!ac-okl.34.731", db="king")
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def run(self):
        #gather product corpus per category
        category_ids = self.get_category_ids_with_many_products()

        for category_id in category_ids:
            products = self.get_products_by_category_id(category_id)
            pc=0
            for product in products:
                pc+=1

                if pc % self.sample_rate != 0:
                    continue

                print pc
                self.process_product(product)

        print 'product count: '+str(pc)

        self.nouns = [k for k, v in self.noun_dict.iteritems() if v > self.filter_occurrence_threshold]
        self.adjectives = [k for k, v in self.adj_dict.iteritems() if v > self.filter_occurrence_threshold]

        print 'nouns'
        print len(self.nouns)
        print self.nouns

        print 'adjectives'
        print len(self.adjectives)
        print self.adjectives

    def process_product(self, product):
        #1
        sentence = self.clean_product_string(product)

        #2
        words = self.tokenize_sentence(sentence)

        #3
        nouns, adjectives = self.extract_nouns_and_adjectives(words)

        for noun in nouns:
            self.noun_dict[noun] = self.noun_dict.get(noun, 0) + 1

        for adjective in adjectives:
            self.adj_dict[adjective] = self.adj_dict.get(adjective, 0) + 1

    #processing the corpus
    def clean_product_string(self, product):
        print 'clean_product_corpus:'
        sentence = product['name'] #+ '\n' + product['description']

        #strip lines
        #sentence = " ".join(sentence.splitlines())
        #strip html
        sentence = " ".join([str(s) for s in BeautifulSoup(sentence).findAll(text=True)])

        #strip punctuations (translate is fastest)
        sentence = sentence.translate(None, self.punctuation)

        #TODO:filter more words

        return sentence

    def tokenize_sentence(self, sentence):
        print sentence
        print '-->'
        #tokenize, lower case, remove stop words, lemmatize
        words = [self.lemmatizer.lemmatize(w.lower()) for w in nltk.word_tokenize(sentence) if w not in stopwords.words('english') ]
        #words = [self.stemmer.stem(w) for w in words]
        return words

    def extract_nouns_and_adjectives(self, words):
        tags = nltk.pos_tag(words)
        print tags

        nouns = set([t[0] for t in tags if t[1] in ['NN']])
        adjectives = set([t[0] for t in tags if t[1] in ['JJ']])
        return (nouns, adjectives)

    #this return the categories with more than 10000 products
    def get_category_ids_with_many_products(self):
        print 'get_category_ids_with_many_products'
        return [120401]
        return [100101, 100402, 109999, 110102, 110106, 110804, 119999, 120203, 120401, 130102, 130804, 131503, 139999,
                150901, 160501, 170301, 170401, 179999, 190301, 200103]

        query = """SELECT cd.category_id, cd.name, cd.description, count(p2c.product_id) as product_count
                FROM category c
                JOIN category_description cd on c.category_id = cd.category_id,
                product_to_category p2c
                WHERE c.category_id = p2c.category_id
                GROUP BY 1
                HAVING count(p2c.product_id) > 10000"""
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        category_tuples = [(row['category_id'], row['name']) for row in results]
        return category_tuples

    def get_products_by_category_id(self, category_id):
        print 'get_products_by_category_id:' + str(category_id)
        query = """SELECT pd.product_id, pd.name, pd.description
                FROM product_to_category p2c, product_description pd
                WHERE p2c.product_id = pd.product_id
                AND p2c.category_id = %s;"""
        self.cursor.execute(query, category_id)
        products = self.cursor.fetchall()
        print 'count:' + str(len(products))
        return products

    def end(self):
        self.db.close()


sk = SeoKeywords()
sk.run()
sk.end()




