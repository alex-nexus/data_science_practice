from collections import Counter, defaultdict
import requests, StringIO
from multiprocessing import Pool,Array
import os, csv, math
from PIL import Image
from colormath.color_objects import RGBColor
from redis import StrictRedis as redis

class ProductColorIndexer:
  def __init__(self):
    self.rdb = redis.from_url('redis://localhost:6379', 2)
    self.file_name = 'image_file.csv'
    self.color_clusters = { 'red':    (255, 0, 0), 
                            'orange': (255, 127, 0), 
                            'yellow': (255, 255, 0), 
                            'green':  (0, 255, 0), 
                            'blue':   (0, 0, 255), 
                            'purple': (127, 0, 255), 
                            'pink':   (255,127,127),
                            'white':  (255, 255, 255), 
                            'gray':   (127,127,127), 
                            'black':  (0, 0, 0)}                                
    #optimize: compute color lab space in advance
  def run(self):
    i=0
    with open(self.file_name, 'rb') as csvfile:
      csv_reader = csv.reader(csvfile, delimiter='|', quotechar='"')
      for line_values in csv_reader:
        i+=1
        p_id, img_url = line_values
         
        if self.rdb.sismember('processed_pids', p_id):
          continue

        self.rdb.sadd('processed_pids', p_id)
        primary_color, percentage = self.process_image(img_url)
        print img_url
        print i, primary_color, percentage
        if percentage <= 40: #skip assigning color if the dominant color is < 40%
          print 'skipping'
          primary_color = 'unknown'              
        self.rdb.zadd('color-'+primary_color, percentage, p_id)
        self.rdb.hset('product:'+str(p_id), 'primary_color', primary_color)
        
  def download_image(self, img_url):  
    r = requests.get(img_url)
    if r.status_code == 200:    
      return Image.open(StringIO.StringIO(r.content))

  def detect_background(self, img):
    w, h = img.size
    corner_points = [(0, 0), (0, h / 2), (0, h - 1), (w - 1, 0), (w / 2, 0), 
              (w / 2, h - 1), (w - 1, h - 1), (w - 1, h / 2)]
    corner_rgbs = [img.getpixel(p) for p in corner_points]
    corner_colors = Counter([self.assign_color_cluster(rgb) for rgb in corner_rgbs])
    (majority_col, majority_count), = corner_colors.most_common(1)
    return majority_col if majority_count >= 4 else None      

  def assign_color_cluster(self, rgb_tuple):
    color_to_distances = [(color, self.lab_distance(rgb_tuple, cluster_rgb)) for color, cluster_rgb in self.color_clusters.iteritems()]
    return sorted(color_to_distances, key=lambda tup: tup[1])[0][0]
    
  def lab_distance(self, rgb1, rgb2):
    lab1 = RGBColor(rgb1[0],rgb1[1], rgb1[2]).convert_to('lab')
    lab2 = RGBColor(rgb2[0],rgb2[1], rgb2[2]).convert_to('lab')
    return round(lab1.delta_e(lab2), 2)
    
  def process_image(self, img_url): 
    img = self.download_image(img_url)
    bg_color = self.detect_background(img)
    rgb_dist = Counter(img.getdata())
    
    color_counter = defaultdict(lambda: 0)
    for rgb_tuple, c in rgb_dist.iteritems():
      if c <= 3: #skip pixel with rare colors
        continue
      color = self.assign_color_cluster(rgb_tuple)
      if color == bg_color: #skip if the color is background color
        continue
      color_counter[color] += c
    #print 'color_counter', color_counter.keys(), color_counter.values() 
    color_percentage = self.find_color_percentage(color_counter)
    return sorted(color_percentage.items(), key=lambda x: -x[1])[0]
        
  def find_color_percentage(self, color_counter):
    total_counter = sum(color_counter.values())
    return dict([(color, round(100.0 * count/total_counter, 2)) for color, count in color_counter.iteritems()])
  
  def display_color_dist(self):
    for color in self.color_clusters.keys():
      print color, self.rdb.zcard('color-'+color)
  
pci = ProductColorIndexer()
while True:
  try:
    pci.run()
  except:
    print 'error'    