class Pair:
    def __init__(self, first: int, second: int) -> None:
        self.first: int = first
        self.second: int = second

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
    return Pair(first, second)
