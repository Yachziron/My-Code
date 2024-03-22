first_list = input()
first_list = first_list.split()
first_int = []
for i in first_list:
    first_int.append(int(i))
second_list = input()
second_list = second_list.split()
second_int = []
for i in second_list:
    second_int.append(int(i))
for i in first_int:
    if i not in second_int:
        check1 = "NO"
        break
    else:
        check1 = "YES"
for i in second_int:
    if i not in first_int:
        check2 = "NO"
        break
    else:
        check2 = "YES"
if check1 == "YES" and check2 == "YES":
    print("YES")
else:
    print("NO")