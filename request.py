import requests

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
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Connection": "keep-alive",
        "Host": "192.168.250.50",
        "Referer": "http://192.168.250.50/svo/graphic?oid=121634830&did=-1&vid=80",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42",
        "X-Requested-With": "XMLHttpRequest"
        }

    cookies = {
        "JSESSIONID":     "13reb3vcok495lblc0opr7kkg",
        "pw":             "73F0CF35AF3850221A1D641803815D686EC21A9316F6CFBFF079AE3B9BFE8DEA",
        "BAYEUX_BROWSER": "ec3egd91iy8tb3mjlhulodl01any",
        "uid":            "0"
                }

    r = requests.get(url, headers=headers, cookies=cookies)

if __name__ == "__main__":
    switch("8388815&did=33561432", "&vid=17&value=1")