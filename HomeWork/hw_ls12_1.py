# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів і запише цей текст в інший файл.

# html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.

# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу, куди потрібно записати очищений текст.
# Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.

# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt).
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.

# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.


import re
import codecs

def delete_html_tags(html_file, result_file="home_cleaned.txt"):
    with codecs.open(html_file, "r", encoding="utf-8") as file:
        html = file.readlines()

    cleaned_lines = []
    for line in html:
        cleaned_line = re.findall(r">(.+)</", line)
        for text in cleaned_line:
            if text.strip():
                cleaned_lines.append(text.strip())

    with open(result_file, "w", encoding="utf-8") as file:
        for line in cleaned_lines:
            file.write(line + "\n")

delete_html_tags("draft.html", "home_cleaned.txt")
