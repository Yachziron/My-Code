from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    intermediary = []
    final = []
    for el1, el2 in zip(nums1, nums2):
        if el2 > el1:
            intermediary.append(el2)
    for i in intermediary:
        index = nums2.index(i)
        final.append(index)
    return final

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)