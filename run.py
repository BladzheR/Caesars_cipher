#########################################################################
# Программа для работы с шифром Цезаря. По умолчанию с русским алфавитом.
# Автор: BladzheR
# Телеграм: @BladzheR
#########################################################################
from functions import *


def main():
    key = get_key()

    # читаем текстовый файл в список
    with open("message", "r") as f:
        message = f.readlines()

    for text in message:
        print("Исходный текст:\n" + text + "\n")
        print("Частотный анализ:")
        print_frequency_analysis(text)
        print("Текст после сдвига согласно ключу:")
        result = get_decoding_text(text, key)
        print(result)

        print("Сделать автоматическое исправление опечаток?")
        answer = input()
        if answer == 'д' or answer == '':
            text = automatic_typo_correction(result)
            print(text)

        while True:
            print("Хотите провести замену определенных букв вручную??\n"
                  "Если да, введите 'д', иначе введите 'н' для ручной замены определенных букв")
            answer = input()
            if answer == 'д' or answer == 'Д' or answer == '':
                break
            elif answer == 'н' or answer == 'Н':
                print("Введите одну букву, которую хотите заменить:")
                template = input()
                print("Введите одну букву на которую хотите заменить:")
                replacement = input()
                result = result.replace(template, replacement)
                print(result)


if __name__ == "__main__":
    main()
