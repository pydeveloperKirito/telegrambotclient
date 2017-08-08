import time
from tkinter import *
import telepot
from telepot.loop import MessageLoop
def handle(msg):
    chat_id = msg['chat']['id']
    messaggio = msg['text']
    user = msg ['chat']['username']
    nome = msg['chat']['first_name']
    if messaggio != "":
        root = Tk()
        w = Label(root, text= chat_id)
        w.pack()
        x = Label(root, text= nome)
        x.pack()
        h = Label(root, text= user)
        h.pack()
        y = Label(root, text= messaggio)
        y.pack()
        root.geometry("300x80")
        root.mainloop()
        print ("hai ricevuto : ", messaggio)
        print ("dall'utente: ", nome)
        print ("dall'username: ", user)

bot = telepot.Bot('inserisci qui il tuo token')

MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)


    
