"""Модуль wo. Содержит функцию: words_occur()"""
# Функции интерфейса


def words_occur():
    """words_occur() - подсчитывает вхождения слов в файле."""
    # Запросить у пользователя имя файла.
    filename = input("type the filename u would check:")
    # Открыть файл, прочитать его и сохранить слова в списке.
    f = open(filename, 'r')
    f_words = f.read().split()
    f.close()
    # Подсчитать количество вхождений каждого слова в файле.
    occur_dict = {}
    for word in f_words:
        # Увеличить счетчик для данного слова.
        occur_dict[word] = occur_dict.get(word, 0) + 1
    # Вывести результаты.
    print("File %s has %d words (%d are unique)" % (filename, len(f_words), len(occur_dict)))
    print(occur_dict)


if __name__ == '__main__':
    words_occur()

