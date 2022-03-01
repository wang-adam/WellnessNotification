import time
from notify import notification
import datetime

# Shows notification every 45 minutes.
minutes = 45

print("Wellness notification that reminds you to take a break every", minutes, "minutes")

# Runs forever, until the computer is shut down or the program is terminated?
while(True):
    time.sleep(60*minutes)
    notification(
        message='Personal Wellness Notification',
        summary='Drink some water and take a stretch break. Let your eyes take a break from the screen. ♡'
    )
    print("Last notified at", datetime.datetime.now())
