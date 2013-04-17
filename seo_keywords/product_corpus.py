import MySQLdb
from BeautifulSoup import BeautifulSoup
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

import nltk

class SeoKeywords:
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="king_app_dev", passwd="!ac-okl.34.731", db="king")
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        self.stemmer = LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()


    def run(self):
        #gather product corpus per category
        category_ids = self.get_category_ids_with_many_products()

        for category_id in category_ids:
            products = self.get_products_by_category_id(category_id)

            for product in products:
                self.clean_product_corpus(product)
                return

            #identify adjective and noun

            #permuate

    #processing the corpus
    def clean_product_corpus(self, product):
        print 'clean_product_corpus:'
        sentence = product['name'] + '\n' + product['description']

        print 'raw'
        print sentence
        #sentence = sentence.splitlines()
        #strip html
        sentence = " ".join(BeautifulSoup(sentence).findAll(text=True))

        print 'processed'
        print sentence

        #tokenize, lower case, remove stop words
        words = [w.lower() for w in nltk.word_tokenize(sentence) if w not in stopwords.words('english') ]
        words = [self.lemmatizer.lemmatize(w) for w in words]
        print words

        print 'tags'
        tags = nltk.pos_tag(words)
        nouns = [t[0] for t in tags if t[1] in set(['NNP', 'NNS', 'NN', 'NP'])]
        adjectives = [t[0] for t in tags if t[1] in set(['JJ'])]

        print 'nouns'
        print nouns

        print 'adjectives'
        print adjectives

        #
        # print filtered_word_tokens


        #clean by stem

        #lemmatize

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




