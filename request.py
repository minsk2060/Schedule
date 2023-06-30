import datetime
import time
import requests
from headers import header, header_alarm_A
from plants import alarms_A, alarms_BC
from excels import writestatus
from tokens import sauter_cookie
import webbrowser
#  В данном скрипте выполняется успешная отправка запроса (пуск ПВ-2.9) не прибегая к библиотеке webbrowser

def switch(get_plant, par):
    """
    switch()     - выполнение запроса на сервер при помощи библиотеки requests
    get_plant    - параметр для формирования url, определяющий код установки
    par          - параметр для формирования url, определяющий действие
    headers      - заголовки запроса
    cookies      - ключи
    """
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={get_plant}{par}"
    r = requests.get(url, headers=header, cookies=sauter_cookie)


def getalarms(alarms_dict, column_number, alarm_text):
    """
    getalarms()   - получение данных о наличии аварии установки в данный момент
    alarms_dict   - словарь с кодами установок для формирования строки запроса
    alarm_now     - текст записи о наличии-отсутствии аварии
    writestatus() - запись сведений об аварии в Состояние.xlsx
    """
    for i, j in enumerate(alarms_dict.keys()):
        time.sleep(10)
        url=f"http://192.168.250.50/svo/details/update?oid={j}&vid=17&mode=cached"
        r=requests.get(url, headers=header_alarm_A, cookies=sauter_cookie, allow_redirects=False)
        if "Alarm: true" in r.text and "False: true" not in r.text:
            alarms_now = alarm_text
        elif "Alarm: false" in r.text:
            alarms_now = "Авария снята"
        else:
            alarms_now = "Нет ответа об аварии"
        writestatus(i, alarms_dict[j], alarms_now, column_number)


if __name__ == "__main__":
    getalarms(alarms_dict=alarms_A, column_number=4, alarm_text='Авария класса А')
    getalarms(alarms_dict=alarms_BC, column_number=5, alarm_text='Авария класса B,C')



"""
{'data': {   '79': ['Binary Input', ''], 
             '114': ['*', ''],
             '77': ['PV1.7_DIA184', ''],
             '115': ['*', ''],
             '113': ['0', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=113&oid=12584036&did=33557432&vid=17">Edit</a>'],
             '111': ['<span class="icon-status icon-statusflag-0-grey " title="Alarm: true"></span> <span class="icon-status icon-statusflag-1-grey  ui-state-disabled" title="Fault: false"></span> <span class="icon-status icon-statusflag-2-grey  ui-state-disabled" title="Overridden: false"></span> <span class="icon-status icon-statusflag-3-grey  ui-state-disabled" title="Out of service: false"></span> ', ''],
             '35': ['<span class="icon-status icon-transition-0-grey " title="To Off-normal: true"></span> <span class="icon-status icon-transition-1-grey  ui-state-disabled" title="To Fault: false"></span> <span class="icon-status icon-transition-2-grey  ui-state-disabled" title="To Normal: false"></span> ', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=35&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '17': ['2', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=17&oid=12584036&did=33557432&vid=17">Edit</a>'],
             '36': ['Off-normal', ''], 
             '33': ['3680502', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=33&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '15': ['293', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=15&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '16': ['22.05.2023 16:29:46', ''], 
             '8263': ['-', ''], 
             '103': ['No fault detected', '<a class ="editbutton  disabled " href="/ajaxjson/bac/getEditOptions?pid=103&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '81': ['false', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=81&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '130': ['<div style="white-space:nowrap;margin-top:4px;"><span class="icon-status icon-transition-0-grey " title="To Off-normal"></span>  <span style="white-space:nowrap;">22.05.2023 16:29:46</span></div><div style="white-space:nowrap;margin-top:4px;"><span class="icon-status icon-transition-1-grey " title="To Fault"></span>  <span style="white-space:nowrap;">-</span></div><div style="white-space:nowrap;margin-top:4px;"><span class="icon-status icon-transition-2-grey " title="To Normal"></span>  <span style="white-space:nowrap;">-</span></div>', ''], 
             '84': ['0', ''], '8264': ['-', ''], '85': ['ДА <span class="text-right "></span>', '<a class ="editbutton  disabled " href="/ajaxjson/bac/getEditOptions?pid=85&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '46': ['НЕТ', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=46&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '371': ['-', ''], '28': ['Общая авария: A', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=28&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '168': ['17-XL_WEB_BI', ''], 
             '351': ['-', ''], 
             '353': ['-', ''], 
             '352': ['-', ''], 
             '355': ['-', ''], 
             '0': ['<span class="icon-status icon-transition-0-grey  ui-state-disabled" title="To Off-normal: false"></span> <span class="icon-status icon-transition-1-grey " title="To Fault: true"></span> <span class="icon-status icon-transition-2-grey " title="To Normal: true"></span> ', ''], 
             '354': ['-', ''], '6': ['ДА', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=6&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '356': ['-', '<a class ="editbutton  disabled " href="/ajaxjson/bac/getEditOptions?pid=356&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '31': ['-', ''], '4': ['ДА', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=4&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '72': ['Alarm', '<a class ="editbutton " href="/ajaxjson/bac/getEditOptions?pid=72&oid=12584036&did=33557432&vid=17">Edit</a>'], 
             '75': ['Binary Input 1124', '']}, 'fields': ['property-value', 'property-edit']}

"""