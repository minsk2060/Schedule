from pywinauto.application import Application
from pywinauto import keyboard
import pywinauto.mouse as mouse
app = Application().start(r"C:\Windows\System32\notepad.exe")
app.connect(path=r"C:\Windows\System32\notepad.exe")
main_dlg = app.window(title='Безымянный.txt-Блокнот')
dlg = app['Безымянный-Блокнот']
dlg.set_focus()
keyboard.send_keys('Hello{ENTER}')
# dlg.menu_select("Вид -> Строка состояния")
# dlg.menu_select("Файл -> Сохранить как")

# dlg.menu_select("Правка -> Заменить...")
# dlg.Edit.type_keys('Welcome to Medium')

# dlg.Replace.Cancel.click()