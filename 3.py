def sort_set_alphabetically(char_set):
    char_list = list(char_set)

    char_list.sort(key=str.lower)

    print("Відсортовані елементи (як список):")
    print(char_list)
    print("-" * 40)

    result_set = set(char_list)
    print("Результат після зворотного перетворення (як множина):")
    print(result_set)

initial_chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
my_set = set(initial_chars)

sort_set_alphabetically(my_set)