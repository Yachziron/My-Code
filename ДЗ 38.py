import datetime

string_datetime = input()


def parse_time(s):
   dt_from_s = datetime.datetime.strptime(s, '%Y %m %d %H %M %S')
   delta = datetime.timedelta(days=1)
   final_dt = dt_from_s + delta
   return int(datetime.datetime.strftime(final_dt, '%d'))

print(parse_time(string_datetime))


# Написать функцию parse_time, которая принимает строку в качестве параметра,
# которая является временем формата “ГГГГ ММ ДД ЧЧ ММ СС” и
# парсит эту строку в объект datetime.datetime и сдвигает ее на один день вперед.
# вывод - количество дней +1