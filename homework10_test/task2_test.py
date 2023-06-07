# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0, 5)


@pytest.mark.smoke
def test_two_numbers():
    assert all_division(6, 3) == 2, 'Неверный результат деления двух чисел'


def test_division_five_numbers():
    assert all_division(1000, 100, 10, 2, 1) == 0.5, 'Неверный результат деления пяти чисел'


def test_lower_zero_numbers():
    assert all_division(10, -5) == -2, 'Неверный результат деления положительного числа на отрицательное'


def test_lower_zero_numbers2():
    assert all_division(-10, -5) == 2, 'Неверный результат деления двух отрицательных чисел'
