import pyautogui as bot # install using pip (Ex - pip install pyautogui) command in terminal.
                # To See Doc --> https://pypi.org/project/PyAutoGUI/
import time # it is inbuilt class

while True:
    time.sleep(3)
    # bot.keyDown('shift') # to make the 1st letter upper case.
    bot.typewrite('i love you lengti.',interval=0.15)
    bot.press('enter')

