import pyautogui

file = open("low_data.log", "a")
file.write(str(pyautogui.size().width) + " " + str(pyautogui.size().height) + "\n")

lastX = 0
lastY = 0

try:
    while True:
        x = pyautogui.position().x
        y = pyautogui.position().y
        if lastX == x and lastY == y:
            continue
        lastX = x
        lastY = y
        file.write(str(x) + " " + str(y) + "\n")
        print("Point(x=" + str(x) + "; y=" + str(y) + ")")
except KeyboardInterrupt:
    pass

file.close()

input("Press enter to exit:")
