import datetime

r = open("../logging/alllogs.txt","r")
cur = r.read().split("\n")
r.close()
for i in range(len(cur)-1):
    if datetime.datetime.now()-datetime.timedelta(days=2) < (datetime.datetime.strptime(cur[i][:17], "%d-%m-%Y  %H:%M")):
                                                                                               "%d-%m-%Y  %H:%M"):
        print("ok")
    else:
        print("er")
# str_date = "14-05-2023  09:40"
# print(datetime.datetime.today().date())
# print(datetime.datetime.strptime(str_date, "%d-%m-%Y  %H:%M"))









