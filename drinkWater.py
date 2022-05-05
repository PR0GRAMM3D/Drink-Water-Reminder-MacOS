from ast import While
import pync
import time



# Amount of seconds before the message is displayed
apples = 1800


# No need to change anything below this line

while True:
    pync.notify("Drink Water", sound="Bottle")
    time.sleep(apples)
