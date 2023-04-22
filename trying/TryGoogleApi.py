import csv
import io
import urllib.request
from openpyxl import load_workbook
schedule_book="https://docs.google.com/spreadsheets/d/1d9GnKlkZDhIBHlPBARGZ4LHm9ofKR9Au/edit?export?format=xlsx"
#schedule_download ="https://drive.google.com/u/0/uc?id=1Bmn-rVslcQHW9q5!j6tA1S6xAKllu2Rf&export=download"
logo = urllib.request.urlopen(schedule_book)
workbook = load_workbook(logo)
