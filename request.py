import datetime
import time
import requests
from headers import header, header_alarm_A, cookie
from plants import alarms_A
from excels import writestatus
#  В данном скрипте выполняется успешная отправка запроса (пуск ПВ-2.9) не прибегая к библиотеке webbrowser

def switch(get_plant,par):
    """
    switch()     - выполнение запроса на сервер при помощи requests

    get_plant    - параметр для формирования url, определяющий код установки
    par          - параметр для формирования url, определяющий действие
    headers      - заголовки запроса
    cookies      - ключи
    """
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={get_plant}{par}"
    r = requests.get(url, headers=header, cookies=cookie)

def getalarms():
    alarms_A_list={}
    for i in range(len(alarms_A.keys())):
        time.sleep(10)
        url=f"http://192.168.250.50/svo/details/update?oid={i}&vid=17&mode=cached"
        r=requests.get(url, headers=header_alarm_A, cookies=cookie, allow_redirects=False)
        if "Alarm: true" in r.text:
            alarms_now="Авария класса А"
        elif "Alarm: false" in r.text:
            alarms_now="Нет аварии"
        writestatus(i,alarms_A.keys()[i], alarms_now)


            # # time.sleep(3)
            # print(r.status_code)
            # print(r.text)
            # # if "Alarm: true" in r.text:
            #     print(f"{j}  in alarm")
            # elif "Alarm: false" in r.text:
            #     print("Alarm false")
            # else :
            #     print ("No alarms detected!")

if __name__ == "__main__":
    # switch('8388858&did=33557432', "&vid=17&value=1")
    # url="http://192.168.250.50/svo/details/?oid=12584036&did=33557432&vid=17"
    # url ="http://192.168.250.50/bac/details/update?oid=12584036&did=33557432&vid=17" # ПВ-1.7
    # url2="http://192.168.250.50/bac/details/update?oid=12584092&did=33557432&vid=17" # ПВ-1.6
    # alarm = "Alarm: true"
    #r = requests.get(url, headers=header, cookies=cookie)
    # print(r.json()["data"]["111"])
    # print(r.json()["data"]["111"][0])
    # if "Alarm: true" in r.json()["data"]["111"][0]:
    #     print("Alarm true")
    # elif "Alarm: false" in r.json()["data"]["111"][0]:
    #     print("Alarm false")
    # else:
    #     print("No data detected")
    # else:
    #     print("Alarm: False")
    getalarms()
    # for i,j in alarms_try.items():
    #     print (i,j)
    # writestatus()

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