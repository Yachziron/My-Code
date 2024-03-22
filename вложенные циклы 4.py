# number_of_kids = int(input())
# for i in range(number_of_kids):
#     name = input()
#     number = input()
x = "1,000,000"

def unique_list(my_list):
    x = []
    for a in my_list:
        if a not in x:
            x.append(a)
    return x

print(unique_list([13, 21, 19, 19, 2, 13]))