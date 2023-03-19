import webbrowser, time
import pyautogui as pg
from pywinauto.application import Application

import ctypes



# PREFX = "http://www.google.com"
# app = Application(backend="uia").connect(title_re=".*Microsoft\u200b Edge", timeout=10)
# app.window().set_focus()
# webbrowser.open_new_tab(PREFX)
# time.sleep(2)
# pg.hotkey('ctrl', 'w')
# pg.hotkey('alt', 'shift')
# time.sleep(2)
# pg.hotkey('ctrl', 'w')



      
def keyboard():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'

print(keyboard())