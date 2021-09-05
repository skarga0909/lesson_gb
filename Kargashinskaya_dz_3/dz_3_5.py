import random


def get_jokes(joke):
    """
    The function get_jokes(n) returns a list of jokes, formed from three random words,
    taken from three lists (one from each).
    """
    i = 1
    result = []
    while i <= n:
        j_1 = random.choice(nouns)
        j_2 = random.choice(adverbs)
        j_3 = random.choice(adjectives)
        joke = [j_1, j_2, j_3]
        joke_str = ' '.join(joke)
        result.append(joke_str)
        i = i + 1
    print(result)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input('введите число шуток: '))
get_jokes(n)
