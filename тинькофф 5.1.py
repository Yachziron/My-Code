import math
def find_logo_position(n, m):
    # Находим НОД (наибольший общий делитель) ширины и высоты экрана
    gcd_value = math.gcd(n, m)

    # Если НОД равен 1, логотип никогда не попадет в угол
    if gcd_value == 1:
        return 0
    else:
        # Определяем, в какой угол попадет логотип
        if (n // gcd_value) % 2 == 0:
            if (m // gcd_value) % 2 == 0:
                return 4  # Правый нижний угол
            else:
                return 3  # Левый нижний угол
        else:
            if (m // gcd_value) % 2 == 0:
                return 2  # Правый верхний угол
            else:
                return 1  # Левый верхний угол


# Ввод данных
n, m = map(int, input().split())

# Вычисление и вывод результата
result = find_logo_position(n, m)
print(result)
