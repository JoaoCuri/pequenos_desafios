from tkinter import *
import pandas as pd
import random

background_color='#82E0AA'

df=pd.read_csv("C:/Users/joao.ferreira/Documents/100 days/31/data/french_words.csv")
to_learn=df.to_dict(orient='records')

def next_card():
    cartao=random.choice(to_learn)
    canvas.itemconfig(card_title,text='French')
    canvas.itemconfig(card_word,text=cartao['French'])





app=Tk()
app.title('Flashy')
app.config(padx=50,pady=50,bg=background_color)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/card_front.png")
canvas.create_image(400,220,image=card_front)
card_title=canvas.create_text(185,70,text='',font=('Arial',20,'italic'))
card_word=canvas.create_text(185,120,text='',font=('Arial',35,'bold'))
canvas.config(bg=background_color,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/wrong.png")
errou=Button(image=wrong,highlightthickness=0)
errou.grid(row=1,column=0)

right=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/right.png")
acertou=Button(image=right,highlightthickness=0)
acertou.grid(row=1,column=1)

next_card()

app.mainloop()