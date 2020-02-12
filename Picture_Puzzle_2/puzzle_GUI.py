'''GUI for the picture_puzzle class. Should have a timer that increments by 1 each second until the puzzle
is completed or reset. The user moves tiles around the puzzle by switching them by clicking on one and then
the other. The puzzle is completed once all the picture tiles are in their original positions, resembling
the original picture.

Fall 2018
Final Project CS108
@author: Caleb Vredevoogd (chv5)'''

from tkinter import *
from picture_puzzle import Four_by_four


class Puzzle_GUI:
    
    def __init__(self, window, image):
        '''
        Constructor takes in a window and image, makes GUI for picture_puzzle class
        '''
        
        self.window = window
        
        self.image = image
        self.can_width = 400
        self.can_height = 400
        self.winnerlabel = StringVar()

        self.canvas = Canvas(self.window, width = self.can_width, height = self.can_height)
        self.canvas.pack(side = 'left')
        self.fbf = Four_by_four(self.image)
        self.fbf.shuffle()
        self.canvas.bind('<Button-1>', self.check_win())
        self.fbf.render(self.canvas)
        
        
        buttonframe = Frame(self.window)
        buttonframe.pack(side = 'right')
        
        self.shuffle_var = False
        shuffle_button = Button(buttonframe, text = "Shuffle", command = self.shuffle, width = 8)
        shuffle_button.pack()
        
        reset_button = Button(buttonframe, text = "Reset", command = self.reset_PZ, width = 8)
        reset_button.pack()
        
        self.clock = IntVar()
        self.clock.set(0)
        clocklabel = Label(buttonframe, textvariable = self.clock)
        clocklabel.pack()
        
        self.winner = False
        winlabel = Label(buttonframe, textvariable = self.winnerlabel)
        winlabel.pack()
        
        self.reset = False
        self.change_clock()
        self.start_game()
        
        
    def start_game(self):
        '''Shuffles the puzzle and renders'''
        self.fbf.shuffle()
        self.fbf.shuffle()
        self.fbf.render(self.canvas)

    def check_win(self):
        '''Constantly checks for wins while the puzzle is not reset'''
        if self.fbf.checkwin() == True:
            if self.reset == False:
                self.winner = self.fbf.checkwin()
                self.reset = True
                print("Should display 'You've won!' ")
                self.winnerlabel.set("You've won!")
    
    def change_clock(self):
        '''Based off of prof. VanderLinden's timer example. 
        Clock will stop if reset button is pressed or if game is won.
        Otherwise, it'll increment as usual.'''
        #reset the clock and keep it there when the puzzle is reset
        if self.reset == True:
            self.clock.set(0)
        
        if self.winner == True:
            self.clock.set(self.clock.get())
            
        #If the puzzle hasn't been reset and the game hasn't been won, increment the timer    
        elif (self.reset == False) or (self.winner == False):
            self.clock.set(self.clock.get()+1)
            
            self.canvas.after(1000, self.change_clock)
            self.check_win()
            
            
        
    def reset_PZ(self):
        '''Resets the puzzle using the reset() method, then re-renders the puzzle'''
        self.reset = True
        self.change_clock()
        self.fbf.reset(self.canvas)
        self.fbf.render(self.canvas)
        self.canvas.update()
        
    def shuffle(self):
        '''Calls the four_by_four's shuffle function, re-renders and updates the canvas'''
        #print("CANVAS: Shuffle")
        self.fbf.shuffle()
        self.fbf.shuffle()
        self.fbf.render(self.canvas)
        self.reset = False
        self.change_clock()
        self.canvas.update()
        self.shuffle_var = True

if __name__ == "__main__":
    root = Tk()
    root.title("Picture Puzzle")
    #Second argument in Puzzle_GUI can be changed to the name of any 400x400 image in the folder
    app = Puzzle_GUI(root, 'Nature.jpg')
    root.mainloop()