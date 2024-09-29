"""Скалярні типи та посилання"""


def inc(a: int):
    return {a, a + 1}

print(inc(5))


def inc_1(a: int):
    return a + 1

obj = 5

print(inc_1(obj))


"""Типи даних"""


array = [True, 'hello', 5, 12, -200, False, 'word', 3.14, 42, 'Python', None, 0, 100, 'example', 2.718, [1, 2, 3], (1, 2), {'key': 'val'}]

tps = {}


for i in array:
    type_of_element = type(i).__name__
    if not type_of_element in tps:
        tps[type_of_element] = 0
    tps[type_of_element] += 1

print(tps)