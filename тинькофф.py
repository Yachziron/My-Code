vvod = input()
a = vvod.split()
d = {}
for i in a:
    d[i] = len(i)
f = max(d.values())
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
print(get_key(d, f))
print(f)
