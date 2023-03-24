import time

try:
    import pyautogui

except:
    print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m]\x1b[38;2;0;255;251m Unable to found pyautogui lib in your system!")
    exit()

try:
    print("\x1b[38;2;0;255;251m[90 Points by the free | by x04000]")
    print("\nPress any key to start")
    input("")

    time.sleep(2)

    i = 0
    for i in range(30):
        i = i+1
        print("Search number: "+str(i))
        pyautogui.click()
        pyautogui.press("a")
        pyautogui.press("enter")
        time.sleep(1)

except KeyboardInterrupt:
    print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m]\x1b[38;2;0;255;251m Keyboard Interrupt!")
except:
    print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m]\x1b[38;2;0;255;251m A unknow error ocurred!")