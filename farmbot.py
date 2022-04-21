from random import randint, random
import pyautogui
import time
import random
from datetime import datetime


def harverstfinder():
        sunflower = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\sunflower.png", confidence=0.7,grayscale=True)
        pumpkin = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\normal_pumpkin .png", confidence=0.8)
        patato = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\patato.png", confidence=0.7,grayscale=True)
        carrot = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\carrot.png", confidence=0.8)
        if sunflower:
            print("ayçiçeği toplanacak")
            harvester("C:\\Users\\doruk\\Desktop\\farmbit\\sunflower.png")
        if pumpkin:
            print("balkabağı toplanacak")
            harvester("C:\\Users\\doruk\\Desktop\\farmbit\\normal_pumpkin .png")
        if patato:
            print("patates toplanacak")
            harvester("C:\\Users\\doruk\\Desktop\\farmbit\\patato.png")
        if carrot:
            print("havuç toplanacak")
            harvester("C:\\Users\\doruk\\Desktop\\farmbit\\carrot.png")
        else:
            print("toplanacak bir şey yok")    
        
def harvester(prodctjpg):

    x = True
    while x==True:
            outthecheck = None
            prodct = pyautogui.locateOnScreen(
            prodctjpg, confidence=0.7,grayscale=True)
            veggiechest = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\veggiechest.png", confidence=0.8)
            chest = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\chest.png", confidence=0.6)
            close_button = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\close.png", confidence=0.8)
            # chest
            if chest != None:
                pointerlocation = chest
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
                pointerlocation[1] = pointerlocation[1]+randint(-30, 0)
                pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
                pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                chest = None
                outthecheck = 1
                close_button = None
                veggiechest = None
                prodct=None
                time.sleep(sleeptime)
                time.sleep(0.5)

            if close_button != None:
                pointerlocation = close_button
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
                pointerlocation[1] = pointerlocation[1]+randint(-15, 15)
                pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
                pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                close_button = None
                veggiechest = None
                chest = None
                prodct=None
                outthecheck = 1
                time.sleep(sleeptime)
                time.sleep(0.5)

            if veggiechest != None:
                pointerlocation = veggiechest
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-10, 10)
                pointerlocation[1] = pointerlocation[1]+randint(-25, -5)
                pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
                pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                chest = None
                outthecheck = 1
                close_button = None
                veggiechest = None
                prodct=None
                time.sleep(sleeptime)    
            
            if prodct != None:
                pointerlocation = prodct
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-10, 10)
                pointerlocation[1] = pointerlocation[1]+randint(-10, 10)
                pointerlocation[2] = pointerlocation[2]+randint(-10, 10)
                pointerlocation[3] = pointerlocation[3]+randint(-10, 10)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

            if chest== None and close_button==None and veggiechest==None and prodct==None and outthecheck==None:
                x=False
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"Toplandı {current_time}")
    
    
"""      while x == True:

        veggiechest = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\veggiechest.png", confidence=0.8)
        chest = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\chest.png", confidence=0.8)
        close_button = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\close.png", confidence=0.8)
        sunflower = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\sunflower.png", confidence=0.7,grayscale=True)
        pumpkin = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\normal_pumpkin .png", confidence=0.8)
        patato = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\patato.png", confidence=0.7,grayscale=True)
        carrot = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\carrot.png", confidence=0.8)
        outthecheck = None
        # chest
        if chest != None:
            pointerlocation = chest
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
            pointerlocation[1] = pointerlocation[1]+randint(-30, 0)
            pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
            pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            chest = None
            outthecheck = 1
            close_button = None
            veggiechest = None
            chest = None
            sunflower = None
            pumpkin = None
            patato = None
            carrot = None
            time.sleep(sleeptime)
            time.sleep(0.5)
        
        # close button
        if close_button != None:
            pointerlocation = close_button
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
            pointerlocation[1] = pointerlocation[1]+randint(-15, 15)
            pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
            pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            close_button = None
            veggiechest = None
            chest = None
            sunflower = None
            pumpkin = None
            patato = None
            carrot = None
            outthecheck = 1
            time.sleep(sleeptime)
            time.sleep(0.5)

        # collect chested veggie
        if veggiechest != None:
            pointerlocation = veggiechest
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-10, 10)
            pointerlocation[1] = pointerlocation[1]+randint(-25, -5)
            pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
            pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            chest = None
            outthecheck = 1
            close_button = None
            veggiechest = None
            chest = None
            sunflower = None
            pumpkin = None
            patato = None
            carrot = None
            time.sleep(sleeptime)

        # collect patato
        if patato != None:
            pointerlocation = patato
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-10, 10)
            pointerlocation[1] = pointerlocation[1]+randint(-10, 10)
            pointerlocation[2] = pointerlocation[2]+randint(-10, 10)
            pointerlocation[3] = pointerlocation[3]+randint(-10, 10)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            time.sleep(sleeptime)

        # collect carrot
        if carrot != None:
            pointerlocation = carrot
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
            pointerlocation[1] = pointerlocation[1]+randint(-15, 15)
            pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
            pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            time.sleep(sleeptime)

        # collect pumpkin
        if pumpkin != None:
            pointerlocation = pumpkin
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-15, 15)
            pointerlocation[1] = pointerlocation[1]+randint(-15, 15)
            pointerlocation[2] = pointerlocation[2]+randint(-15, 15)
            pointerlocation[3] = pointerlocation[3]+randint(-15, 15)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            time.sleep(sleeptime)

        # collect sunflower
        if sunflower != None:
            pointerlocation = sunflower
            pointerlocation = list(pointerlocation)
            pointerlocation[0] = pointerlocation[0]+randint(-10, 10)
            pointerlocation[1] = pointerlocation[1]+randint(-10, 10)
            pointerlocation[2] = pointerlocation[2]+randint(-10, 10)
            pointerlocation[3] = pointerlocation[3]+randint(-10, 10)
            pointerlocation = tuple(pointerlocation)
            pyautogui.moveTo(pointerlocation)
            sleeptime = (random.randint(300, 500))/5000
            time.sleep(sleeptime)
            pyautogui.click(pointerlocation)
            sleeptime = (random.randint(300, 999))/5000
            time.sleep(sleeptime)

        if patato == None and veggiechest == None and sunflower == None and pumpkin == None and veggiechest == None and close_button == None and chest == None and outthecheck == None:
            x = False 
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print(f"Toplandı {current_time}")
 """


