# В классе Calculator создайте метод calculate_discount,
# который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - протестировать этот метод с помощью assert в Python.
# Если метод calculate_discount получает некорректные аргументы, он должен выбросить исключение.

class Calculator:
    def calculate_discount(self, purchase_amount, discount_percentage):
        if not isinstance(purchase_amount, (int, float)) or not isinstance(discount_percentage, (int, float)):
            raise ValueError("Неверный ввод: purchase_amount и discount_percentage должны быть числами")

        if purchase_amount < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError(
                "Неверный ввод: purchase_amount должна быть неотрицательной, а iscount_percentage должен быть от 0 до 100")

        discount_amount = purchase_amount * (discount_percentage / 100)
        discounted_price = purchase_amount - discount_amount
        return discounted_price


def test_calculate_discount_valid_inputs():
    calculator = Calculator()
    assert calculator.calculate_discount(100, 10) == 90.0
    assert calculator.calculate_discount(50.5, 25) == 37.875


def test_calculate_discount_invalid_inputs():
    calculator = Calculator()
    try:
        calculator.calculate_discount("invalid", 10)
    except ValueError:
        assert "Неверный ввод: purchase_amount и discount_percentage должны быть числами"

    try:
        calculator.calculate_discount(100, -10)
    except ValueError:
        assert "Неверный ввод: purchase_amount должна быть неотрицательной, а discount_percentage должен быть от 0 до 100"

    try:
        calculator.calculate_discount(100, 110)
    except ValueError:
        assert "Неверный ввод: purchase_amount должна быть неотрицательной, а discount_percentage должен быть от 0 до 100"


if __name__ == "__main__":
    test_calculate_discount_valid_inputs()
    test_calculate_discount_invalid_inputs()
    print("Все тесты пройдены успешно!")
