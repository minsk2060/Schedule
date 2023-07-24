<!DOCTYPE html>
<html>
<head>
</head>
<body>
<p>Наименование проекта: <br>Schedules</p>
<p>Цель проекта: <br> Автоматизизация работы оборудования по расписанию. <br>
Управление из мессенджеров.</p>
<p>Описание:<br>
Оборудование уже работает под контролем стороннего веб-приложения Sauter ModuWebVision.<br>
Управление оборудованием изначально выполнялось из этого приложения в ручном режиме.<br>
В проекте реализуется возможность управления обрудованием автоматически <br>
в определенное время по заданному расписанию.<br>
Расписание задается в файле формата excel (применен встроенный язык VBA).<br>
Выполняется периодическое чтение из этого файла и формирование запроса.<br>
Затем выполеняется отправка запроса на сервер Sauter в заданное время.<br>
Предусматривается логгирование работы оборудования с записью в текстовый файл.<br>
Предусматривается отправка сообщений об аварии оборудования в мессенджеры Telegram и Viber.<br>
Предусматривается возможность управлять оборудованием из мессенджера Telegram. <br> 
</p>
<p>Файлы и папки:<br>
<table style = "border: none;">
<tr>
    <td>adding/</td>    
    <td colspan="2">- сторонные файлы для корректной работы проекта на устройстве:</td>
</tr>
<tr>
    <td></td>
    <td>1251.zip</td>
    <td>- комплект для корректного отображения русского текста в скриптах VBA</td>
</tr>
<tr>
    <td>excel/</td>
    <td colspan="2">- файлы формата excel:</td>
</tr>
<tr>
    <td></td>
    <td>Расписание.xlsm</td>
    <td>- пользовательский файл, в котором задается расписание</td>
</tr>
<tr>
    <td></td>
    <td>Состояние.xlsx</td>
    <td>- пользовательский файл, в который выполняются записи об авариях</td>
</tr>

<tr>
    <td>logging/</td>
    <td colspan="2">- файлы логов формата txt:</td>
</tr>
<tr>
</tr>
    <td></td>
    <td>alllogs</td>
    <td>- отправленные на сервер последние действия, но за более длительный период</td>
<tr>
</tr>
<tr>
    <td></td>
    <td>bug_1,bug_2,...</td>
    <td>- нетиповые ошибки в ходе работы над проектом и методы их решения</td>
</tr>
    <td></td>
    <td>log_scheduling</td>
    <td>- отправленные на сервер последние действия в пользовательском виде</td>
<tr>
</tr>
    <td></td>
    <td>readlogs</td>
    <td>- задания, прочитанные из excel</td>
<tr>
</tr>
    <td></td>
    <td>readme_xl</td>
    <td>- краткое пояснение пользователю для работы файлом Расписание.xlsm</td>
<tr>
</tr>
    <td></td>
    <td>steps_py</td>
    <td>- текущие задачи для решения в python</td>
<tr>
</tr>
<tr>
    <td></td>
    <td>steps_xl</td>
    <td>- текущие задачи для решения в excel</td>
</tr>
<tr>
    <td>tlegram/</td>
    <td colspan="2">- файлы для работы с мессенджером Telegram:</td>
</tr>
<tr>
    <td></td>
    <td>bug_6.txt, bug_7.txt</td>
    <td>- баги, встретившиеся в работе с Telegram</td>
</tr>
<tr>
    <td></td>
    <td>checkBot.py</td>
    <td>- реализация бесперебойной работы бота</td>
</tr>
<tr>
    <td></td>
    <td>ExampleBot.py</td>
    <td>- рабочий бот для примера</td>
</tr>
<tr>
    <td></td>
    <td>logobot.txt</td>
    <td>- логгирование автоматического перезапуска бота в случае падения</td>
</tr>
<tr>
    <td></td>
    <td>runBot.py</td>
    <td>- запуск бота в отдельном процессе</td>
</tr>
<tr>
<tr>
    <td></td>
    <td>steps.txt</td>
    <td>- текущие задачи для решения по работе с Telegram</td>
</tr>

<tr>
    <td></td>
    <td>TelegramBotAlarms.py</td>
    <td>- бот для рассылки сообщений об аварии оборудования</td>
</tr>
<tr>
    <td></td>
    <td>TelegramBotHalls.py</td>
    <td>- бот для управления вентиляцией залов</td>
</tr>


<tr>
    <td>trying/</td>
    <td colspan="2">- пробные сценариии</td>
</tr>
<tr>
    <td>viber/</td>
    <td colspan="2">- файлы для работы с мессенджером Viber:</td>
</tr>
<tr>
    <td></td>
    <td>ViberBot.py</td>
    <td>- бот для рассылки сообщений об авари оборудования</td>
</tr>
<tr>
    <td></td>
    <td>ViberSet.py</td>
    <td>- настройки для запуска webhook</td>
</tr>

<tr>
    <td>excels.py</td>
    <td colspan="2">- работа с excel (лучше не читать, там черт ногу сломит)</td>
</tr>
<tr>
    <td>Schedule.py</td>
    <td colspan="2">- основная логика</td>
</tr>
<tr>
    <td>plants.py</td>
    <td colspan="2">- перечни оборудования и кодов</td>
</tr>
<tr>
    <td>logs.py</td>
    <td colspan="2">- логгирование действий с оборудованием</td>
</tr>
<tr>
    <td>request.py</td>
    <td colspan="2">- формирование и выполнение запросов</td>
</tr>

<tr>
    <td>headers.py</td>
    <td colspan="2">- заголовки запросов</td>
</tr>
<tr>
    <td>.gitignore</td>
    <td colspan="2">- перечень файлов с конфидентными данными</td>
</tr>

</table>

<p>Библиотеки:<br>
<table style = "border: none;">
<tr>
    <td>openpyxl</td>    
    <td colspan="2">- работа с файлами формата excel</td>
</tr>
<tr>
    <td>datetime,  &nbsp time &nbsp</td>    
    <td colspan="2">- работа с датой, временем</td>
</tr>
<tr>
    <td>schedule</td>    
    <td colspan="2">- выполнение функций по расписанию в назначенное время</td>
</tr>
<tr>
    <td>pywinauto</td>    
    <td colspan="2">- работа с приложением Notepad</td>
</tr>
<tr>
    <td>telebot</td>    
    <td colspan="2">- работа с мессенджером Telegram</td>
</tr>
<tr>
    <td>viberbot</td>    
    <td colspan="2">- работа с мессенджером Viber</td>
</tr>
<tr>
    <td>requests</td>    
    <td colspan="2">- выполнение http запросов</td>
</tr>
<tr>
    <td>psutil</td>    
    <td colspan="2">- сканирование системных процессов</td>
</tr>
<tr>
    <td>subprocess</td>    
    <td colspan="2">- запуск системных процессов </td>
</tr>

<tr>
    <td>flask</td>    
    <td colspan="2">- создание web сервера (частично необходим для работы с Viber)
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
</td>
</tr>


</table>

</body>

</html>