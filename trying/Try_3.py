from datetime import datetime, timedelta

#���������� ���� ����������� ��������
curtime = datetime.now()
lastime = (curtime - timedelta(days=3))

print(curtime.strftime("%d-%m-%Y  %H:%M"))
print(lastime.strftime("%d-%m-%Y  %H:%M"))
