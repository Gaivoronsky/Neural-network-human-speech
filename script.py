import random


def generate_train_and_metk(size = 5000):
    with open("dict.txt", "r") as file:
        Dict = file.read().splitlines()

    dict_words = dict.fromkeys(Dict)
    j = 0
    for i in dict_words:
        dict_words[i] = j
        j += 1

    dict_words_values = {}
    j = 0
    for i in dict_words:
        dict_words_values.update({j: i})
        j += 1

    with open("paraz.txt", "r") as file:
        Paraz = file.read().splitlines()

    bad_words = []
    for i in Paraz:
        bad_words.append(dict_words[i])

    itera = 0
    metka_values = []
    base_text = []
    for i in range(size):
        metka_values.append(0)
    while itera < size:
        j = 0
        random_values = []
        while j < 10:
            random_values.append(random.choice(range(len(dict_words_values))))
            j += 1
        else:
            text = ''
            for i in range(10):
                text += dict_words_values[random_values[i]]
                text += ' '
            base_text.append(text)

            for l in range(len(random_values)):
                for k in range(len(bad_words)):
                    if random_values[l] == bad_words[k]:
                        metka_values[itera - 1] = 1

        itera += 1

    with open("metka.txt", "w") as file:
        for i in metka_values:
            file.write(str(i) + ",")

    with open("train.txt", "w") as file:
        for i in base_text:
            file.write(i + '\n')