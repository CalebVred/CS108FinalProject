'''puzzle class that takes a 400x400 pixel image, divides it into 16
tile objects and randomizes the value of their current coordinates.
Final Project 1
Fall 2018
@author: Caleb Vredevoogd (chv5)'''

#having modes for different difficulties could be a bigger challenge than you originally thought
from PIL import Image, ImageTk
import tkinter as tk
import unittest

from puzzle_piece import Tile, Pic_tile
from numpy.random.mtrand import randint
from PIL.ImageTk import PhotoImage


class Four_by_four():
    
    def __init__(self, image):
        '''Constructor for a 3x3 puzzle class takes in window and 400x400 image'''
        self.im = Image.open(image)
        #test_image_object = ImageTk.PhotoImage(self.im)
        #test_label = tk.Label(self.window, image = test_image_object)
        self.tile_list = []
        self.shufflebreak = False
        self.pic_dict = {}
        self.reset_var = True
        self.make_gridlist()
        self.build_dict()

        self.button_dict = {}
        
        self.event_list = []
        
        self.switchlist = []
        
        self.button_sum = 0
    
        
        #test_label.pack()

    def make_gridlist (self):
        '''Makes a list of tiles with original coordinates but no constraint'''
        for piece_x in range (0,4):
            for piece_y in range (0,4):
                orig_coord = (piece_x, piece_y)
                tile = Pic_tile(orig_coord, ())
                self.tile_list.append(tile)
    
                   
    def build_dict(self):
        '''Builds a dictionary with coordinate tuples as keys and tiles with 
        (left, upper, right, lower) bounds as the constraint value
        Also can be used to rebuild the puzzle in its original order'''
        constant = 100
        for tile in self.tile_list:
            tile_tuple = tile.get_orig()
            box = (tile_tuple[0]*constant, tile_tuple[1]*constant, 
                   (tile_tuple[0]+1)*constant, ((tile_tuple[1]+1)*constant))
            im_key = str(tile_tuple)
            tile.set_constraint(box)
            self.pic_dict[im_key] = tile
            
                
    def render (self, canvas):
        '''Renders a photo to a canvas using current coordinates''' 
        if self.reset_var == True:
            self.build_dict()
            #self.reset(canvas)
            self.reset_var = False
        
        for key, tile in self.pic_dict.items():
            cropped = self.im.crop(tile.get_constraint())
            ph = ImageTk.PhotoImage(cropped)
            pic_button = tk.Button(canvas, image = ph, 
                                   command = lambda k = key: self.to_be_switched(k, canvas))
            pic_button.image = ph
            self.button_dict[key] = pic_button
              
            coord = tile.get_current()
            pic_button.grid(row = coord[1], column = coord[0])

        #for key, tile in self.pic_dict.items():
        self.to_be_switched()    
        canvas.update()     

    def to_be_switched(self, strng = None, canvas = None):
        '''Receives two keys from buttons, matches them to two tiles and switches them'''
        
        can = canvas
        if strng != None:
            for key, tile in self.pic_dict.items():
                if key == strng:
                    self.switchlist.append(tile)
                    #print("Added tile with key " + key + " to to_be_switched")
                    #print("Length of to_be_switched: " + str(len(self.switchlist)))
                        
                    if len(self.switchlist) == 2:
                        #print("The length of to_be_switched is 2. Executing puzzle_switch...\n")
                        self.puzzle_switch(self.switchlist[0], self.switchlist[1])
                        self.render(can)
                        #can.update()
                        self.checkwin()
                        self.switchlist = []
                        return True
                        break

    def reset(self, canvas):
        '''Resets tiles to their original coordinates'''
        self.reset_var = True
        for key, tile in self.pic_dict.items():
            tile.change_current(tile.get_orig())
        self.render(canvas)
        canvas.update()    
        
    def puzzle_switch(self, tile1, tile2):
        '''Matches the (x,y) coordinates of two events to two tile pixel constraints. Once a match is found,
        switch the two tiles' current coordinates and assign '''
        #print ("tile1's current coordinates: " + str(tile1.get_current()))
        #print ("tile2's current coordinates: " + str(tile2.get_current()) + "\n")
        #print ("Executing tile1.switch(tile2)\n")
        tile1.switch(tile2)
        #print ("tile1's current coordinates: " + str(tile1.get_current()))
        #print ("tile2's current coordinates: " + str(tile2.get_current()) + "\n")                       
    
    def checkwin(self):
        '''Checks if all the tiles on the puzzle are in their original position
         and returns True if so or vice versa'''
        #print("self.to_be_switched as been executed, checking for win...")
        maybe_win = True
        for key, tile in self.pic_dict.items():
            if tile.get_orig() != tile.get_current():
                maybe_win = False
                break
        #print(str(maybe_win))
        return maybe_win
        
    def shuffle(self):
        '''Shuffles tiles' current coordinates. '''        
        
        for key, tile in self.pic_dict.items():
            rand_self = '(' + str(randint(0, 4)) + ', ' + str(randint(0, 4)) + ')'  
            while True:
                rand_other = '(' + str(randint(0, 4)) + ', ' + str(randint(0, 4)) + ')'
                if rand_other == rand_self:
                    return
                else:
                    break
            
            self.pic_dict[rand_self].switch(self.pic_dict[rand_other])
        
        for key, tile in self.pic_dict.items():
            if self.pic_dict[key].get_orig() == self.pic_dict[key].get_current():
                self.shuffle()
            else:
                break
            #test_dict[rand_self] = self.pic_dict[rand_self]
            #test_dict[rand_other] = self.pic_dict[rand_other]

    
if __name__ == '__main__':
    
    class Shuffle_test(unittest.TestCase):
        four_by_four = Four_by_four('Dog.jpg')
        four_by_four.shufflebreak = False
        four_by_four.shuffle()
        
    class Switch_test(unittest.TestCase):
        f_b_f = Four_by_four('Dog.jpg')
        f_b_f.shufflebreak = False
    
    unittest.main()