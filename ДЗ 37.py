import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    delta = datetime.timedelta(days, seconds)
    initial_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    end_time = initial_time + delta
    string_from_end_time = datetime.datetime.strftime(end_time, '%d, %S')
    string_from_end_time = string_from_end_time.replace(" ", "")
    return tuple(int(item) for item in string_from_end_time.split(','))


print(shift_time(days, seconds))

# Написать функцию shift_time, которая принимает 2 параметра: количество дней
# и количество секунд и сдвигает дату и время 01.01.2023 12:30:00 на
# указанное количество дней и секунд. В качестве выходного значения нужно
# вывести кортеж: день и секунда от сдвинутого времени.


# перевести дейтайм в строку?
