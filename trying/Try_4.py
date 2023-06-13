import datetime


#only_date = (datetime.today().toordinal())   # Здесь найдена только дата, когда он работает, нужно найти период
# # print(only_date)
delta_before = datetime.timedelta(days=0, hours=16)
delta_after  = datetime.timedelta(days=0, hours=8)
Voolfov_1 = datetime.datetime.fromordinal(datetime.datetime.today().toordinal()) - delta_before
Voolfov_2 = datetime.datetime.fromordinal(datetime.datetime.today().toordinal()) + delta_after

print(Voolfov_1)
print(Voolfov_2)

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