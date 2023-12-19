try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(f"Ділити на нуль не можна! {e}")
finally:
    print("Далі якийсь код")

try:
    number = int(input("Введіть число:"))
except ValueError as e:
    print(e)