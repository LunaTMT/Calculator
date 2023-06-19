from tkinter import Button
from functools import partial

class CustomButton:

    def __init__(self, interface, text, pos_x, pos_y, size_x=2, size_y=2) -> None:
        
        self.screen = interface.screen
        self.button = Button(interface.window, 
                             text=text, 
                             width=size_x, height=size_y,
                             command = partial(self.screen.__iadd__, text))
        
        self.button.place(x = pos_x, y = pos_y)
        
