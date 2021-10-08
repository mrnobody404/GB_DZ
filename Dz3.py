import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def random_choice(write):
    j = []
    for i in range(0,write):
        a = random.choice(nouns)
        b = random.choice(adverbs)
        c = random.choice(adjectives)
        e = f'{a} {b} {c}'
        j.append(e)

    return j
write = int(input('Введите число'))
print(random_choice(write))
