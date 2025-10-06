import pytest

from tasks.pair_class import Pair, make_pair


class TestPair:
    def test_init_valid(self):
        pair = Pair(1, 5)
        assert pair.first == 1
        assert pair.second == 5

    def test_init_invalid(self):
        with pytest.raises(ValueError):
            Pair(5, 1)

    def test_rangecheck_inside(self):
        pair = Pair(1, 5)
        assert pair.rangecheck(3) is True

    def test_rangecheck_outside(self):
        pair = Pair(1, 5)
        assert pair.rangecheck(7) is False
        assert pair.rangecheck(1) is True
        assert pair.rangecheck(5) is False

    def test_make_pair_valid(self):
        pair = make_pair(1, 5)
        assert isinstance(pair, Pair)

    def test_display_method(self):
        pair = Pair(1, 5)
        # Проверяем, что метод display не вызывает ошибок
        try:
            pair.display()
        except Exception as e:
            pytest.fail(f"display() method failed with {e}")
