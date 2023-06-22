# Этот код сохранен для примера
# Раньше использовался для отправки запросов через окно браузера
# После перехода к библиотеке requests данный код стал не нужен
from pywinauto.application import Application
import webbrowser
import time
from pyautogui import hotkey

def browsing():
    """
    browsing()   - открытие и установка фокуса на окне браузера Edge
    app          - объект для подключения и установки фокуса на окне браузера Edge
    try          - проверка на предмет не закрыт ли браузер, открытие
    except       - открытие браузера, закрытие лишней страницы
    set_focus()  - вывод окна браузера на передний план
    """
    app =Application(backend ="uia")
    try:
        app.connect(title_re=u".*Microsoft\u200b Edge", timeout=10)
    except:
        app.start("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
        app.connect(title_re=u".*Microsoft\u200b Edge", timeout=10)
        webbrowser.open("http://192.168.250.50/svo/graphic?oid=121634830&did=-1&vid=80")
        time.sleep(3)
        hotkey("ctrl", "tab")
        hotkey("ctrl", "w")
        time.sleep(3)
    app.window().set_focus()

def sendrequesttowebbrowser(get_plant, par):
    """
    sendrequesttowebbrowser()  - отправка запроса путем вставки текста в адресную строку браузера
    get_plant                  - параметр для формирования url, определяющий код установки
    par                        - параметр для формирования url, определяющий действие ( 0 -стоп, 1 пуск и т.п.)
    time.sleep(3)              - задержка времени  для отправки запроса
    hotkey()                   - закрытие окна с запросом
    """
    webbrowser.open_new_tab("http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=" + get_plant + par)
    time.sleep(3)
    hotkey("ctrl", "w")

if __name__ == "__main__":
    browsing()
    sendrequesttowebbrowser("8388858&did=33557432", "0")
