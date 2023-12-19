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

#підняття винятків
text = input("Введіть текст! ")
if type(text) != int:
    raise TypeError(f"Ми не працюємо з цим {type(text)} типом")
