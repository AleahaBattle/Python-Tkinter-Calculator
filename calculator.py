import tkinter as tk
from tkinter import ttk, Tk, StringVar, Entry
from tkinter.ttk import Style, Button


class Calculator(object):
    # class calc_value variable
    calc_value = 0.0

    # keep track of math buttons clicked
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    subt_trigger = False

    
    def __init__(self, root):
        # set the background colour of root window 
        root.configure(background='black')

        # set the title of root window
        root.title('Calculator')

        # the configuration of root window
        root.geometry('460x200')

        # block resizing of Window
        root.resizable(width=False, height=False)

        # hold value stored in entry
        self.display = StringVar(root, value='')

        # customize the styling for the buttons and entry
        style = Style()
        style.configure('TButton', font='Serif 15', padding=10)
        style.configure('TEntry', font='Serif 18', padding=10)
        
        # create the text entry box to show the expression. 
        self.expression_field = Entry(root, textvariable=self.display,
                                      width=50)
        self.expression_field.grid(row=0, columnspan=4)

        # ----- buttons --------
        # create Buttons and place at a particular 
        # location inside the root window. 
        # when user press the button, the command or 
        # function affiliated to that button is executed.
		
        # ----- 1st Row -----
        self.seven = Button(root, text='7', 
                            command=lambda: self.num_press(7)).grid(row=1, column=0)

        self.eight = Button(root, text='8', 
                        command=lambda: self.num_press(8)).grid(row=1, column=1)
        
        self.nine = Button(root, text='9', 
                        command=lambda: self.num_press(9)).grid(row=1, column=2)
        
        self.divide = Button(root, text='/', 
                        command=lambda: self.math_press('/')).grid(row=1, column=3)

        # ----- 2nd Row -----
        
        self.four = Button(root, text='4', 
                        command=lambda: self.num_press(4)).grid(row=2, column=0)
        
        self.five = Button(root, text='5', 
                        command=lambda: self.num_press(5)).grid(row=2, column=1)
        
        self.six = Button(root, text='6', 
                        command=lambda: self.num_press(6)).grid(row=2, column=2)
        self.multiply = Button(root, text='*', 
                        command=lambda: self.math_press('*')).grid(row=2, column=3)


        # ----- 3rd Row -----
        
        self.one = Button(root, text='1', 
                        command=lambda: self.num_press(1)).grid(row=3, column=0)
        
        self.two = Button(root, text='2', 
                        command=lambda: self.num_press(2)).grid(row=3, column=1)
        
        self.three = Button(root, text='3', 
                        command=lambda: self.num_press(3)).grid(row=3, column=2)
        self.subtract = Button(root, text='-', 
                        command=lambda: self.math_press('-')).grid(row=3, column=3)

        # ----- 4th Row -----
        
        self.clear = Button(root, text='AC', 
                        command=self.clear).grid(row=4, column=0)
                               
        self.zero = Button(root, text='0', 
                        command=lambda: self.num_press(0)).grid(row=4, column=1)
        
        self.equal = Button(root, text='=', 
                        command=self.equal_press).grid(row=4, column=2)
        
        self.add = Button(root, text='+', 
                        command=lambda: self.math_press('+')).grid(row=4, column=3)
    
	# ----- functions --------

    def num_press(self, num):
        # Function to update expressiom in the text entry box
        # Called anytime a number button is pressed

		# clear the entry box of previous evaluations if any
        self.expression_field.delete(0, 'end')
		
        # get the current value in the entry
        num_value = self.expression_field.get()
		
		# update current value, concatenate string of new value
        num_value += str(num)
        
		# clear the entry box
        self.expression_field.delete(0, 'end')

        # update the expression with the insert method
        self.expression_field.insert(0, num_value)


    def is_float(self, str_val):
		# Function to return True or False if the string is a float
        try:
			# check if string is a float with float() 
            float(str_val)
            return True
		# Handle ValueError if string isn't a float
        except ValueError:
            return False

    def math_press(self, value):
		# Function to Handles logic when math buttons are pressed
		
		# if entry contains a number, update trigger
        if self.is_float(str(self.expression_field.get())):
		
			# make false to cancel out previous math button click
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.subt_trigger = False
			
			# Get the value out of the entry box for the calculation
            self.calc_value = float(self.display.get())
			
			# Set the math button click so when equals is clicked
            # that function knows what calculation to use
            if value == '/':
                self.div_trigger = True
            elif value == '*':
                self.mult_trigger = True
            elif value == '+':
                self.add_trigger = True
            else:
                self.subt_trigger = True

		# clear the entry box
        self.expression_field.delete(0, 'end')
                          

    def equal_press(self):
        # Function to evaluate the final expression
        
        # handling the errors like zero 
        # division error etc.
        try:
            # check if a math button was clicked
            if self.div_trigger or self.mult_trigger or self.add_trigger or self.subt_trigger:
				
				# evaluate the expression
                if self.div_trigger:
                    solution = self.calc_value / float(self.display.get())
                elif self.mult_trigger:
                    solution = self.calc_value * float(self.display.get())
                elif self.add_trigger:
                    solution = self.calc_value + float(self.display.get())
                else:
                    solution = self.calc_value - float(self.display.get())

                print(self.calc_value, ' ', float(self.display.get()), ' ', solution)
				
				# clear the entry box
                self.expression_field.delete(0, 'end')
				
                # show the solution
                self.expression_field.insert(0, solution)

        except:
            # handle an error
            self.display.set('error')
            self.calc_value = ''
			self.expression_field.insert(0, 'error')
   
   
    def clear(self):
        # Function to clear the contents of text entry box
        self.expression_field.delete(0, 'end')


# ----- Run App --------
   
if __name__ == '__main__':
    # create a root window
    root = Tk()

    # create the calculator
    calc = Calculator(root)
   
    # start the root, run app until exited.
    root.mainloop()
