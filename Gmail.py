import pyautogui as pg
import webbrowser
import time
#make sure you log into gmail first
webbrowser.open("http://mail.gcds.net")
time.sleep(10)
#wait 10 seconds and then it pesses 'C'
pg.hotkey('c')
time.sleep(7)
pg.hotkey('tab')
time.sleep(1)
pg.typewrite("Phone call", 0.1)



time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.typewrite("Please call me when you have the chance.",0.1)
