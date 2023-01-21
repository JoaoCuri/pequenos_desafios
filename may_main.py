from tkinter import *
import pandas as pd
import random


try:
    df=pd.read_csv("C:/Users/joao.ferreira/Documents/100 days/31/data/words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("C:/Users/joao.ferreira/Documents/100 days/31/data/Ingle_port.csv")
    
to_learn=df.to_dict(orient='records')
cartao={}


def next_card():
    global cartao
    global flip_timer
    window.after_cancel(flip_timer)
    cartao=random.choice(to_learn)
    canvas.itemconfig(card_title,text='English',fill='black')
    canvas.itemconfig(card_word,text=cartao['English'],fill='black')
    canvas.itemconfig(card_back,image=front_img)
    flip_timer=window.after(3000, func=flip_card)
    
    
def flip_card():
    canvas.itemconfig(card_title,text='Português',fill='white')
    canvas.itemconfig(card_word,text=cartao['Português'],fill='white')
    #back_img=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/card_back.png")
    canvas.itemconfig(card_back,image=back_img)
    
def save():
    to_learn.remove(cartao)
    export=pd.DataFrame(to_learn)
    print(len(to_learn))
    export.to_csv("C:/Users/joao.ferreira/Documents/100 days/31/data/words_to_learn.csv")
    next_card()
    


window=Tk()
window.title('App')
window.geometry('500x500+100+90')
window.configure(bg='#ADF4C8')
window.resizable(False,False)

flip_timer=window.after(3000, func=flip_card)

canvas=Canvas(width=400,height=263,bg='#ADF4C8',highlightthickness=0)
canvas2=Canvas(width=400,height=263,bg='#ADF4C8',highlightthickness=0)
front_img=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/card_front.png")
back_img=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/card_back.png")
card_back=canvas.create_image(5, 15,anchor=CENTER,image=front_img)

card_title=canvas.create_text(185,70,text='',font=('Arial',20,'italic'))
card_word=canvas.create_text(185,120,text='',font=('Arial',35,'bold'))
canvas.place(relx=0.5, rely=0.4, anchor=CENTER)

wrong=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/wrong.png")
errou=Button(image=wrong,highlightthickness=0,command=next_card)
errou.place(x=60,y=350)

right=PhotoImage(file="C:/Users/joao.ferreira/Documents/100 days/31/images/right.png")
acertou=Button(image=right,highlightthickness=0,command=save)
acertou.place(x=340,y=350)

next_card()

window.mainloop()