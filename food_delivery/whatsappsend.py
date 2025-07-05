
import pywhatkit as kit
import datetime

# Set the time a minute ahead from current time
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1  # message will be sent 1 minute from now

# Send message
kit.sendwhatmsg("+917219463969", "mobile reprai kelak tu", hour, minute)

