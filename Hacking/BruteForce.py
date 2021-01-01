import random
import Paroli

class BadPasswordGenerator:
    def __init__(self):
        self.passwords = Paroli.passwords_file.split()
        self.index = 0

    def generate(self):
        if self.index >= len(self.passwords):
            raise ValueError('Пароли закончились')
        password = self.passwords[self.index]
        self.index += 1
        return password


bad_gen = BadPasswordGenerator()
print(len(bad_gen.passwords))
print(bad_gen.generate())


class GoodPasswordGenerator:
    def __init__(self, length=10):
        self.length = length
        self.alphabet = '0123456789' \
                        'qwertyuiopasdfghjklzxcvbnm' \
                        'QWERTYUIOPASDFGHJKLZXCVBNM' \
                        '!@#$%^&*()_+{};:"\'\\|<>?,./'

    def generate(self):
        password = ''
        for i in range(self.length):
            symbol = random.choice(self.alphabet)
            password += symbol

        return password


# good_gen5 = GoodPasswordGenerator(length=5)
# good_gen10 = GoodPasswordGenerator()
# print(good_gen10.alphabet)
# print(len(good_gen10.alphabet))
# print(good_gen10.length, good_gen5.length)
# print(good_gen10.generate(), good_gen5.generate())


import requests

response = requests.get('https://google.com/')
print(response.status_code)
print(response.text)