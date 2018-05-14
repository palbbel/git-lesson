from string import ascii_letters, digits

valid_values = list(digits + ascii_letters)
radix = len(valid_values)

def convert(number):
    # Конвертирует из 10 в нашу систему
    resault = []

    while number:
        resault.insert(0, valid_values[number % radix])
        number //= radix

    return ''.join(resault)


def inverse(number):
    # Переводит из нашей СС в 10
    resault = 0

    for p, i in enumerate(reversed(number)):
        n = valid_values.index(i)

        resault += n * radix ** p



