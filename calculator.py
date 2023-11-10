# Import Module 
from PySimpleGUI import *
  
# GUI Layout 
# multi dimensional list containing a row of the calculators layout
layout = [[Txt(''  * 10)], 
          [Text('', size = (15, 1), font = ('Helvetica', 18), #Creating the text element for the window of the calculator: First the text, then the size, then the font, then allow for an input.
                text_color = 'black', key = 'input')], 
          [Txt(''  * 10)], 
          [ReadFormButton('c'), ReadFormButton('«')], 
          [ReadFormButton('7'), ReadFormButton('8'), ReadFormButton('9'), ReadFormButton('/')], 
          [ReadFormButton('4'), ReadFormButton('5'), ReadFormButton('6'), ReadFormButton('*')], #Creating the buttons for the calculator using the ReadFormButton function
          [ReadFormButton('1'), ReadFormButton('2'), ReadFormButton('3'), ReadFormButton('-')], 
          [ReadFormButton('.'), ReadFormButton('0'), ReadFormButton('='), ReadFormButton('+')], 
          ] 
  
# Set PySimpleGUI 
form = FlexForm('CALCULATOR', default_button_element_size = (5, 2), #Creating the window for the calculator using the FlexForm function then creating the default button element size and setting the auto size to false so it doesn't automatically fit the size to the text
                
                auto_size_buttons = False, grab_anywhere = False) #Grab anywhere is set to false so the user can't move the window around
form.Layout(layout) #setting the layout to the list we created earlier
  
# Result Value 
Result = '' 
  
# Make Infinite Loop 
def new_func(form, Result):
    form.FindElement('input').Update(Result)#FindELement finds the element wit the key input and updates it with the result

while True: 
    # Button Values 
    button, value = form.Read()#form.Read is used to read events from the window. It returns a tuple containing the button clicked and the values of the input elements. So button contains the the label of the button and value will contain the dicitonary of input values 
      
    # Check Press Button Values 
    if button == 'c': #If the button is c then it cears the result window
        Result = '' 
        new_func(form, Result) 
    elif button=='«': 
        Result = Result[:-1] #If the button is backspace then it removes the last character from the result window
        form.FindElement('input').Update(Result) 
    elif len(Result) == 16 : #If the length of result is 16 then it will not allow the user to enter any more characters
        pass
      
   # Results 
    elif button == '=': 
        Answer = eval(Result) #If the button is the number then it will evaluate the result and display the answer. eval() evaluates the string expression directly and returns the result.
        Answer = str(round(float(Answer),3)) # simply rounds the answer to 3 decimal places
        form.FindElement('input').Update(Answer) #Update the input for answer
        Result = Answer 
          
    # close the window 
    elif button == 'Quit'  or button == None: 
        break
    else: 
        Result += button #If the button is not any of the above then it will add the button to the result window. Such as the 8 button or the + button
        form.FindElement('input').Update(Result)#Update the input for result