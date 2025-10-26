class Pair:
    first: int
    second: int

    def __init__(self, first: int, second: int) -> None:
        if first >= second:
            raise ValueError("Ошибка: first должен быть меньше second.")
        self.first = first
        self.second = second

    def read(self) -> None:
        self.first = int(input("Введите начало интервала (first): "))
        self.second = int(input("Введите конец интервала (second): "))
        if self.first >= self.second:
            raise ValueError("Ошибка: first должен быть меньше second.")

    def display(self) -> None:
        print(f"[{self.first}, {self.second})")

    def rangecheck(self, number: int) -> bool:
        return self.first <= number < self.second


def make_pair(first: int, second: int) -> Pair:
    try:
        return Pair(first, second)
    except ValueError as e:
        print(e)
        exit(1)
