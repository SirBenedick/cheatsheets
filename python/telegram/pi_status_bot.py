import telepot
import subprocess
import datetime
from pprint import pprint

bot = telepot.Bot('BOT_TOKEN')
#print(bot.getMe())

response = bot.getUpdates()
#pprint(response)

msg =    "Status: \n"
msg +=  str(datetime.datetime.now()) + "\n"
msg +=  subprocess.getoutput("df -h") + "\n\n"
msg +=  subprocess.getoutput("free -h") + "\n\n"
msg +=  subprocess.getoutput("/opt/vc/bin/vcgencmd measure_temp") + "\n\n"

bot.sendMessage(USER_ID, msg)
