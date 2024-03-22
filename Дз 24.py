def cache_deco(func):

    cache = {}

    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return inner

@cache_deco
def solution(func_map, func_filter, data):

    for line in data.splitlines():
        func_name, *args = line.split()
        if func_name not in func_filter:
            continue
        try:
            func = func_map[func_name]
        except KeyError:
            print("Unknown function:", func_name)
            continue
        for item in func_filter(data):
            yield func(item)

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)