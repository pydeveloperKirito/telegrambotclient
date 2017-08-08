import time
import random
import datetime
import telepot.aio
from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
import telepot
from telepot.loop import MessageLoop
import subprocess
import sys
bot = telepot.Bot('inserisci il tuo token qui')
def message ():
    testo = input("cosa vuoi inviare?: ")
    if testo != "": 
       bot.sendMessage(chat,testo)
def choice():
    print ("digita ciao123 per uscire")
    print ("digita text per inviare un testo")
    print ("digita button per inviare un bottone")
chat = input("in quale chat vuoi inviare il messaggio?: ")
choice ()
scelta = input ("cosa vuoi fare?: ")
if scelta == "text":
    message ()
elif scelta == "ciao123":
    exit()
elif scelta == "button":
    testobottone = input("digita il testo del bottone: ")
    urlbottone = input("digita l'url del bottone: ")
    testo = input("digita il testo principale del messaggio: ")
    markup = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text= testobottone, url=urlbottone)]
    ])
    bot.sendMessage(chat,testo,reply_markup=markup )
