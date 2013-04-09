import matplotlib.pyplot as MPL
import numpy as NP
import matplotlib.cm as cm
#from scipy import misc as MSC
#import matplotlib.image as MPI

class CheckerBoard:
    def __init__(self, width_pixel=1600, length_pixel=800, num_block=8):
        self.width_pixel = width_pixel
        self.length_pixel = length_pixel
        self.num_block = num_block
        self.width_block = self.width_pixel / num_block
        self.length_block = self.length_pixel / num_block
                        
    def generate_pixels(self):
        #all black to begin with
        self.pixels = NP.zeros((self.length_pixel, self.width_pixel))
        for j in NP.arange(self.num_block):
            for i in NP.arange(self.num_block):
                if (j + i ) % 2 == 1:
                    self.pixels[j*self.length_block:(j+1)*self.length_block:1, i*self.width_block:(i+1)*self.width_block:1] = 1
                        
    def render(self):
        MPL.imshow(self.pixels, cmap = cm.gist_gray)
        MPL.show()
        
  
cb = CheckerBoard()
cb.generate_pixels()
cb.render()