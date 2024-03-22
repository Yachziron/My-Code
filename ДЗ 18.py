def cache_deco(func):
    """Cache decorator."""

    cache = {}

    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]

    return inner


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# нужно создать словарь, назови его кэш, он будет нужен для проверки
# сделай сам декоратор, внутри условие проверки для функции

#  Напишите декоратор, который будет кэшировать вызовы
#  функции, которая будет передана на вход. То есть
#  декоратор должен проверить нет ли в кэше (например, словаре)
#  значения, и если нет, то вычислить и запомнить результат,
#  если есть, то взять это значение. Дополните код ниже,
#  дописав свой код в секции “YOUR CODE HERE”.
