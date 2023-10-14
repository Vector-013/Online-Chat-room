from client import Client
import time
from threading import Thread

c1 = Client("tim")
c2 = Client("god")


def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 1/10th of a second
        new_messages = c1.get_messages()  # get any new msgs from client
        msgs.extend(new_messages)  # add to local list of msgs
        for msg in new_messages:
            print(msg)  # display new msgs
            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()

c1.send_message("hello")
time.sleep(5)
c2.send_message("hello")
time.sleep(5)
c1.send_message("sup")
time.sleep(5)
c2.send_message("allgood")
time.sleep(5)
c1.send_message("nicea")
time.sleep(5)

c1.disconnect()
time.sleep(5)
