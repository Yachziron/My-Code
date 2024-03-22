def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before func call")
        tmp = func(*args, **kwargs)
        print("After func call")
        return tmp
    return wrapper

@my_decorator
def phone(model, charge=100, storage="128 Gb", status="Working"):
    if not 0 <= charge <= 100:
        print("Incorrect charge data!")
        return
    print(
        f"This {model} is {charge} percent charged. "
        f"It has {storage} of storage, current status is '{status}'."
    )

phone("iPhone")
