import datetime
def onduties():
    """������� ��������������� ����������� ��� ������� �� ����� � �����������."""
    dat = datetime.datetime().now() # ���������� ����������� ����
    d = dat.toordinal() % 4         # ����� ���������� ����� ���� � ����� ������� �� ������� �� 4
    if datetime.time(8, 00) < dat.time() < datetime.time(23, 59): # ���������� ������ ������ ����� ����� (8:00...0:00)
        # �������, ��������� ������� ��� ������ ����� ����� � ������
        # ����       0, 1
        # ���������  1, 2
        # ������     2, 3
        # ���        3, 0
        if d == 0:
            onduty = "Zhenia"
        elif d == 1:
            onduty = "Alexandr"
        elif d == 2:
            onduty = "Nikita"
        elif d == 3:
            onduty = "Yura"
    elif datetime.time(0, 00) < dat.time() < datetime.time(8, 00): # ���������� ������ ������ ����� ����� 0:00...8:00
        if d == 0:
            onduty = "Yura"
        elif d == 1:
            onduty = "Zhenia"
        elif d == 2:
            onduty = "Alexandr"
        elif d == 3:
            onduty = "Nikita"

    return onduty
