def count_words(input_string):
    # Удаляем лишние пробелы и разбиваем строку по пробелам
    words = input_string.strip().split()
    # Возвращаем количество слов
    return len(words)

# Пример использования
text = "Привет, как дела?"
print(count_words(text))  # Вывод: 3
