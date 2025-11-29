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

full_gameRun = True
p1_gameRun = True
p2_gameRun = True
p3_gameRun = True
start_status = True
level = 0
v_tips = ["Just test build, bare in mind!","These are actually useless"]
xp = 0
level = 1
alive_mob = []





goblin1 = False
goblin2 = False
goblin3 = False
slime1 = False
slime2 = False
slime3 = False
bandit1 = False
bandit2 = False
bandit3 = False
bandit4 = False
hgoblin1 = 0
hgoblin2 = 0
hgoblin3 = 0
hslime1 = 0
hslime2 = 0
hslime3 = 0
hbandit1 = 0
hbandit2 = 0
hbandit3 = 0
hbandit4 = 0
#--------------------------------#
#-------------events-------------#

def ba_goblin():
    global goblin1
    global goblin2
    global slime1
    global goblin3
    global st_ba_goblin
    mob_count = random.randint(1,10)
    if mob_count <= 3:
        st_ba_goblin = True
        goblin1 = True
        goblin2 = True
    elif mob_count <= 7 and mob_count > 3:
        st_ba_goblin = True
        goblin1 = True
        goblin2 = True
        slime1 = True
    elif mob_count >= 10 and mob_count > 7:
        st_ba_goblin = True
        goblin2 = True
        goblin1 = True
        slime1 = True
        goblin3 = True


def ba_slime():
    global slime1
    global slime2
    global goblin1
    global slime3
    global st_ba_slime
    mob_count = random.randint(1,10)
    if mob_count <= 3:
        st_ba_slime = True
        slime1 = True
        slime2 = True
    elif mob_count <= 7 and mob_count > 3:
        st_ba_slime = True
        slime1 = True
        slime2 = True
        goblin1 = True
    elif mob_count >= 10 and mob_count > 7:
        st_ba_slime = True
        slime1 = True
        slime2 = True
        goblin1 = True
        slime3 = True
    
def ba_bandit():
    global bandit1
    global bandit2
    global bandit3
    global bandit4
    global st_ba_bandit
    mob_count = random.randint(1,10)
    if mob_count <= 4:
        st_ba_bandit = True
        bandit1 = True
        bandit2 = True
    elif mob_count <= 8 and mob_count > 4:
        st_ba_bandit = True
        bandit1 = True
        bandit2 = True
        bandit3 = True
    elif mob_count >= 10 and mob_count > 8:
        st_ba_bandit = True
        bandit1 = True
        bandit2 = True
        bandit3 = True
        bandit4 = True

#--------------------------------#
#------------function------------#

def gameStart ():
    global full_gameRun
    full_gameRun = True

def gameEnd():
    global full_gameRun
    print("Game is closing now  :)")
    time.sleep(5)
    full_gameRun = False

def tips():
   tips_random = random.choices(v_tips,k=1)
   print("<TIP>   ",tips_random[0])
   return

def ba_event_proc():
    global et_random
    global et_chosen
    events = [ba_goblin,ba_slime,ba_bandit]
    et_random = random.choices(events,weights=[10,5,2],k=1)
    et_chosen = et_random[0]()
    return

def hero_choose():
    global hero
    while True:
        hero_num = int(input("What class you want to play from?\n1) Knight\n2) Archer\n"))
        if hero_num == 1:
            hero = "Knight"
            break
        elif hero_num == 2:
            hero = "Archer"
            break
        else:
            continue
    return

def level_sys():
    global xp
    global level
    if xp >= 10*(level*1.1):
        level = level + 1

def ba_check_mob_hp():
    global goblin1
    global goblin2
    global goblin3
    global slime1
    global slime2
    global slime3
    global bandit1
    global bandit2
    global bandit3
    global bandit4
    global hgoblin1
    global hgoblin2
    global hgoblin3
    global hslime1
    global hslime2
    global hslime3
    global hbandit1
    global hbandit2
    global hbandit3
    global hbandit4
    global alive_mob
    if goblin1 == True:
        hgoblin1 = 8*(level*0.5)
        alive_mob.append("goblin1")
    if goblin2 == True:
        hgoblin2 = 8*(level*0.5)
        alive_mob.append("goblin2")
    if goblin3 == True:
        hgoblin3 = 8*(level*1)
        alive_mob.append("goblin3")
    if slime1 == True:
        hslime1 = 6*(level*0.5)
        alive_mob.append("slime1")
    if slime2 == True:
        hslime2 = 6*(level*0.5)
        alive_mob.append("slime2")
    if slime3 == True:
        hslime3 = 6*(level*1)
        alive_mob.append("slime3")
    if bandit1 == True:
        hbandit1 = 10*(level*0.5)
        alive_mob.append("bandit1")
    if bandit2 == True:
        hbandit2 = 10*(level*0.5)
        alive_mob.append("bandit2")
    if bandit3 == True:
        hbandit3 = 10*(level*0.5)
        alive_mob.append("bandit3")
    if bandit4 == True:
        hbandit4 = 10*(level*1)
        alive_mob.append("bandit4")

#------------classatk------------#

def archer():
    global level
    global hero
    global ar_basic1
    global ar_basic1atk
    global ar_isbasic1
    global ar_basic1isaoe
    global ar_basic2
    global ar_basic2atk
    global ar_basic2cd
    global ar_isbasic2
    global ar_basic2isaoe
    global ar_ult
    global ar_ultatk
    global ar_ultcd
    global ar_isult
    global ar_ultisaoe
    if hero == "Archer":
        if level >= 1:
            ar_isbasic1 = True
            ar_basic1 = "bowshot"
            ar_basic1atk = 6
            ar_basic1isaoe = False
        if level >= 2:
            ar_isbasic2 = True
            ar_basic2 = "snipe"
            ar_basic2atk = 10
            ar_basic2cd = 1
            ar_basic2isaoe = False
        if level >= 5:
            ar_isult = True
            ar_ult = "arrow rain"
            ar_ultatk = 32
            ar_ultcd = 3
            ar_ultisaoe = True

#--------------------------------#
#--------------game--------------#
while full_gameRun is True:

    print("Welcome to ProjectTest. A text-based rougelike project being worked on by an idiot!")

    
    gm_start_status = str(input("Would you like to start the game or quit?\nStart / Quit  "))
    if gm_start_status.lower() == "start":
        print("Booting up game.\n")
        time.sleep(2)
    elif gm_start_status.lower() == "quit":
        gameEnd()

    while p1_gameRun is True:
        print("Starting a match\n ")
        time.sleep(1.5)
        tips()
        print(" ")
        time.sleep(1.5)
        hero_choose()
        print(f"You've chosen {hero}!\n\n\n")
        break

    while p2_gameRun is True:
        ba_event_proc()
        ba_check_mob_hp()
        if hero == "Archer":
            archer()
        break

    while p3_gameRun is True:
        print(alive_mob)
        break
    break

#--------------------------------#
