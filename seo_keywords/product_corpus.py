import MySQLdb


class SeoKeywords:

    def __init__(self):
        self.db=MySQLdb.connect(host="localhost", user="king_app_dev", passwd="!ac-okl.34.731",db="king")
        self.cursor = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)


    def run(self):
        #gather product corpus per category
        category_tuples = self.get_category_id()

        for category_id in category_tuples:
            products = self.get_products_by_category_id(category_id)
            #processing the corpus

            #clean by stem and lemmatize

            #identify adjective and noun

            #permuate

    def get_category_id(self):
        print 'get_category_id'
        return [100101, 100402, 109999, 110102, 110106, 110804, 119999, 120203, 120401, 130102, 130804, 131503, 139999, 150901, 160501, 170301, 170401, 179999, 190301, 200103]

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
        print 'get_products_by_category_id:'+str(category_id)
        query = """SELECT pd.product_id, pd.name, pd.description
                FROM product_to_category p2c, product_description pd
                WHERE p2c.product_id = pd.product_id
                AND p2c.category_id = %s;"""
        self.cursor.execute(query, category_id)
        products = self.cursor.fetchall()
        print 'count:'+str(len(products))
        return products

    def end(self):
        self.db.close()


sk = SeoKeywords()
sk.run()
sk.end()




