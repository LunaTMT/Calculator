from typing import Any
from screen import Screen
from custom_button import CustomButton

import tkinter as tk
from functools import partial

class CalculatorInterface():

    def __init__(self) -> None:
        self.window     =        tk.Tk()
        self.window.geometry('360x370') 


        self.screen        =       Screen(self)
        
        self.C               = CustomButton(self, "C",   18, 310)
        self.plus_equals     = CustomButton(self, "+/-", 18, 250)
        self.AC              = CustomButton(self, "DEL", 18, 190)
        self.ON              = CustomButton(self, "OFF", 18, 130)

        self.zero            = CustomButton(self, "0",   69, 310)
        self.one             = CustomButton(self, "1",   69, 250)
        self.four            = CustomButton(self, "4",   69, 190)
        self.seven           = CustomButton(self, "7",   69, 130)

        self.zero_zero       = CustomButton(self, "00",  120, 310)
        self.two             = CustomButton(self, "2",   120, 250)
        self.five            = CustomButton(self, "5",   120, 190)
        self.eight           = CustomButton(self, "8",   120, 130)

        self.dot             = CustomButton(self, ".",   170, 310)
        self.three           = CustomButton(self, "3",   170, 250)
        self.six             = CustomButton(self, "6",   170, 190)
        self.nine            = CustomButton(self, "9",   170, 130)

        self.plus            = CustomButton(self, "+",   218, 253, size_y=5)
        self.times           = CustomButton(self, "X",   218, 190)
        self.percent         = CustomButton(self, "%",   218, 130) 

        self.equal           = CustomButton(self, "=",   265, 310)
        self.minus           = CustomButton(self, "-",   265, 250)
        self.divide          = CustomButton(self, "÷",   265, 190)
        self.sq_rt           = CustomButton(self, "√",   265, 130)


        self.mem_plus        = CustomButton(self, "M+",  310, 310)
        self.mem_minus       = CustomButton(self, "M-",  310, 250)
        self.mem_read        = CustomButton(self, "MR",  310, 190)
        self.mem_clear       = CustomButton(self, "MC",  310, 130)

        

    def run(self):
        self.window.mainloop()
