str1 = input()
str2 = input()
str3 = input()
b = []
for i in (str1, str2, str3):
    if "зайка" in i:
        b.append(i)
print(f"{min(b)} {len(min(b))}")