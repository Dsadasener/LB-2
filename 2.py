
def insert_before_element(lst, target, new_item):
    if target in lst:
        index = lst.index(target)
        lst.insert(index, new_item)
        print("\nОновлений список:", lst)
    else:
        print(f"\nПомилка: елемент '{target}' не знайдено у списку.")

input_data = input("Введіть елементи списку через пробіл: ")
my_list = input_data.split()

print("Поточний список:", my_list)

target_element = input("Перед яким елементом вставити новий?: ")
new_element = input("Введіть новий елемент: ")

insert_before_element(my_list, target_element, new_element)