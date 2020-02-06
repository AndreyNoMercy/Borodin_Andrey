# Не успел разобраться как вывести результат так же красиво, как в заданни.
# Основная работа зовет)

#current = float(input('Количество километров в первый день: '))
#goal = int(input('Результат, к которого хотим достугнуть: '))
current = float(2)
goal = int(8)
day = 1

print(f"{day}-й день: {current:.2f}")

while True:

    if current < goal:
        current += (0.1 * current)
        day += 1
        print(f"{day}-й день: {current:.2f}")

    else:
        print()
        print(f"на {day}-й день спортсмен достиг результата - не менеее {goal} км.")
        break