def planter(slc):
    x = True
    planting=["","sunflower","patato","pump","carrot"]
    print(f"ekilecek={planting[slc]}")

    while x == True:
        if slc == 1:
            print("ayçiçeği ekiliyor")
            if pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\Selectedsunflowerseed.png") != None:

                y = True
                while y == True:
                    hole = pyautogui.locateOnScreen(
                        "C:\\Users\\doruk\\Desktop\\farmbit\\normal_hole.png", confidence=0.8)
                    if hole == None:
                        hole = pyautogui.locateOnScreen(
                            "C:\\Users\\doruk\\Desktop\\farmbit\\middlehole.png", confidence=0.8)

                    if hole == None:
                        y = False
                        x = False

                    if hole != None:
                        pointerlocation = hole
                        pointerlocation = list(pointerlocation)
                        pointerlocation[0] = pointerlocation[0] + \
                            randint(-10, 10)
                        pointerlocation[1] = pointerlocation[1] + \
                            randint(-25, -5)
                        pointerlocation[2] = pointerlocation[2] + \
                            randint(-15, 15)
                        pointerlocation[3] = pointerlocation[3] + \
                            randint(-15, 15)
                        pointerlocation = tuple(pointerlocation)
                        pyautogui.moveTo(pointerlocation)
                        sleeptime = (random.randint(300, 500))/5000
                        time.sleep(sleeptime)
                        pyautogui.click(pointerlocation)
                        sleeptime = (random.randint(300, 999))/5000
                        hole = None
                        time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselectedsunflowerseed.png", confidence=0.8) != None:
                print("ayçiçek tohumu ekrandan seçildi")
                # buraya dikkat
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\unselectedsunflowerseed.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselectedsunflowerseed.png", confidence=0.8) == None and pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\Selectedsunflowerseed.png") == None:
                print("ayçiçek tohumu envanterden seçildi")
                # open items
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\items.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(1, 3))
                time.sleep(sleeptime)
                # find sunflower
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\sunflowerinbasket.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)
                # close menu
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\closemenu.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

        if slc == 2:
            print("patates ekiliyor")
            if pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\selectedpatatoseed.png") != None:

                y = True
                while y == True:
                    hole = pyautogui.locateOnScreen(
                        "C:\\Users\\doruk\\Desktop\\farmbit\\normal_hole.png", confidence=0.8)
                    if hole == None:
                        hole = pyautogui.locateOnScreen(
                            "C:\\Users\\doruk\\Desktop\\farmbit\\middlehole.png", confidence=0.8)

                    if hole == None:
                        y = False
                        x = False

                    if hole != None:
                        pointerlocation = hole
                        pointerlocation = list(pointerlocation)
                        pointerlocation[0] = pointerlocation[0] + \
                            randint(-10, 10)
                        pointerlocation[1] = pointerlocation[1] + \
                            randint(-25, -5)
                        pointerlocation[2] = pointerlocation[2] + \
                            randint(-15, 15)
                        pointerlocation[3] = pointerlocation[3] + \
                            randint(-15, 15)
                        pointerlocation = tuple(pointerlocation)
                        pyautogui.moveTo(pointerlocation)
                        sleeptime = (random.randint(300, 500))/5000
                        time.sleep(sleeptime)
                        pyautogui.click(pointerlocation)
                        sleeptime = (random.randint(300, 999))/5000
                        hole = None
                        time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselectedpatatoseed.png", confidence=0.8) != None:
                print("patates tohumu ekrandan seçildi")
                # buraya dikkat
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\unselectedpatatoseed.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselectedpatatoseed.png", confidence=0.8) == None and pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\selectedpatatoseed.png") == None:
                print("patates tohumu envanterden alınıyor")
                # open items
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\items.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(1,3))
                time.sleep(sleeptime)
                # find sunflower
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\patatoseedbasket.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)
                # close menu
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\closemenu.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

        if slc == 3:
            if pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\selected_pumpkin_seed.png") != None:
                print("pumpkin ekiliyor")
                y = True
                while y == True:
                    hole = pyautogui.locateOnScreen(
                        "C:\\Users\\doruk\\Desktop\\farmbit\\normal_hole.png", confidence=0.8)
                    if hole == None:
                        hole = pyautogui.locateOnScreen(
                            "C:\\Users\\doruk\\Desktop\\farmbit\\middlehole.png", confidence=0.8)

                    if hole == None:
                        y = False
                        x = False

                    if hole != None:
                        pointerlocation = hole
                        pointerlocation = list(pointerlocation)
                        pointerlocation[0] = pointerlocation[0] + \
                            randint(-10, 10)
                        pointerlocation[1] = pointerlocation[1] + \
                            randint(-25, -5)
                        pointerlocation[2] = pointerlocation[2] + \
                            randint(-15, 15)
                        pointerlocation[3] = pointerlocation[3] + \
                            randint(-15, 15)
                        pointerlocation = tuple(pointerlocation)
                        pyautogui.moveTo(pointerlocation)
                        sleeptime = (random.randint(300, 500))/5000
                        time.sleep(sleeptime)
                        pyautogui.click(pointerlocation)
                        sleeptime = (random.randint(300, 999))/5000
                        hole = None
                        time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselected_pumpkin_seed.png", confidence=0.8) != None:
                print("pumpkin tohumu ekrandan seçiliyordi")
                # buraya dikkat
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\unselected_pumpkin_seed.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\selected_pumpkin_seed.png") == None and pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\unselected_pumpkin_seed.png", confidence=0.8) == None:
                print("pumpkin envanterden seçiliyor")
                # open items
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\items.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(1,3))
                time.sleep(sleeptime)
                # find sunflower
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\pumpkinseedbasket.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)
                # close menu
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\closemenu.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

        if slc == 4:
            if pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\carrotseedselected.png") != None:
                print("havuç ekiliyor")
                y = True
                while y == True:
                    hole = pyautogui.locateOnScreen(
                        "C:\\Users\\doruk\\Desktop\\farmbit\\normal_hole.png", confidence=0.8)
                    if hole == None:
                        hole = pyautogui.locateOnScreen(
                            "C:\\Users\\doruk\\Desktop\\farmbit\\middlehole.png", confidence=0.8)

                    if hole == None:
                        y = False
                        x = False

                    if hole != None:
                        pointerlocation = hole
                        pointerlocation = list(pointerlocation)
                        pointerlocation[0] = pointerlocation[0] + \
                            randint(-10, 10)
                        pointerlocation[1] = pointerlocation[1] + \
                            randint(-25, -5)
                        pointerlocation[2] = pointerlocation[2] + \
                            randint(-15, 15)
                        pointerlocation[3] = pointerlocation[3] + \
                            randint(-15, 15)
                        pointerlocation = tuple(pointerlocation)
                        pyautogui.moveTo(pointerlocation)
                        sleeptime = (random.randint(300, 500))/5000
                        time.sleep(sleeptime)
                        pyautogui.click(pointerlocation)
                        sleeptime = (random.randint(300, 999))/5000
                        hole = None
                        time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\carrotseedunselected.png", confidence=0.8) != None:
                print("havuç ekrandan seçiliyor")
                # buraya dikkat
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\carrotseedunselected.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)

            elif pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\carrotseedselected.png") == None and pyautogui.locateOnScreen("C:\\Users\\doruk\\Desktop\\farmbit\\carrotseedunselected.png", confidence=0.8) == None:
                print("havuç envanterden seçiliyor")
                # open items
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\items.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(1,3))
                time.sleep(sleeptime)
                # find sunflower
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\basketcarrot.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)
                # close menu
                pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\closemenu.png", confidence=0.8)
                pointerlocation = list(pointerlocation)
                pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
                pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
                pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
                pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
                pointerlocation = tuple(pointerlocation)
                pyautogui.moveTo(pointerlocation)
                sleeptime = (random.randint(300, 500))/5000
                time.sleep(sleeptime)
                pyautogui.click(pointerlocation)
                sleeptime = (random.randint(300, 999))/5000
                time.sleep(sleeptime)


