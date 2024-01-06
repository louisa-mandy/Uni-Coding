# tk inter button 

from tkinter import *
import random

window = Tk()
window.geometry('300x300')
window.title('test')


'''def changecolor():
    
    window.config(bg='green')'''


'''Label(window, text='hello world', bg = 'red').grid(row=2, column=0)

btn1 = Button(window, text ='change color', command = changecolor)

btn1.grid()

Button(window, text='Click Here', command=changecolor).grid(row=6,column=0)'''

score = 0 


def changetext():
    global score # biar score bisa kebaca di dalam function
    score+=1
    text1.config(bg='purple', fg='yellow', text = score)
    

def reset_button():
    text1.config(text = 0)

def change_color():
    colors = [ '#93D2DF', '#E9D1EE', '#D8EED1', '#FFFCB9', 'black']
    randomcolor = random.choice(colors)
    window.config(bg= randomcolor)

text1 = Label(window, text='0', bg='yellow', fg='red', font=('Arial','30','bold')) # font type, font size, intensity
text1.grid(row=5,column=15)

Button(window, text='click count', command=changetext).grid(row=10,column=15)
Button(window, text='reset button', command=reset_button).grid(row=15,column=15)
Button(window, text='Change color', command=change_color).grid(row=20,column=15)

window.mainloop()