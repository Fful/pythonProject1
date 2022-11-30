with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    del_signs = str.maketrans("", "", ",.?!-_;:")
    for line in infile:
        # Привести к одному регистру
        line_low = line.lower()
        # Удалить знаки препинания
        line_del_signs = line_low.translate(del_signs)
        # Разбить на слова
        words = line_del_signs.split()
        # Записать все слова по одному на строку файла
        for cleaned_words in words:
            outfile.write(cleaned_words + "\n")