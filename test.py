from calc import (add, subtract, multiply, divide, power, square_root)
import pytest 

# Тесты для операции сложение
def test_add_positive():
    assert add (2, 3) == 5

def test_add_negative():
    assert add (2, 3) == -5

def test_add_with_zero():
    assert add (0, 5) == 5

def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 5, 5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Тесты для операции вычитание
def test_subtract_positive():
    assert subtract (3, 1) == 2

def test_subtract_negative():
    assert subtract (7, 3) == -4

def test_subtract_with_zero():
    assert subtract (0, 4) == -4

def test_subtract_floats():
    assert subtract (3.4, 1.1) == 2.3

def test_subtract_with_negative_number():
    assert subtract (-3, -5) == 2

@pytest.mark.parametrize("a, b, expected", [
    (8, 3, 5),
    (-2, -3, 1),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

# Тесты для операции умножения
def test_multiply_positive():
    assert multiply (5, 2) == 10 

def test_multiply_negative():
    assert multiply (3, 7) == -21

def test_multiply_with_zero():
    assert multiply (12, 0) == 0

def test_multiply_floats():
    assert multiply (10.5, 3.2) == 33.6

def test_multiply_with_negative_number():
    assert multiply (32, -2) == -64

def test_multiply_with_negative_number2():
    assert multiply (-5, -5) == 25

# Тесты для операции деления
def test_divide_positive():
    assert divide (10, 2) == 5

def test_divide_negative():
    assert divide (6, 3) == -2

def test_divide_with_zero():
    assert divide (52, 0) == 0 # or Error

def test_divide_floats():
    assert divide (32.2, 2.2) == 14.63636363636364

def test_divide_with_negative_number():
    assert divide (-10, -5) == 2

# Тесты для операции возведения в степень
def test_power_positive():
    assert power (2, 2) == 4

def test_power_negative():
    assert power (2, 3) == 8

def test_power_with_zero():
    assert power (7, 0) == 1

def test_power_floats():
    assert power (9.3, 2) == 86.49

def test_power_with_negative_number():
    assert power (-10, 2) == 100

def test_power_with_negative_number2():
    assert power (-10, 3) == -1000

# Тест для операции квадратного корня
def test_sqrt_positive():
    assert square_root (4) == 2

def test_sqrt_negative():
    assert square_root (16) == -4

def test_sqrt_with_negative_number():
    assert square_root (-16) == 4

def test_sqrt_with_negative_number2():
    assert square_root(-16) == -4