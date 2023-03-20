import webbrowser, time, schedule
import pyautogui as pg
from pywinauto.application import Application
import ctypes



#
#
def keyboard():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'

def turn():
    app = Application(backend="uia").connect(title_re=".*Microsoft\u200b Edge", timeout=10)
    app.window().set_focus()
    webbrowser.open_new_tab('http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=8388815&did=33561432&vid=17&value=2')
    time.sleep(2)
    keyboard()
    if keyboard() == "ru":
        print("russian keyboard is detected")
        # hotkey("alt", "shift")
        # time.sleep(3)
        pg.keyUp('ctrl')
        pg.press('w')
        pg.keyDown('ctrl')
        print("after the 'ctrl ц' string ")
    elif keyboard() == "en":
        print("english keyboard is detected")
        # time.sleep(3)
        pg.hotkey('ctrl', 'w')
        print("after the 'ctrl W' string ")

schedule.every(15).seconds.do(turn)



while True:
    schedule.run_pending()
    time.sleep(1)
