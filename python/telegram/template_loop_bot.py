#1.0
import telepot
import random
import datetime
import time
import subprocess

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
        user = str(chat_id)
        msg = ""
        print( 'User: ' + user + ' Nachricht: ' + str(command) )

        if command == '/roll':
                bot.sendMessage(chat_id, random.randint(1,6))
        elif command == '/time':
                bot.sendMessage(chat_id, str(datetime.datetime.now()))
        elif command == '/temp':
                msg = subprocess.getoutput("/opt/vc/bin/vcgencmd measure_temp")
                bot.sendMessage(chat_id,msg)
                print(user + ": " + msg )

bot = telepot.Bot('BOT-TOKEN')
bot.message_loop(handle)

print( 'I am listening ...')

while 1:
    time.sleep(10)