class seeds:
    def __init__(self, sunfseed, patseed, pumpseed, carseed, holes):
        self.sunfseed = int((sunfseed/holes)-(sunfseed-holes) % 1)
        self.patseed = int((patseed/holes)-(patseed-holes) % 1)
        self.pumpseed = int((pumpseed/holes)-(pumpseed-holes) % 1)
        self.carseed = int((carseed/holes)-(carseed-holes) % 1)
        self.lastplanted = ""

    def selector(self):
        #is it in i sor
        print(f"kalan sunflower ekim sayısı={self.sunfseed}\nkalan patates ekim sayısı={self.patseed}\nkalan pump ekim sayısı={self.pumpseed}\nkalan havuş ekim sayısı={self.carseed}")
        isitin=None
        if self.sunfseed > 0 and self.patseed > 0 and isitin==None:
            slc = randint(1, 2)
            if slc == 1:
                self.sunfseed -= 1
                planter(slc)
                self.lastplanted = "sunflower"
                isitin=1

            if slc == 2:
                self.patseed -= 1
                planter(slc)
                self.lastplanted = "patato"
                isitin=1

        if self.sunfseed > 0 and self.patseed == 0 and isitin==None:
            slc = 1
            planter(slc)
            self.sunfseed -= 1
            self.lastplanted = "sunflower"
            isitin=1

        if self.sunfseed == 0 and self.patseed > 0 and isitin==None:
            slc = 2
            planter(slc)
            self.patseed -= 1
            self.lastplanted = "patato"
            isitin=1

        if self.sunfseed == 0 and self.patseed == 0 and self.pumpseed > 0 and self.carseed > 0 and isitin==None:
            slc = random.randint(1, 10)
            if slc < 10:
                self.pumpseed -= 1
                planter(3)
                self.lastplanted = "pumpkin"
                isitin=1

            if slc==10:
                self.carseed -= 1
                planter(4)
                self.lastplanted = "carrot"
                isitin=1

        if self.sunfseed == 0 and self.patseed == 0 and self.pumpseed == 0 and self.carseed>0 and isitin==None:
            slc = 4
            self.carseed -= 1
            planter(slc)
            self.lastplanted = "carrot"
            isitin=1

        if self.sunfseed == 0 and self.patseed == 0 and self.carseed == 0 and self.pumpseed>0 and isitin==None:
            slc = 3
            self.pumpseed -= 1
            planter(slc)
            self.lastplanted = "pumpkin"
            isitin=1

        elif self.sunfseed == 0 and self.patseed==0 and self.carseed == 0 and self.pumpseed == 0:
            pointerlocation = pyautogui.locateOnScreen(
                "C:\\Users\\doruk\\Desktop\\farmbit\\closebrowser.png")
            pyautogui.moveTo(pointerlocation)
            pyautogui.click(pointerlocation)

