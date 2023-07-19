import pathlib
from pathlib import Path
path = "../logging/readlogs.txt"


plnt="ПВ-2.6"
f = open("../logging/readlogs.txt", "r")
s = []
a = f.read().split("\n")


for i in a:
#     print(i)
    if plnt in i:
        s.append(i)
prnt = "\n".join(s)
#
#
print(prnt)
#     s.append(i.split(" "))
#
#
# m = []
# for i in s:
#     if "ПВ-2.7" in i[0]:
#         m.append(i)
# a =[]
# print (m)
# for i in m:
#     print (i[7], type (i[7]))
#     a.append(" ".join(i[1:])+"\n")
#
# print("".join(a))