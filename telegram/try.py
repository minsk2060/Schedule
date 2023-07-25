from plants import alarms_A, alarms_BC

all_plants = {"ПВ-2.4": "8388808&did=33561432",
              "ПВ-2.5": "8388778&did=33560432",
              "ПВ-2.6": "8388770&did=33560432",
              "ПВ-2.7": "8388835&did=33561432",
              "ПВ-2.8": "8388827&did=33561432",
              }


rev_alarms_BC = {v[:6]:k for k,v in alarms_BC.items() if v[:6] in all_plants.keys()}
rev_alarms_A = {v[:6]:k for k,v in alarms_A.items() if v[:6] in all_plants.keys()}


for k, v in rev_alarms_BC.items():
    print (k,v)

for k, v in rev_alarms_A.items():
    print (k,v)

"""
ПВ-2.4 12583849&did=33561432
ПВ-2.4 12583848&did=33561432

ПВ-2.5 12583737&did=33560432
ПВ-2.5 12583736&did=33560432

ПВ-2.6 12583709&did=33560432
ПВ-2.6 12583708&did=33560432

ПВ-2.7 12583961&did=33561432
ПВ-2.7 12583960&did=33561432

ПВ-2.8 12583933&did=33561432
ПВ-2.8 12583932&did=33561432
"""