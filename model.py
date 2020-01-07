from keras.layers import Dense
from keras.models import Sequential, load_model
import matplotlib.pyplot as plt
import numpy as np


def preproc_dataset(dir):
    with open(dir + ".txt", "r") as file:
        train = file.read().splitlines()

    base = []
    for i in train:
        base.append(i.split(" "))
        base[-1].pop(-1)

    with open("dict.txt", "r") as file:
        dict_words = file.read().splitlines()

    dict_words = dict.fromkeys(dict_words)
    j = 0
    for i in dict_words:
        dict_words[i] = j
        j += 1

    train_one_hots = np.zeros((len(base), len(dict_words)))

    for id_b, val_i in enumerate(base):
        for id_b_w, val_j in enumerate(val_i):
            for id_d, val_k in enumerate(dict_words):
                if val_j == val_k:
                    train_one_hots[id_b][id_d] = 1

    with open("metka.txt", "r") as file:
        metka = file.read().split(',')

    metka.pop(-1)
    metka = [int(i) for i in metka]

    dataset = {
        'data': train_one_hots,
        'result': np.array(metka)
    }

    return dataset


def train_and_check_model():
    dataset = preproc_dataset('train')

    max_words = len(dataset['data'][0])

    model = Sequential()
    model.add(Dense(256, activation='relu', input_shape=(max_words,)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(dataset['data'],
                        dataset['result'],
                        epochs=5,
                        validation_split=0.1)

    model.save('Words_neural.h5')

    plt.plot(history.history['accuracy'],
             label='Доля верных ответов на обучающем наборе')
    plt.plot(history.history['val_accuracy'],
             label='Доля верных ответов на проверочном наборе')
    plt.xlabel('Эпоха обучения')
    plt.ylabel('Доля верных ответов')
    plt.legend()
    plt.show()


def predicting_model():
    model = load_model('Words_neural.h5')
    data = preproc_dataset('pred')

    result = model.predict(data['data'])

    return result