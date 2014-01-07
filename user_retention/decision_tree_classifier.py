import os
from collections import defaultdict
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import numpy as NP
import csv

class DecisionTreeClassifier:
    def __init__(self, ):
      self.cohort_user_ids = set()
      self.retained_user_ids = set()
      self.actions = set()
      self.user_action_dict = defaultdict(lambda: defaultdict(int)) 

    def run(self):
      self.import_user_behavior()
      self.import_retained_user_id()
      self.featurize()
      self.init_numpy_data()
      self.load_numpy_data()
      self.train()
      
    def import_user_behavior(self):
      f= open('user_actions.csv', 'r')
      reader = csv.reader(f, delimiter='|')
      for row in reader:
        user_id, action, count = int(row[0]), row[1], int(row[2])
        print user_id, action, count
        self.cohort_user_ids.add(user_id)
        self.actions.add(action)
        self.user_action_dict[user_id][action] = count

    def import_retained_user_id(self):
      file= open('retained_user_ids.txt', 'r')
      for line in file:
        self.retained_user_ids.add(int(line))
      
    def featurize(self):
      self.row_count = len(self.cohort_user_ids)
      self.col_count = len(self.actions)
      print 'rows#', self.row_count
      print 'columns#', self.col_count

      self.cohort_user_tx = dict([(i, attr) for i, attr in enumerate(sorted(self.cohort_user_ids))])        
      self.cohort_user_lut = dict([(attr, i) for i, attr in self.cohort_user_tx.items()])            

      self.action_tx = dict([(i, attr) for i, attr in enumerate(sorted(self.actions))])        
      self.action_lut = dict([(attr, i) for i, attr in self.action_tx.items()])
      
    def init_numpy_data(self):
      self.X = NP.zeros((self.row_count, self.col_count), dtype=NP.int)
      self.y = NP.zeros(self.row_count, dtype=NP.int)

    def load_numpy_data(self):
      print 'load_numpy_data'
      for user_id, action_count in self.user_action_dict.iteritems():
        i = self.cohort_user_lut[user_id]
        for action, count in action_count.iteritems():
          j = self.action_lut[action]
          self.X[i, j] = count
          #add response variable
          if user_id in self.retained_user_ids:
            self.y[i] = 1
          
    def train(self):
      print 'train'
      self.dt = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None, min_samples_leaf=1,)
      self.dt = self.dt.fit(self.X, self.y)
      with open("user_actions.dot", 'w') as f:
        f = tree.export_graphviz(self.dt, out_file=f)
      os.system("dot -Tpdf user_actions.dot -o user_actions.pdf")    


dtc = DecisionTreeClassifier()
dtc.run()