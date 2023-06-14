import datetime


#only_date = (datetime.today().toordinal())   # Здесь найдена только дата, когда он работает, нужно найти период
# # print(only_date)
delta_before = datetime.timedelta(days=0, hours=100)
delta_after  = datetime.timedelta(days=0, hours=8)
Voolfov_1 = datetime.datetime.fromordinal(datetime.datetime.today().toordinal()) - delta_before
Voolfov_2 = datetime.datetime.fromordinal(datetime.datetime.today().toordinal()) + delta_after


#print(datetime.datetime.now().toordinal()%4)
#print((datetime.datetime.now()+delta_before).toordinal()%4)

# Фамилия, резульат деления времени первой части смены и второй
# Вульфов  3, 0
# Клышко   0, 1
# Басыров  1, 2
# Федорчук 2, 3


dat = datetime.datetime(2023,06,22,12,30)
# a=738683
#
#print(datetime.datetime.fromordinal(only_date))
# Период это начало даты минус 16 часов и начало даты плюс 8 часов


# """
# 12.06.2023 - 738683
# Вульфов  -3
# Клышко
# Басыров
# Федорчук
# """