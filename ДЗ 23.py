# from typing import List
#
# def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
#    for i, el in enumerate(nums1):
#        print(i, el)
#     for i, el in enumerate(muns2):
#         print(i, el)
#
#
# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)

nums1 = [6,2,10,12,5]
nums2 = [4,5,6,7,8]
for i, el in enumerate(nums1):
    print(i, el)
for i, el in enumerate(nums2):
    print(i, el)
intermediary = []
for el1,el2 in zip(nums1,nums2):
    if el2 > el1:
        intermediary.append(el2)

print(intermediary)
final = []
for i in intermediary:
    index = nums2.index(i)
    final.append(index)
print(final)

# Написать функцию get_indexes которая принимает два списка и возвращает список индексов,
# в которых элемент из первого списка меньше элемента из второго списка по данному индексу.
# Желательно проходиться сразу по двум массивам одновременно (вспомните функцию zip).
# Для нахождения индексов можно использовать enumerate вместе с zip.
# Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

# в итоге должен получиться список с индексами из двух списков

# может сделать наоборот? сначала сравнить списки, а потом уже искать индексы?
