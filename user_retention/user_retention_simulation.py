from random import sample, randint
from collections import defaultdict
import csv

class UserRetentionSimulation:
  USER_ACTIONS = ['CommentAction', 'FollowAction', 'LikeAction', 'PostAction', 
    'ProductTagAction', 'PublishAction', 'RegisterAction', 'ResurrectAction', 
    'SaveAction', 'SearchAction', 'SessionAction']

  def __init__(self, user_count = 1000):
    self.user_count = user_count
    self.user_actions = defaultdict(lambda: defaultdict(int)) 

  def run(self):
    self.simulate_cohort_user_id()
    self.simulate_retained_user_id()
    self.simulate_user_behavior()
    self.export_to_csv()
    self.export_retained_user_ids()
    
  def simulate_cohort_user_id(self):
    self.user_ids = sample(range(self.user_count * 2), self.user_count)
    print 'cohort#', len(self.user_ids)

  def simulate_retained_user_id(self):
    self.retained_user_ids = sample(self.user_ids, int(self.user_count * 0.25)) 
    print 'retained#', len(self.retained_user_ids)  

  def simulate_user_behavior(self):
    print 'simulate_user_behavior...'
    number_actions = len(self.user_ids) * 100     
    for i in range(number_actions):
      user_id = self.user_ids[randint(0, self.user_count-1)]
      action = self.USER_ACTIONS[randint(0, 10)]
      self.user_actions[user_id][action] += 1
      if i%100 == 0:
        print i, user_id, action, self.user_actions[user_id][action]
          	
  def export_to_csv(self):
    print 'export user_actions to csv...'
    f= open('user_actions.csv', 'wb')
    writer = csv.writer(f, delimiter='|')
    for user_id, action_count in self.user_actions.iteritems():
      for action, count in action_count.iteritems():
        writer.writerow([user_id, action, count])
    f.close()

  def export_retained_user_ids(self):
    print 'export retained user ids to csv...'
    f = open('retained_user_ids.txt', 'wb')
    for user_id in self.retained_user_ids:
    	f.write(str(user_id)+"\n")
    f.close()

urs = UserRetentionSimulation()
urs.run()