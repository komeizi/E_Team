import json
import pprint

def kcal_sorted(kcal_list: list) -> None:
    return_list = []
    sorted_list = sorted(kcal_list, key=lambda x: x['kcal'], reverse=True)
    for i in sorted_list:
        e = {"name":i["name"],"kcal":i["kcal"]}
        return_list.append(e)
    d = {"kcal_ranking": return_list}
    with open('test1.json', 'w') as f:
        json.dump(d, f, indent=4)
    #return return_list

def step_sorted(step_list: list) -> None:
    return_list = []
    sorted_list = sorted(step_list, key=lambda x: x['step'], reverse=True)
    for i in sorted_list:
        e = {"name":i["name"],"step":i["step"]}
        return_list.append(e)
    d = {"step_ranking": return_list}
    with open('test2.json', 'w') as f:
        json.dump(d, f, indent=4)
    #return None

def month_select(month_list: list, m: int) -> list:
    return_list = []
    selected_M = [k for k in month_list if k["month"] == m]
    return selected_M

def day_month_select(month_list: list, m: int, d: int) -> list:
    return_list = []
    selected_D = [k for k in month_list if k["month"] == m and k["day"] == d]
    return selected_D

def dict2json(date: list) -> list:
    return_dict = {krank:date}


test = [{"name": 1, "year":2022, "month": 3, "day": 4,"kcal": 166, "step": 42},
        {"name": 7777, "year":2023, "month": 5, "day": 7,"kcal": 126, "step": 422},
        {"name": 771, "year":2021,"month": 9, "day": 7,"kcal": 1260, "step": 4},
        {"name": 3, "year":2022, "month": 5, "day": 7,"kcal": 1663, "step": 424}]


#mselect = month_select(test,5)
#dselect = day_month_select(test,5,7)
#krank = kcal_sorted(test)
#srank = step_sorted(test)
kcal_sorted(test)
step_sorted(test)

#deback========================
"""
print("月")
pprint.pprint(dselect)
pprint.pprint(kcal_sorted(mselect))
print("月日")
pprint.pprint(mselect)
pprint.pprint(kcal_sorted(mselect))
print("kcal")
pprint.pprint(krank)
print("step")
pprint.pprint(srank)
"""
#==============================
"""
with open('test2.json', 'w') as f:
    json.dump(d, f, indent=4)
"""