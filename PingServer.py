from discordwebhook import Discord
from time import gmtime, strftime
import time
import datetime

discord = Discord(url="https://discord.com/api/webhooks/1132091000635002981/v1APgHUgAqMm5i58CeH0jv6i3YsaIJGqA6sY_Jc2Z01WMJr-dlcCrmIZ-Yodv0yRVdMW")
# discord.post(content="@ち, Hello there")
now = datetime.now()
SetTime = "09:25:00"

while True:    
    CurrentTime = (strftime("%H:%M:%S", gmtime()))
    if SetTime == CurrentTime:
        discord.post(content="@ち, Hello there")
        print(f"correct time: {CurrentTime}")
        time.sleep(1)
    else:
        print(f"not time: {CurrentTime}")
        time.sleep(1)
