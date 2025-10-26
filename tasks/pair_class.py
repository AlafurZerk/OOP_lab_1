class Pair:
    def __init__(self, first, second):
        if first >= second:
            raise ValueError("Ошибка: first должен быть меньше second.")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите начало интервала (first): "))
        self.second = int(input("Введите конец интервала (second): "))
        if self.first >= self.second:
            raise ValueError("Ошибка: first должен быть меньше second.")

    def display(self):
        print(f"[{self.first}, {self.second})")

    def rangecheck(self, number):
        return self.first <= number < self.second


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        exit(1)
