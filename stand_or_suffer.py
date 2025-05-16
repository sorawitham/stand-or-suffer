import time
from datetime import datetime
from plyer import notification


def show_notification():
    notification.notify(
        title="Stand Up!",
        message="Time to rise, stretch, and defy the chair gods.",
        timeout=10,  # show for 10 seconds
    )


print("💡 stand-or-suffer is running... (press Ctrl+C to stop)")

while True:
    now = datetime.now()
    if now.minute % 15 == 0 and now.second == 0:
        show_notification()
        time.sleep(60)  # prevent double notification in the same minute
    else:
        time.sleep(1)
