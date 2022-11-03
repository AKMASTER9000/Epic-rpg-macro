from pynput.keyboard import Key, Controller
import time
sus = True
donstat = input("Are you a donator? \n(no=not a donator, don=donator, epic=epic d, super=super+) \n- ")
hrea = 60
wrea = 300
frea = 600
advrea = 3600
hunt = 59
work = 298
farm = 597
adventure = 3596
if donstat == "don":
    hrea = hrea * 0.9
    wrea = wrea * 0.9
    frea = frea * 0.9
    advrea = advrea * 0.9
    hunt -= 6
    work -= 30
    farm -= 60
    adventure -= 360
if donstat == "epic":
    hrea = hrea * 0.8
    wrea = wrea * 0.8
    frea = frea * 0.8
    advrea = advrea * 0.8
    hunt -= 12
    work -= 60
    farm -= 120
    adventure -= 720
if donstat == "super":
    hrea = hrea * 0.65
    wrea = wrea * 0.65
    frea = frea * 0.65
    advrea = advrea * 0.65
    hunt -= 21
    work -= 105
    farm -= 210
    adventure -= 1260
print("The macro(w) will start in 10 seconds")
time.sleep(10)
while(sus):
    keyboard = Controller()
    hunt += 1
    work += 1
    farm += 1
    adventure += 1
    if hunt == hrea + 1:
        keyboard.type("Rpg hunt h t")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        hunt = 0
    if work == wrea + 1:
        keyboard.type("Rpg bigboat")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        work = 0
    if farm == frea + 1:
        keyboard.type("Rpg farm")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        farm = 0
    if adventure == advrea + 1:
        keyboard.type("Rpg adv")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        adventure = 0
    time.sleep(1)
