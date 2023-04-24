from datetime import datetime
from plants import plant

def logging(get_plant, par):
    current_time = datetime.now()
    plant_log = get_plant.replace(" ", "")
    print(current_time.strftime("%d.%m.%Y  %H:%M "), plant[f"{plant_log}"], acting(plant_log, par))
def acting (plant_log, par):

    action = ""
    # If other plants
    if par[-1:] == "1":
        action = " Пуск на низкой скорости"
    elif par[-1:] == "2":
        action = " Пуск на высокой скорости"
    elif par[-1:] == "0":
        action = " Cтоп"

    # If swimming pool
    if plant_log == "8388883&did=33560432":
        if par[-1:] == "0":
            action = " Выключение подсветки"
        elif par[-1:] == "2":
            action = " Включение желтой подсветки"
        elif par[-1:] == "1":
            action = " Включение синей подсветки"

    # If dryers
    elif plant_log == "79691782&did=33556432" or plant_log == "79691777&did=33555432":
        if par[-1:] == "5":
            action = " Стоп"
        elif par[-1:] == "1":
            action = " Пуск в режиме хоккей"
        elif par[-1:] == "2":
            action = " Пуск в режиме фигурное катание"
    return action
