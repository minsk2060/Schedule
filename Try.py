import pywinauto
from pywinauto.application import Application

from pywinauto import Desktop

# app =Application(backend ="uia").connect(path="C://Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
# app.window(title_re='.*- Microsoft Edge', control_type="Window").set_focus()
# d = Desktop(backend='uia')
# main_window = d.window(title_re='.*- Microsoft Edge', control_type="Window")
# main_window.dump_tree()
# main_window.set_focus()
# windows = Desktop(backend="uia").windows()
#
# for w in windows:
#     print(w)
#     print(type(w))
#     #print(w.window_text())

# app = Application().connect(path=r"C:/Windows/System32/notepad.exe")
# app = Application(backend="uia").connect(path="C://Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
# # dlgspec = app.window()
# pywinauto.findwindows.enum_windows()
# print(pywinauto.findwindows.enum_windows())
# app.window(title_re = "*pywinauto").set_focus()
# app = Application(backend="uia").connect(path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
# print(app.process)
# print(app.windows())
app = Application(backend="uia").connect(title_re=u".*Microsoft\u200b Edge", timeout=10)
app.window().set_focus()
# print(app.process)
# print(app.windows())
# app.window(title_re=u".*Microsoft\u200b Edge").dump_tree()