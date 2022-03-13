def split_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def convert_to_base(number, alphabet):
    digits = split_to_base(number, len(alphabet))
    if digits[-2:] == [0, 0]:
        power = 0
        while digits[-1] == 0:
            power += 1
            digits.pop()

        postfix = 'ro' + convert_to_base(power, alphabet)
    else:
        postfix = ''

    return ''.join(alphabet[n] for n in digits) + postfix


def generate_alphabet(base, sequences):
    result = []

    for i in range(base):
        word = ''
        for sequence in sequences:
            word += sequence[i % len(sequence)]
        result.append(word)

    return result


def visualize(
    alphabet,
    units={
        'mile': 1440,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 86400 * 7,
        'month': 86400 * 30,
        'year': 86400 * 360,
    },
):
    for i, word in enumerate(alphabet):
        print(f'{i}. {word[0].capitalize()} - {word}')

    convert = lambda n: convert_to_base(n, alphabet)

    print('\nSome nouns:')
    for original, translation in units.items():
        print(f'- {original} is {convert(translation)}')


if __name__ == '__main__':
    visualize(generate_alphabet(12, [
        'b p d t v f g k j sh z s'.split(),
        'a i e o u'.split(),
    ]))