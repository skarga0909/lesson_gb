def num_translate(number):
    for item in numbers_ten:
        if number == item:
            return numbers_ten[item]
    return None


number = input("Enter a number in English: ")
numbers_ten = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восень', 'nine': 'девять', 'ten': 'десять'}

print(num_translate(number))