def antiafk():
        pointerlocation = pyautogui.locateOnScreen(
        "C:\\Users\\doruk\\Desktop\\farmbit\\sunflowericon.png", confidence=0.8)
        pyautogui.moveTo(pointerlocation)
        pyautogui.click(pointerlocation)
         # open items
        pointerlocation = pyautogui.locateOnScreen(
                    "C:\\Users\\doruk\\Desktop\\farmbit\\items.png", confidence=0.8)
        pointerlocation = list(pointerlocation)
        pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
        pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
        pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
        pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
        pointerlocation = tuple(pointerlocation)
        pyautogui.moveTo(pointerlocation)
        sleeptime = (random.randint(300, 500))/5000
        time.sleep(sleeptime)
        pyautogui.click(pointerlocation)
        sleeptime = (random.randint(1,3))
        time.sleep(sleeptime)
         #close menu
        pointerlocation = pyautogui.locateOnScreen(
                     "C:\\Users\\doruk\\Desktop\\farmbit\\closemenu.png", confidence=0.8)
        pointerlocation = list(pointerlocation)
        pointerlocation[0] = pointerlocation[0]+randint(-1, 2)
        pointerlocation[1] = pointerlocation[1]+randint(-2, 2)
        pointerlocation[2] = pointerlocation[2]+randint(-5, 3)
        pointerlocation[3] = pointerlocation[3]+randint(-5, 3)
        pointerlocation = tuple(pointerlocation)
        pyautogui.moveTo(pointerlocation)
        sleeptime = (random.randint(300, 500))/5000
        time.sleep(sleeptime)
        pyautogui.click(pointerlocation)
        sleeptime = (random.randint(300, 999))/5000
        time.sleep(sleeptime)        
        #geri dön
        pointerlocation = pyautogui.locateOnScreen(
                "C:\\Users\\doruk\\Desktop\\farmbit\\netflixicon.png", confidence=0.8)
        pyautogui.moveTo(pointerlocation)
        pyautogui.click(pointerlocation)        


