import pytest
from tasks.time_class import Time


class TestTime:
    def test_creation_from_parts(self):
        """Тестирования создания через часы, минуты, секунды"""
        time = Time(10, 30, 45)
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_creation_from_string_colon(self):
        """Тестирование создания из строки с разделителем в виде двоеточия"""
        time = Time("10:30:45")
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_creation_from_string_space(self):
        """Тестирование создания из строки с разделителем в виде пробела"""
        time = Time("10 30 45")
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_creation_from_seconds(self):
        """Тестирование создания из указанного количества секунд"""
        time = Time(3665)  # 1 hour, 1 minute, 5 seconds
        assert time.hours == 1
        assert time.minutes == 1
        assert time.seconds == 5

    def test_to_seconds(self):
        """Тестирование преобразования в секуды"""
        time = Time(1, 1, 5)
        assert time.to_seconds() == 3665

    def test_to_minutes(self):
        """Тестирование преобразования"""
        time = Time(1, 1, 30)
        assert time.to_minutes() == 61  # rounded

    def test_comparison_operators(self):
        """Тестирование сравнения"""
        t1 = Time(10, 0, 0)
        t2 = Time(10, 0, 0)
        t3 = Time(11, 0, 0)

        assert t1 == t2
        assert t1 <= t2
        assert t1 >= t2
        assert t1 < t3
        assert t3 > t1
        assert t1 != t3

    def test_add_seconds(self):
        """Тестирование добавления секунд"""
        time = Time(10, 0, 0)
        new_time = time.add_seconds(65)
        assert new_time.hours == 10
        assert new_time.minutes == 1
        assert new_time.seconds == 5

    def test_subtract_seconds(self):
        """Тестирование вычитания секунд"""
        time = Time(10, 1, 5)
        new_time = time.subtract_seconds(65)
        assert new_time.hours == 10
        assert new_time.minutes == 0
        assert new_time.seconds == 0

    def test_subtract_seconds_negative(self):
        """Тестирование вычитания слишком большого количества секунд"""
        time = Time(0, 0, 10)
        with pytest.raises(ValueError, match="Результат не может быть отрицательным"):
            time.subtract_seconds(20)

    def test_diff_in_seconds(self):
        """Тестирование разницы"""
        t1 = Time(10, 0, 0)
        t2 = Time(10, 1, 0)
        assert t1.diff_in_seconds(t2) == 60

    def test_invalid_initialization(self):
        """Тестирование на недопустимые параметры инициализации"""
        with pytest.raises(ValueError):
            Time(25, 70, 80)

        with pytest.raises(ValueError):
            Time("invalid_string")

    def test_display_method(self, capsys):
        """Тестирование вывода"""
        time = Time(1, 2, 3)
        time.display()
        captured = capsys.readouterr()
        assert "01:02:03" in captured.out