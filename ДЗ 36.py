from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
	final = []
	for el1, el2 in zip_longest(values_list_1, values_list_2):
		if el1 == None:
			el1 = 1
		if el2 == None:
			el2 = 1
		x = (el1, el2)
		final.append(x)
	return final

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# Написать функцию fill_missing_values, которая принимает два списка int-ов
# и делает из них один список кортежей, где в качестве элементов кортежа
# элементы списков на одинаковых позициях. Если один из список закончился,
# то в нужно заполнить значение в кортеже единицей.
# l1 = [1,2,3]
#
# l2 = [4,5,6,7,8]
#
# for el1, el2 in zip_longest(l1, l2):
# 	if el1 == None:
# 		el1 = 1
# 	if el2 == None:
# 		el2 = 1
# 	x = (el1, el2)
# 	final.append(x)
# print(final)


