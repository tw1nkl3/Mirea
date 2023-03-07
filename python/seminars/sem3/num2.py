import csv
from collections import Counter
from functools import lru_cache
from typing import List

import Levenshtein
import pymorphy2


@lru_cache(maxsize=None)
def load_dictionary(file_path: str) -> List[str]:
    """Загрузка словаря из CSV-файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        words = [row[0] for row in reader]
    return words


def spell(text: str, dictionary: List[str]) -> str:
    """Проверка орфографии текста."""
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()

    corrected_words = []
    for word in words:
        # Проверка, есть ли слово в словаре
        if word in dictionary:
            corrected_words.append(word)
        else:
            # Поиск среди словарных слов с расстоянием Левенштейна равным 1
            candidate_words = [w for w in dictionary if Levenshtein.distance(word, w) == 1]
            if candidate_words:
                # Выбор наиболее популярного слова из кандидатов
                counter = Counter(candidate_words)
                corrected_word = counter.most_common(1)[0][0]
                corrected_words.append(corrected_word)
            else:
                # Поиск среди словарных слов с расстоянием Левенштейна равным 2
                candidate_words = [w for w in dictionary if Levenshtein.distance(word, w) == 2]
                if candidate_words:
                    # Выбор наиболее популярного слова из кандидатов
                    counter = Counter(candidate_words)
                    corrected_word = counter.most_common(1)[0][0]
                    corrected_words.append(corrected_word)
                else:
                    # Слово не найдено в словаре
                    corrected_words.append(word)

    # Возвращение скорректированного текста
    return ' '.join(corrected_words)


# Загрузка словаря из CSV-файла с указанием частот встречаемости
dictionary = load_dictionary('dictionary.csv')

# Проверка орфографии текста
text = 'помоему я напесал усё правильна'
corrected_text = spell(text, dictionary)
print(corrected_text)  # по-моему я написал все правильно
