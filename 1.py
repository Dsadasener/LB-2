while True:
    sentence = input("Введіть речення (щонайменше 7 слів): ")
    words = sentence.split()

    if len(words) >= 7:
        break
    else:
        print("Помилка! Речення має містити щонайменше 7 слів.")

result_words = []

for word in words:
    clean_word = word.strip(".,!?\"'").lower()

    if clean_word != "привіт":
        result_words.append(word)

if len(result_words) == 0:
    print("\nУ реченні немає слів, відмінних від «привіт».")
else:
    print("\nСлова в реченні, відмінні від «привіт»:")
    print(" ".join(result_words))