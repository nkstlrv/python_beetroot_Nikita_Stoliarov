# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

import calendar

day_names = list(calendar.day_name)
print("\n List of the week days -->", day_names)

week_list_1 = [[d+1, i] for d, i in enumerate(day_names)]

dict_1 = {}
dict_2 = {}

i_1 = 0
i_2 = 0

while len(week_list_1) > i_1:
    dict_1.update({week_list_1[i_1][0]: week_list_1[i_1][1]})
    i_1 += 1
print("\n Our first dict -->", dict_1)


while len(week_list_1) > i_2:
    dict_2.update({week_list_1[i_2][1]: week_list_1[i_2][0]})
    i_2 += 1
print("\n Our second dict -->", dict_2)


