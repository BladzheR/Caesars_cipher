from pyaspeller import Word

QUANTITY_LETTER_ALPHABET = 32  # Кол-во букв в алфавите
alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def get_key():
    """
    Получить ключ от пользователя путём ручного ввода с клавиатуры.
    :return: возвращает целое десятичное число (ключ)
    """
    while True:
        print('Введите числовой ключ[1-%s]' % QUANTITY_LETTER_ALPHABET)

        key = input()

        # проверка на целове число и на соответствие условию ввода от 1 до QUANTITY_LETTER_ALPHABET
        if key.isdecimal() and 1 <= int(key) <= QUANTITY_LETTER_ALPHABET:
            return int(key)
        else:
            print("Упс... Что-то пошло не так. Попробуйте еще раз!")


def get_decoding_text(text, key):
    """
    Расшифровка шифра Цезаря по ключу.
    :param text: строка содержащая текст
    :param key: ключ для расшифровки текста(целое десятичное число)
    :return: текстовая строка содержащая расшифрованны текст
    """
    translated = ''
    key = -key  # Используется для расшифровки
    for symbol in text:
        if symbol.isalpha():

            if symbol.isupper():
                alphabet = alphabet_upper

            elif symbol.islower():
                alphabet = alphabet_lower

            index = alphabet.index(symbol)

            shift = index + key

            if shift >= QUANTITY_LETTER_ALPHABET:
                shift -= QUANTITY_LETTER_ALPHABET

            res = alphabet[shift:]

            translated += res[0]
        else:
            translated += symbol

    return translated


def check(words, char):
    k = 0
    for i in words:
        if i == char:
            k += 1
    return k


def print_frequency_analysis(text):
    """
    Расчет и вывод частотного анализа в консоль.
    :param text: строка содержащая текст
    :return:
    """

    dict = {i for i in text.replace(' ', '')}  # удаляем пробелы из строки

    percent = 100
    length = len(text)
    var = 0
    my_dict = {}

    for symbol in dict:
        stat = percent * check(text, symbol) / length
        if var % 2 == 0:
            print("\t\t{0} - {1}%\t".format(symbol, round(stat, 4)), end="")
            var += 1

            my_dict[symbol] = stat
        else:
            print("{0} - {1}%".format(symbol, round(stat, 4)))
            var += 1

            my_dict[symbol] = stat

    print("\n")

    return 0


def automatic_typo_correction(text):
    """
    Автоматическое исправление опечаток в тексте используя pyaspeller.
    :param text: строка содержащая текст
    :return: строка после обработки
    """
    list_word = text.split()
    result_text = ""
    for word in list_word:
        check = Word(word)
        result_check = check.spellsafe
        if result_check:
            result_text += result_check + " "
        else:
            result_text += word + " "

    return result_text
