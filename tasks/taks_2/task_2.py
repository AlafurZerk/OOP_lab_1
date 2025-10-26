#!/usr/bin/env python3


from tasks.time_class import Time

if __name__ == "__main__":
    print("=== Демонстрация класса Time ===")

    print("Создание времени разными способами:")
    t1 = Time(10, 30, 45)
    print("Из чисел (10, 30, 45):", end=" ")
    t1.display()

    t2 = Time("12:45:30")
    print("Из строки '12:45:30':", end=" ")
    t2.display()

    t3 = Time("12 45 30")
    print("Из строки '12 45 30':", end=" ")
    t3.display()

    t4 = Time(3665)
    print("Из секунд (3665):", end=" ")
    t4.display()

    print("\n--- Операции со временем ---")
    print("Разница в секундах между t1 и t2:", t1.diff_in_seconds(t2))

    t5 = t1.add_seconds(120)
    print("t1 + 120 секунд:", end=" ")
    t5.display()

    t6 = t2.subtract_seconds(180)
    print("t2 - 180 секунд:", end=" ")
    t6.display()

    print("t1 в секундах:", t1.to_seconds())
    print("t1 в минутах (с округлением):", t1.to_minutes())

    print("\n--- Сравнение времени ---")
    print("t1 == t2:", t1 == t2)
    print("t1 < t2:", t1 < t2)
    print("t1 > t2:", t1 > t2)

    print("\n--- Ввод времени с клавиатуры ---")
    t7 = Time(0, 0, 0)
    t7.read()
    print("Вы ввели:", end=" ")
    t7.display()
