import webbrowser, schedule, time
from selenium import webdriver
from pywinauto.application import Application

path ="../logging/log_scheduling.txt"
f = open(path,"r")
current = f.read()
f.close()
f = open(path, "w")
f.write(current + "456")
f.close()








