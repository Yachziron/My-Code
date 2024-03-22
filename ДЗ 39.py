import collections
import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    a = []
    c = []
    for i in dates:
        dt_from_string = datetime.datetime.strptime(i, '%Y-%m-%dT%H:%M:%S')
        # print(type(dt_from_string))
        # print(dt_from_string)
        string_from_dt = int(datetime.datetime.strftime(dt_from_string, '%m'))
        # print(string_from_dt)
        a.append(string_from_dt)
    counter = collections.Counter(a)
    b = counter.most_common(n)
    # print(b)
    for el1, el2 in b:
        c.append(el1)
    # print(c)
    return c


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# Написать функцию most_common_months, которая принимает в качестве параметра список строк,
# которые являются датами формата “ГГГГ-ММ-ДДTЧЧ-ММ-СС” и некоторое целое число n,
# и выводит топ n самых частых месяцев этих дат. Желательно,
# чтобы это было реализовано через Counter из модуля collections.

# нужно найти самые частые месяца?? нужно сделать фильтрацию по месяцу
# как это сделать??? вытащить из даты месяц?
# строки превратить даты, потом обратно в дату, где только месяц

# dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
# print(most_common_months(dates, 2))

# [1, 2]
# вытащили название месяца, нужно теперь засунуть это в список и потом по списку пройтись
# мосткоммон
