def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

#В этом коде мы определяем декоратор repeat_deco, который принимает параметр
# n - число повторений. Декоратор возвращает функцию-обертку wrapper, которая
# вызывает декорированную функцию n раз и возвращает результат последнего вызова.
# Затем мы используем декоратор @repeat_deco(n=3) для декорирования функции my_func.
# При вызове my_func() она будет вызвана три раза, и результат последнего вызова будет возвращен.