sunfseed = int(input("enter num sunfseed"))
patseed = int(input("enter number of pat seed"))
pumpseed = int(input("enter number of pump seed"))
carseed = int(input("enter number of car seed"))
holes = int(input("enter number of holes"))
seedobj = seeds(sunfseed=sunfseed, patseed=patseed,
                pumpseed=pumpseed, carseed=carseed, holes=holes)

while True:
    harverstfinder()
    seedobj.selector()

    pointerlocation = pyautogui.locateOnScreen(
        "C:\\Users\\doruk\\Desktop\\farmbit\\netflixicon.png", confidence=0.8)
    pyautogui.moveTo(pointerlocation)
    pyautogui.click(pointerlocation)
    print(f"ekildiğini söylediği={seedobj.lastplanted}")
    if seedobj.lastplanted == "sunflower":
        p = randint(4, 15)+50
        print(f"uyku zamanı={p}")
        time.sleep(p)
    if seedobj.lastplanted == "patato":
        p = randint(10, 22)+290
        print(f"uyku zamanı={p}")
        time.sleep(p)
    if seedobj.lastplanted == "pumpkin":
        p = randint(10, 70)+1800
        print(f"uyku zamanı={p}")
        time.sleep(p)
    if seedobj.lastplanted == "carrot":
        p = randint(100, 300)+3600
        x = (p/2)+randint(1,10)
        print(f"uyku zamanı={p}")
        time.sleep(x)
        x=p/2
        antiafk()
        time.sleep(x)

    try:
        pointerlocation = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\notepad_unselected.png")
        pyautogui.moveTo(pointerlocation)
        pyautogui.click(pointerlocation)
    except:
        try:
            pyautogui.press("esc")
            time.sleep(1)
            pyautogui.press("esc")
            pointerlocation = pyautogui.locateOnScreen(
            "C:\\Users\\doruk\\Desktop\\farmbit\\notepad_unselected.png")
            pyautogui.moveTo(pointerlocation)
            pyautogui.click(pointerlocation)
        except:

            pass    
        pass
    print("\n \n")
    pointerlocation = pyautogui.locateOnScreen(
        "C:\\Users\\doruk\\Desktop\\farmbit\\sunflowericon.png", confidence=0.8)
    pyautogui.moveTo(pointerlocation)
    pyautogui.click(pointerlocation)

    harverstfinder()
    time.sleep(2)