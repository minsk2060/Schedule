# # DO NOT DELETE THE COMMENTED PIECE !!!
# # This is for reading plants names from  excel
# from openpyxl import load_workbook
# schedule_book="./excel/Расписание.xlsm"
# workbook = load_workbook(schedule_book)
# plants={}
# for j in range(53, 383, 10):
#         plant_name = (str(workbook.active.cell(row=j, column=2).value))
#         plant_code = (str(workbook.active.cell(row=j, column=4).value))
#         plants[f"{plant_code}"] = plant_name
# for i in plants:
#         print(len(i),type(i),i,plants[i])
#
plant = {
        '79691777&did=33555432': 'ПВ-1.1 ',
        '79691782&did=33556432': 'ПВ-2.1 ',
        '8388619&did=33560432':  'ПВ-1.2 ',
        '8388864&did=33557432':  'ПВ-1.5 ',
        '8388871&did=33557432':  'ПВ-1.6 ',
        '8388858&did=33557432':  'ПВ-1.7 ',
        '8388708&did=33557432':  'П-1.8  ',
        '8388676&did=33559432':  'П-1.9  ',
        '8388704&did=33557432':  'П-1.10 ',
        '8388743&did=33559432':  'П-1.11 ',
        '8388762&did=33560432':  'ПВ-2.2 ',
        '8388822&did=33561432':  'ПВ-2.3 ',
        '8388808&did=33561432':  'ПВ-2.4 ',
        '8388778&did=33560432':  'ПВ-2.5 ',
        '8388770&did=33560432':  'ПВ-2.6 ',
        '8388827&did=33561432':  'ПВ-2.7 ',
        '8388835&did=33561432':  'ПВ-2.8 ',
        '8388815&did=33561432':  'ПВ-2.9 ',
        '8388788&did=33560432':  'ПВ-2.10',
        '8388739&did=33559432':  'ПВ-2.11',
        '8388750&did=33559432':  'ПВ-2.12',
        '8388757&did=33559432':  'ПВ-2.13',
        '8388795&did=33560432':  'ПВ-2.14',
        '8388845&did=33559432':  'ПВ-2.15',
        '8388650&did=33561432':  'П-2.18 ',
        '8388672&did=33559432':  'П-2.19 ',
        '8388654&did=33561432':  'П-2.20 ',
        '8388614&did=33560432':  'П-2.21 ',
        '8388902&did=33560432':  'П-2.23 ',
        '8388851&did=33559432':  'П-2.24 ',
        '79992777&did=33554453': 'В-1.9  ',
        '79993777&did=33554453': 'B-1.38 ',
        '8388883&did=33560432':  'Бассейн'
        }

alarm_A={ '79691777&did=33555432': 'ПВ-1.1 ',
        '79691782&did=33556432': 'ПВ-2.1 ',
        '12582981&did=33560432':  'ПВ-1.2 ',
        '12584064&did=33557432':  'ПВ-1.5 ',
        '12584092&did=33557432':  'ПВ-1.6 ',
        '12584036&did=33557432':  'ПВ-1.7 ',
        '12583436&did=33557432':  'П-1.8  ',
        '12583282&did=33559432':  'П-1.9  ',
        '12583415&did=33557432':  'П-1.10 ',
        '12583596&did=33559432':  'П-1.11 ',
        '12583680&did=33560432':  'ПВ-2.2 ',
        '12583904&did=33561432':  'ПВ-2.3 ',
        '12583848&did=33561432':  'ПВ-2.4 ',
        '12583736&did=33560432':  'ПВ-2.5 ',
        '12583708&did=33560432':  'ПВ-2.6 ',
        '12583960&did=33561432':  'ПВ-2.7 ',
        '12583932&did=33561432':  'ПВ-2.8 ',
        '12583876&did=33561432':  'ПВ-2.9 ',
        '12583764&did=33560432':  'ПВ-2.10',
        '12583575&did=33559432':  'ПВ-2.11',
        '12583624&did=33559432':  'ПВ-2.12',
        '12583652&did=33559432':  'ПВ-2.13',
        '12583792&did=33560432':  'ПВ-2.14',
        '12583988&did=33559432':  'ПВ-2.15',
        '12583142&did=33561432':  'П-2.18 ',
        '12583261&did=33559432':  'П-2.19 ',
        '12583163&did=33561432':  'П-2.20 ',
        '12582953&did=33560432':  'П-2.21 ',
        '8388902&did=33560432':  'П-2.23 ',
        '12584008&did=33559432':  'П-2.24 ',
        '21272522&did=33554453&vid=80': 'В-1.9.1  ',
        '7d9992777&did=33554453': 'В-1.9.2  ',
        '21273522&did=33554453&vid=80': 'B-1.38.1 ',
        '21273527&did=33554453&vid=80': 'B-1.38.2 ',
        '8388883&did=33560432':  'Бассейн'}

alarm_BC={ '79691777&did=33555432': 'ПВ-1.1 ',
        '79691782&did=33556432': 'ПВ-2.1 ',
        '8388619&did=33560432':  'ПВ-1.2 ',
        '8388864&did=33557432':  'ПВ-1.5 ',
        "":  'ПВ-1.6 ',
        "http://192.168.250.50/svo/details/?oid=12584037&did=33557432&vid=17":  'ПВ-1.7 ',
        '8388708&did=33557432':  'П-1.8  ',
        '8388676&did=33559432':  'П-1.9  ',
        '8388704&did=33557432':  'П-1.10 ',
        '8388743&did=33559432':  'П-1.11 ',
        '8388762&did=33560432':  'ПВ-2.2 ',
        '8388822&did=33561432':  'ПВ-2.3 ',
        '8388808&did=33561432':  'ПВ-2.4 ',
        '8388778&did=33560432':  'ПВ-2.5 ',
        '8388770&did=33560432':  'ПВ-2.6 ',
        '8388827&did=33561432':  'ПВ-2.7 ',
        '8388835&did=33561432':  'ПВ-2.8 ',
        '8388815&did=33561432':  'ПВ-2.9 ',
        '8388788&did=33560432':  'ПВ-2.10',
        '8388739&did=33559432':  'ПВ-2.11',
        '8388750&did=33559432':  'ПВ-2.12',
        'http://192.168.250.50/bac/details/update?oid=12583653&did=33559432&vid=17':  'ПВ-2.13', # класс В, С
        '8388795&did=33560432':  'ПВ-2.14',
        'http://192.168.250.50/bac/details/?oid=12583989&did=33559432&vid=17':  'ПВ-2.15',
        '8388650&did=33561432':  'П-2.18 ',
        '8388672&did=33559432':  'П-2.19 ',
        '8388654&did=33561432':  'П-2.20 ',
        '8388614&did=33560432':  'П-2.21 ',
        '8388902&did=33560432':  'П-2.23 ',
        'http://192.168.250.50/svo/details/?oid=12584009&did=33559432&vid=17&mode=cached':  'П-2.24 ',
        '79992777&did=33554453': 'В-1.9  ',
        '79993777&did=33554453': 'B-1.38 ',
        '8388883&did=33560432':  'Бассейн'}

#"http://192.168.250.50/alarms/active/group?group=bacnet.33560432.12583737"