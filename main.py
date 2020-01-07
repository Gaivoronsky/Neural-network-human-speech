from voice import record_recognition
from model import preproc_dataset, train_and_check_model, predicting_model
from script import generate_train_and_metk


def train_model():
    generate_train_and_metk()
    train_and_check_model()


def use_code():
    record_recognition()
    result = predicting_model()

    if result > 0.5:
        print('В вашей речи есть слова паразиты')
    elif result < 0.5:
        print('В вашей речи нет слов паразитов')
    else:
        print('Error')

use_code()