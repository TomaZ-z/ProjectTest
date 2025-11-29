#-------------import-------------#

import random
import time

#--------------------------------#
#-----------attributes-----------#

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

#--------------------------------#
#------------variable------------#

gameRun = True

#--------------------------------#
#-------------events-------------#

def e_basic():
    print(f"{ITALIC}This is a basic encounter{END}")

def e_slight():
    print(f"{CROSSED}This is a slightly basic encounter{END}")
    
def e_advanced():
    print(f"{UNDERLINE}This is an advanced encounter{END}")

#--------------------------------#
#------------function------------#

def gameStart ():
    global gameRun
    gameRun = True

def gameEnd():
    global gameRun
    print("Game is closing now  :)")
    time.sleep(5)
    gameRun = False

def event_perc():
    global events
    global et_random
    global et_chosen
    events = [e_basic,e_slight,e_advanced]
    et_random = random.choices(events,weights=[10,5,2],k=1)
    et_chosen = et_random[0]()
    return

#--------------------------------#
#--------------main--------------#

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
    input("reroll another")

#--------------------------------#
