n = int(input())

if n == 1:
    print("NO")
for i in range(2, n):
    print(f"остаток от деления n на i {n % i}")
    print(i)
for i in range(1, n):
    if n % i != 0:
        answer = "YES"
    else:
        answer = "NO"
print(answer)

#проверить остатки от деления на все числа в ренжде от 1 до числа?
#отдельно обработать единицу?
# if n % i == 0:
#     answer = "NO"