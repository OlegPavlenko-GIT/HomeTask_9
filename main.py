# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из
# исходного файла все слова, состоящие не менее чем из семи букв.
def filter_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        words = text.split()

        long_words = [word for word in words if len(word) >= 7]

    with open(output_file, 'w') as file:
        for word in long_words:
            file.write(word + '\n')

# Укажите путь к исходному файлу и файлу для записи отфильтрованных слов
input_file = 'text.txt'
output_file = 'New.txt'

# Вызов функции для фильтрации слов
filter_words(input_file, output_file)

#
#
# 2. Дан текстовый файл. Подсчитать количество слов в нём.
def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        return word_count

# Пример использования
word_count = count_words('text.txt')
print(f'Количество слов: {word_count}')
