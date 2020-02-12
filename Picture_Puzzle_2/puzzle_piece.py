'''Tile class represents tiles meant for the picture_puzzle class. Each tile takes in
an image, (x,y) coordinate tuple and [x,y] new coordinate list set by default to the
values of the tuple
Final Project 1
Fall 2018
@author: Caleb Vredevoogd (chv5)'''
import unittest

class Tile:
    def __init__(self, orig_xy = (0,0), constraint = ()):
        '''Tile object has original (x,y) coordinates, current (x,y) coordinates, which
        are set by default to original coordinates, and type, which is set to 'x'''
        self.orig = orig_xy
        self.crnt = orig_xy
        self.const = constraint
        self.type = 'x'
    
    def get_type(self):
        '''returns type'''
        return self.type
    
    def get_orig(self):
        '''returns original coordinates'''
        return self.orig
    
    def get_current(self):
        '''returns current coordinates'''
        return self.crnt
    
    def set_current(self, newt):
        self.crnt = newt
    
    def change_current(self, new_c):
        '''changes the current coordinates to a new tuple or list new_c'''
        self.crnt = new_c
        
    def get_constraint(self):
        '''returns the image constraint variable'''
        return self.const
    
    def set_constraint(self, new):
        '''sets the image constraint variable. Ideally this will only be used once'''
        self.const = new
        
    def switch(self, other):
        '''swap current coordinates with an adjacent object of a different type'''
        temp_coord_var_o = other.get_current()
        temp_coord_var_s = self.get_current()
        self.change_current(temp_coord_var_o)
        other.change_current(temp_coord_var_s)
        
class Pic_tile(Tile):
    def __init__(self, orig_xy, constraint):
        '''Pic_tile's constructor is identical to Tile except for the use of super()
        and self.type = 'pic' '''
        Tile.__init__(self, orig_xy, constraint)
        self.orig = orig_xy
        self.crnt = orig_xy
        self.type = 'pic'
        
#Unittest test cases
class Test_accessor(unittest.TestCase):
    tile_a = Tile((0,1), ())
    tile_tuple = tile_a.get_orig()
    assert tile_a.get_orig() == (0,1)
    assert tile_tuple[0] == 0
    
class Test_switch(unittest.TestCase):
    tile_x = Tile((2,2), ())
    tile_y = Tile((45,33), ())
    tile_x.switch(tile_y)
    
    assert tile_x.get_current() == (45,33)
    assert tile_y.get_current() == (2,2)
    
if __name__ == "__main__":
    unittest.main()