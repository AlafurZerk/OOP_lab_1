import pytest

from tasks.time_class import Time


class TestTime:
    def test_init_from_numbers(self):
        time = Time(10, 30, 45)
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_init_from_string_colon(self):
        time = Time("10:30:45")
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_init_from_string_space(self):
        time = Time("10 30 45")
        assert time.hours == 10
        assert time.minutes == 30
        assert time.seconds == 45

    def test_init_from_seconds(self):
        time = Time(3665)
        assert time.hours == 1
        assert time.minutes == 1
        assert time.seconds == 5

    def test_to_seconds(self):
        time = Time(1, 1, 5)
        assert time.to_seconds() == 3665

    def test_to_minutes(self):
        time = Time(1, 1, 5)
        assert time.to_minutes() == 61

    def test_add_seconds(self):
        time = Time(1, 1, 5)
        new_time = time.add_seconds(60)
        assert new_time.hours == 1
        assert new_time.minutes == 2
        assert new_time.seconds == 5

    def test_subtract_seconds(self):
        time = Time(1, 2, 5)
        new_time = time.subtract_seconds(60)
        assert new_time.hours == 1
        assert new_time.minutes == 1
        assert new_time.seconds == 5

    def test_comparison_operators(self):
        time1 = Time(1, 0, 0)
        time2 = Time(2, 0, 0)
        time3 = Time(1, 0, 0)

        assert time1 < time2
        assert time2 > time1
        assert time1 == time3
        assert time1 != time2
        assert time1 <= time3
        assert time2 >= time1

    def test_diff_in_seconds(self):
        time1 = Time(1, 0, 0)
        time2 = Time(1, 1, 0)
        assert time1.diff_in_seconds(time2) == 60
