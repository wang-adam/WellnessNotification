import plyer
import time
from plyer.utils import platform
from plyer import notification
import datetime

# Shows notification every hour.
minutes = 60

# Runs forever, until the computer is shut down or the program is terminated?
while(True):
    time.sleep(60*minutes)
    notification.notify(
        title='Personal Wellness Notification',
        message='Drink some water and take a stretch break. Let your eyes take a break from the screen. ♡',
        timeout=10,
    )
    print("Last notified at ", datetime.datetime.now())
