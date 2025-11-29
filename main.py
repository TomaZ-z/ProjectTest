import random
import time


gameRun = True






def gameStart ():
    global gameRun
    gameRun = True

def gameEnd():
    global gameRun
    print("Game is closing now  :)")
    time.sleep(5)
    gameRun = False

#-------------events-------------#

def e_basic():
    print("This is a basic encounter")

def e_slight():
    print("This is a slightly basic encounter")
    
def e_advanced():
    print("This is an advanced encounter")

#--------------------------------#

def event_perc():
    global events
    global et_random
    global et_chosen
    events = [e_basic,e_slight,e_advanced]
    et_random = random.choices(events,weights=[10,5,2],k=1)
    et_chosen = et_random[0]()
    return


def event_occurr():
    print(et_chosen)






print("Welcome to ProjectTest. A text-based rougelike project being worked on by a idiot!")

while True:
    gm_start_status = str(input("Would you like to start the game or quit?\nStart / Quit  "))
    if gm_start_status.lower() == "start":
        print("Booting up game.")
        time.sleep(2)
        break
    elif gm_start_status.lower() == "quit":
        gameEnd()
        break
    else:
        print("Invalid command. Please retry.")
    

while gameRun is True:
    event_perc()
    input("next?")