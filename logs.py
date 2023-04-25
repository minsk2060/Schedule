from datetime import datetime
from plants import plant

def logging(get_plant, par):
    current_time = datetime.now()
    plant_log = get_plant.replace(" ", "")
    f = open("./logging/log_scheduling.txt", "a")
    log = (current_time.strftime("%d.%m.%Y  %H:%M  "), plant[f"{plant_log}"], acting(plant_log, par))
    f.write(f"{''.join(log)}\n")
    f.close()

def acting (plant_log, par):
    action = ""
    a = par[-1:]
    # If other plants
    if a == "1":   action = "  Пуск на низкой скорости"
    elif a == "2": action = "  Пуск на высокой скорости"
    elif a == "0": action = "  Cтоп"
    # If swimming pool
    if plant_log == "8388883&did=33560432":
        if a == "0":   action = "  Выключение подсветки"
        elif a == "2": action = "  Включение желтой подсветки"
        elif a == "1": action = "  Включение синей подсветки"
    # If dryers
    elif plant_log == "79691782&did=33556432" or plant_log == "79691777&did=33555432":
        if a == "5":   action = "  Стоп"
        elif a == "1": action = "  Пуск в режиме хоккей"
        elif a == "2": action = "  Пуск в режиме фигурное катание"
    return action
