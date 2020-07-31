# Notification shower using Python

import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
    title = "You need to do Java Programming today.",
    message = "Its fun!",
    app_icon = "/home/rishi_garg/Pictures/Screenshot from 2020-07-29 13-44-22.png",
    timeout = 3
    )
