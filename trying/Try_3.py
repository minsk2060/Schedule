import pathlib
from pathlib import Path
path = "C:/Users/milli/Documents/Programming/Python/Projects/schedules/logging/readlogs.txt"

f = open(path, "r")
s=[]
for i in f.read().replace("     ", " ").split("\n"):
    s.append(i.split(" "))

m = []
for i in s:
    if "ПВ-2.4" in i[0]:
        m.append(i)
a =[]
for i in m:
    a.append(" ".join(i[1:])+"\n")
print("".join(a))