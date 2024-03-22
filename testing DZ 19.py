def repeat_deco(n=1):
    def repeater(func):
        a = 1
        while a <= n:
            func()
            a += 1

    return repeater


@repeat_deco(6)
def hello():
    print("hello")


