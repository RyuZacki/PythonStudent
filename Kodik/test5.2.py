from datetime import datetime

#Декораторы2.0


def timeit(arg): # <-- Тут я получаю функцию, как объект
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs) # <-- Тут я вызвал функцию, которую получиь на входе
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit('name')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit('name')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l

l1 = timeit('name')(one)(10)

# l1 = timeit(one)(10) # => wrapper(10) => one(10)
# print(type(l1), l1.__name__)

# l1 = one
# a = l1(10)
# print(a)

# l1 = one(10000)
# l2 = two(10000)
#
# #print(l1)
# #print(l2)
