import webbrowser, schedule, time
from selenium import webdriver
from pywinauto.application import Application

# PREFX = "http://www.google.com"
# app = Application(backend="uia")
# app.connect(title_re=".*Microsoft\u200b Edge", timeout=10)
# app.window().set_focus()
# webbrowser.open_new_tab(PREFX)
# driver = webdriver.Edge(executable_path ="C://Program Files (x86)/Microsoft/Edge/Application/edgedriver_win64/msedgedriver.exe")
# driver = webdriver.Edge()
driver = webdriver.Edge()
driver.get("https://www.google.com/")
driver.get("https://www.google.com/")
driver.close()









