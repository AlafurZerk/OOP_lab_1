#!/usr/bin/env python3


from tasks.pair_class import Pair, make_pair

if __name__ == "__main__":
    print("=== Демонстрация класса Pair ===")

    p1 = make_pair(3, 7)
    print("Интервал p1:", end=" ")
    p1.display()
    print("Проверка числа 5 в интервале p1:", p1.rangecheck(5))
    print("Проверка числа 7 в интервале p1:", p1.rangecheck(7))

    print("\n--- Создание интервала вручную ---")
    p2 = Pair(0, 0)
    try:
        p2.read()
    except ValueError as e:
        print(e)
        exit(1)

    print("Интервал p2:", end=" ")
    p2.display()

    num = int(input("Введите число для проверки в интервале p2: "))
    print(f"Число {num} в интервале p2:", p2.rangecheck(num))
