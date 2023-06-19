
from tkinter import Label
from math import sqrt
import sys

class Screen():
    

    def __init__(self, interface) -> None:
        self.memory = ""
        self.screen = ""
        self.specials = {"X" : "*",
                         "÷" : "/"}
                         
        self.functions = {"√"   : self.square_root,
                          "DEL" : self.delete,
                          "C"   : self.clear_screen,
                          "+/-" : self.absolute_value,
                          "OFF" : self.quit,
                          "MR"  : self.recall_memory,
                          "MC"  : self.clear_memory,
                          "%"   : self.get_percent}
                         
        self.screen_label =  Label(interface.window, 
                            bg="white", 
                            width=40, height=3)
        self.screen_label.place(x = 20, y = 20)


        self.memory_label =  Label(interface.window, 
                            bg="grey", 
                            width=10, height=1)
        self.memory_label.place(x = 260, y = 58)


    def __iadd__(self, value):
        if self.screen == "Syntax ERROR":
            self.screen = value
        elif any(memory_functions in self.screen for memory_functions in ("M-", "M+")) and value == "=":
            self.memory_evaluate()
        elif value == "=":
            self.evaluate()
        elif value in self.specials:
            self.get_special(value)
        elif value in self.functions:
            self.get_function(value)
        else:
            self.screen += value
        
        self.update_screen()
        
 
    def memory_evaluate(self):
        self.screen = self.screen.replace("M", self.memory)
        self.evaluate()
    def evaluate(self):
        try:
            self.screen = str(eval(self.screen))
            self.memory = self.screen 
            self.update_memory()
        except:
            self.screen = "Syntax ERROR"
    def get_special(self, value):
        self.screen += self.specials[value]
    def get_function(self, value):
        self.functions[value]()
    
    def update_screen(self):
        self.screen_label['text'] = self.screen 
    def update_memory(self):
        self.memory_label['text'] = self.memory
    def clear_screen(self):
        self.screen = ""

    def square_root(self):
        self.screen = f"sqrt({self.screen})"
    def delete(self):
        self.screen = self.screen[:-1]
    def absolute_value(self):
        idx = 1
    
        if self.screen and self.screen[0] == "-":
            while True:
                try:
                    if self.screen[idx] == '-':
                        idx += 1
                    else:
                        break
                except:
                    break

            self.screen = self.screen[idx:]
    def quit(self):
        sys.exit(0)  
    def get_percent(self):
        self.screen = str(eval(f"{self.screen}/100"))
   
    def recall_memory(self):
        self.screen += self.memory
    def clear_memory(self):
        self.memory = ""
        self.update_memory()