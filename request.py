import time
import requests
from headers import header, header_alarm_A, sauter_cookie
from plants import alarms_A, alarms_BC
from excels import writestatus
#from tokens import sauter_cookie

def switch(get_plant, par):
    """
    switch()     - выполнение запроса (пуск/стоп) при помощи библиотеки requests
    get_plant    - параметр для формирования url, определяющий код установки
    par          - параметр для формирования url, определяющий действие
    headers      - заголовки запроса
    cookies      - ключи
    """
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={get_plant}{par}"
    r = requests.get(url, headers=header, cookies=sauter_cookie)


def getalarms(alarms_dict, column_number, alarm_text):
    """
    getalarms()   - выполнение запроса о наличии аварии установки в данный момент
    alarms_dict   - словарь с кодами установок для формирования строки запроса
    alarm_now     - текст записи о наличии/отсутствии аварии
    writestatus() - запись сведений об аварии в Состояние.xlsx
    """
    for i, j in enumerate(alarms_dict.keys()):
        time.sleep(10)
        url=f"http://192.168.250.50/svo/details/update?oid={j}&vid=17&mode=cached"
        r=requests.get(url, headers=header_alarm_A, cookies=sauter_cookie, allow_redirects=False)
        alarms_now = "Авария снята"
        if r.text:
            if "Alarm: true" in r.text:
                if 'title="Fault: true"' not in r.text:
                    alarms_now = alarm_text
            # elif "Alarm: false" in r.text:
            # else:
            #     alarms_now = "Авария снята"
        # else:
        #     alarms_now = "Нет ответа об аварии"
        writestatus(i, alarms_dict[j], alarms_now, column_number)


if __name__ == "__main__":
    g = "8388808&did=33561432"
    p = "&vid=17&value=1"
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={g}{p}"
    r = requests.get(url, headers=header, cookies=sauter_cookie)
    print(r.text)
    # getalarms(alarms_dict=alarms_A, column_number=4, alarm_text='Авария класса А')
    # getalarms(alarms_dict=alarms_BC, column_number=5, alarm_text='Авария класса B,C')

