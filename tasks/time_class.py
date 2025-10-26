class Time:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                self._init_from_string(args[0])
            elif isinstance(args[0], int):
                self._init_from_seconds(args[0])
            elif isinstance(args[0], Time):
                self.hours = args[0].hours
                self.minutes = args[0].minutes
                self.seconds = args[0].seconds
            else:
                raise ValueError("Invalid initialization argument")
        elif len(args) == 3:
            self._init_from_parts(args)
        else:
            raise ValueError("Invalid number of arguments")

        self._normalize()

    def _init_from_string(self, time_str):
        for separator in [":", " ", "-", ".", ","]:
            if separator in time_str:
                parts = list(map(int, time_str.split(separator)))
                if len(parts) == 3:
                    self._init_from_parts(parts)
                    return

        try:
            total_seconds = int(time_str)
            self._init_from_seconds(total_seconds)
        except ValueError:
            raise ValueError("Неправильный формат времени")

    def _init_from_parts(self, parts):
        self.hours, self.minutes, self.seconds = parts
        if not (0 <= self.minutes < 60 and 0 <= self.seconds < 60):
            raise ValueError("Минуты и секунды должны быть между 0 и 59")

    def _init_from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def _normalize(self):
        total_seconds = self.to_seconds()
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def read(self):
        while True:
            try:
                time_str = input("Введите время в формате чч:мм:сс: ")
                self._init_from_string(time_str)
                self._normalize()
                break
            except ValueError as e:
                print(f"Ошибка: {e}. Попробуйте еще раз.")

    def display(self):
        time_str = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        print(time_str)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def to_minutes(self):
        return round(self.to_seconds() / 60)

    def diff_in_seconds(self, other):
        return abs(self.to_seconds() - other.to_seconds())

    def add_seconds(self, seconds):
        total_seconds = self.to_seconds() + seconds
        return Time(total_seconds)

    def subtract_seconds(self, seconds):
        total_seconds = self.to_seconds() - seconds
        if total_seconds < 0:
            raise ValueError("Не может быть < 0")
        return Time(total_seconds)

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()
