import pytest
from tasks.pair_class import Pair, make_pair


class TestPair:
    def test_creation_valid(self):
        """Тестирование правильного создания пары"""
        pair = Pair(1, 5)
        assert pair.first == 1
        assert pair.second == 5

    def test_creation_invalid(self):
        """Тестирование на создание недопустимой пары чисел"""
        with pytest.raises(ValueError, match="Первое число должно быть меньше второго"):
            Pair(5, 1)

    def test_rangecheck_inside(self):
        """Тестирование диапазона с числом внутри диапазона"""
        pair = Pair(1, 5)
        assert pair.rangecheck(3) is True

    def test_rangecheck_lower_bound(self):
        """Тестирование диапазона с числом на нижней границе"""
        pair = Pair(1, 5)
        assert pair.rangecheck(1) is True

    def test_rangecheck_upper_bound(self):
        """Тестирование диапазона с числом на верхней границе"""
        pair = Pair(1, 5)
        assert pair.rangecheck(5) is False

    def test_rangecheck_outside(self):
        """Тестирование диапазона с числом вне диапазона"""
        pair = Pair(1, 5)
        assert pair.rangecheck(0) is False
        assert pair.rangecheck(6) is False

    def test_make_pair_valid(self):
        """Тестирование функции make_pair с допустимыми значениями"""
        pair = make_pair(2, 4)
        assert isinstance(pair, Pair)
        assert pair.first == 2
        assert pair.second == 4

    def test_display_method(self, capsys):
        """Тест вывода"""
        pair = Pair(1, 3)
        pair.display()
        captured = capsys.readouterr()
        assert "[1, 3)" in captured.out