f = open("PV26.txt", "r")
r = f.read()
n = r[r.index('<tr data-pid="85">')+18:]
e = n[:n.index('</tr>')]
g = int(e[e.index("property-value")+16])
if g == 5:
    print ("Работает на высокой скорости")
elif g == 0:
    print()
f.close()
