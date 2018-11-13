#!/usr/bin/python
import sys, re, telepot
message=(sys.argv)[1]
bot = telepot.Bot(token='535077668:AAH_DpjjasrRi20dD-S6uJ9R1gcGnPVv3_w')
chat_id = bot.getUpdates()[-1].message.chat_id
print(chat_id)
