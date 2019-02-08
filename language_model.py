import random
import pickle
import numpy as np


class Text_generator:

    def __init__(self, seed=0):
        seed = int(seed)
        random.seed(seed)
        np.random.seed(seed)
        self.model = {}

    def fit(self, text_string):
        words = Text_generator.prepare_text(text_string)
        last_word = ""
        sequence = {}
        for word in words:
            if last_word in sequence:
                if word not in sequence[last_word]:
                    sequence[last_word][word] = 0
                sequence[last_word][word] += 1
            else:
                sequence[last_word] = {}
                sequence[last_word][word] = 1

            last_word = word

        for word in sequence:
            if word == '':
                continue
            keys = np.array(list(sequence[word].keys()))
            values = np.array(list(sequence[word].values()), dtype='f')

            values = values / values.sum()
            words = [keys, values]

            self.model[word] = words

    def save_model(self, path):
        with open(path + '.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_model(self, path):
        with open(path + '.pickle', 'rb') as handle:
            self.model = pickle.load(handle)

    def generate(self, begin_word='', length=10):
        if begin_word == '' or begin_word not in self.model:
            begin_word = random.choice(list(self.model.keys()))

        curr_word = begin_word
        result_text = ''

        for i in range(length):
            result_text += curr_word + ' '
            curr_word = np.random.choice(self.model[curr_word][0], 1,
                                         p=self.model[curr_word][1])[0]
        return result_text

    @staticmethod
    def prepare_text(text):
        clean_text = ""
        text = text.lower()
        for i in text:
            # Russion and english letters
            if i.isalpha():
                clean_text += i
            elif i == ' ' or i == '\n':
                clean_text += ' '

        word_array = clean_text.split(' ')
        word_array = [word for word in word_array if word != '']

        return word_array
