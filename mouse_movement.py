from pynput import mouse
import  pyautogui

file = open("mouse_data.log", "w")
file.write(str(pyautogui.size().width) + " " + str(pyautogui.size().height) + "\n")

def on_move(x, y):
    print(x, y)
    file.write(str(x) + " " + str(y) + "\n")


def on_click(x, y, button, pressed):
    print(x, y)
    if pressed:
        print("Click")
        file.write("Click\n")
    else:
        print("Released")
        file.write("Released\n")
        if x == 0 and y == 0:
            return False


with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()


file.close()
