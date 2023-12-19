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
# text = input("Введіть текст! ")
# if type(text) != int:
#     raise TypeError(f"Ми не працюємо з цим {type(text)} типом")
#генерація власних винятків
class BuildingError(Exception):
    def __str__(self):
        return "Не вистачає матеріалів! Не можливо побудувати"

def check_materials(amont_materials, limit_materials):
    if amont_materials > limit_materials:
        print("Матеріалу достатньо!")
    else:
        raise BuildingError

my_materials = 123
check_materials(my_materials, 300) #300 мінімальна кількість