import pync
import time

print("Program activated, your reminder will be sent according to the specified amount of seconds")

print("This is the first reminder:")
# ----------------------------------------------------------------------------------------------------------------------

seconds = 900

# 1800 seconds is equal to 30 minutes
# 900 seconds is equal to 15 minutes


# ----------------------------------------------------------------------------------------------------------------------

while True:
    pync.notify("Don't forget to drink water")
    print("Reminder sent!")
    time.sleep(seconds)
