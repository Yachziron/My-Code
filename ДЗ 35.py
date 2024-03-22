from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    specializations_dict = defaultdict(list)
    for specialization, name in specializations:
        specializations_dict[specialization].append(name)
    return dict(specializations_dict)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)


# Написать функцию fill_specializations, которая принимает список кортежей
# из специальности и имени и возвращает словарь, где в качестве ключей
# специальности, а в качестве значений - списки имен. Желательно,
# чтобы это было реализовано через словарь со значением по умолчанию.
