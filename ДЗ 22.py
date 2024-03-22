from typing import List, Dict

#
# def make_most_common_keys(d: Dict[int, int]) -> List[int]:
#    return sorted(d, reverse = True)
#
#
# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)

#сортировка по значениям
# d =  {5:3, 3:5, 0:2, 4:6, 7:10}
dsort = sorted(d.values(), reverse=True)
def get_key(d, value):
    endlist = []
    for i in dsort:
        value = i
        for k, v in d.items():
            if v == value:
                endlist.append(v)
    return(endlist)
print(get_key(d, dsort))


# def get_key(d, value):
#     for k, v in d.items():
#         if v == value:
#             return k
#
# print(get_key(d,5))

#сортируем по значениям, выводим ключи
#мы можем найти ключ по значению, значит делаем сортировку по значению
#потом для листа из значений выводим соответствующеие ключи через for