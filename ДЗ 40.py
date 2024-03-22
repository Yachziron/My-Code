import collections
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    deq = collections.deque(nums)
    n_range = range(n)
    for i in n_range:
        # print(deq)
        a = deq.pop()
        # print(deq)
        deq.appendleft(a)
        # print(deq)
    return list(deq)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#
# Написать функцию rotate_list, которая принимает список целых чисел и целое число,
# которое будет задавать, сколько крутить список. Под кручением
# списка подразумевается забор элемента из конца списка и
# вставка его в начало списка. Желательно, чтобы это было реализовано через двустороннюю очередь.


# вход print(rotate_list([1,2,3,4], 1))
# выход [4, 1, 2, 3]
