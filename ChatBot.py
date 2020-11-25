from chatterbot import ChatBot
from PIL import ImageTk
from PIL import Image
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *



# pyttsx3
bot = ChatBot("Chat Bot")


trainer=ChatterBotCorpusTrainer(bot)


# training  bot 

trainer.train("chatterbot.corpus.english")



main = Tk()

main.geometry("500x620")

main.title("Chat Bot")

img = PhotoImage(file="bot.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)

def bot_response():
    query = textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    print(type(bot_response))
    msgs.insert(END, "Bot : " + str(answer))
  
    textF.delete(0, END)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# text field

textF = Entry(main, font=("Calibri", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="SEND", font=("Calibri", 20),command=bot_response)
btn.pack()

main.mainloop()