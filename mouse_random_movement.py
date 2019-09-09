import pyautogui
import random

file = open("test.log", "w")

file.write(str(1920) + " " + str(1080) + "\n")

for i in range(0, 100000000):
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    #pyautogui.moveTo(x, y)
    file.write(str(x) + " " + str(y) + "\n")

#for i in range(0, 1000000):
#    for j in range(0, 8):
#        for k in range(0, 8):
#            x = 100 + j
#            y = 100 + k
#            file.write(str(x) + " " + str(y) + "\n")


file.write(str(random.randint(1000, 1100)) + " " + str(random.randint(1000, 1100)) + "\n")

file.close()