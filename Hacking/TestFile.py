

class GoodPasswordGenerator:
    def __init__(self):
        print('Я родился')
        self.length = 10

    def generate(self):
        self.length += 1
        return 'abc123'


good_gen = GoodPasswordGenerator()
print(good_gen.length)
good_gen.length2 = 15
print(good_gen.length2)
print(good_gen.generate())

