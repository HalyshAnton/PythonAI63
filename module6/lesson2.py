# # індексація
#
# word = "Python"
#
# # застосування індекса
# # [str змінна][індекс]
# letter = word[1]  # 1 індекс -- у
#
# print(letter)
#
# print(word[3])
#
# num = 3
# print(word[num])
#
# letter1 = word[2]
# letter2 = word[5]


# можна лише отримувати символи але не змінювати
word = "Python"

# word[0] = "J"

# word[100]

# від'ємні індекси

# останній символ

# text = "Hello world"
#
# print(text[-1])


# зрізи

# змінна[початок:кінець:крок]

text = "Hello world"


# print(text[0:5])
# print(text[6:11])
#
# # нюанс 1 -- якщо не вказати початок, то зазамовчунням початок слова
# print(text[:5])

# # нюанс 2 -- якщо не вказати кінець, то зазамовчунням буде кінецб слова
# print(text[6:])
# print(text[:6])


# word = "Python!"
#
# print(word[:3])  # перші 3
# print(word[3:])  # всі окрім перших трьох
#
# print(word[-3:]) # останні 3
# print(word[-3])  # третя з кінця літера
# print(word[:-3]) # все окрім останніх трьох
# print(word[::-1])  # слово задом неперед


# # поєднання з циклом for
#
# text = "Python"
#
# for i in range(len(text)):  # 99% використання range
#     # i -- індекс(число)
#
#     letter = text[i]
#     print(f"{letter} -- з індексом {i}")
