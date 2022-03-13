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
    if digits[-3:] == [0, 0, 0]:
        power = 0
        while digits[-1] == 0:
            power += 1
            digits.pop()

        postfix = 'ro' + convert_to_base(power, alphabet)
    else:
        postfix = ''

    return ''.join(alphabet[n] for n in digits) + postfix


# noinspection PyDefaultArgument
def generate_alphabet(
    vowels='a i e o u'.split(),
    consonants=zip(
        'b d v g j z'.split(),
        'p t f k sh s'.split(),
    ),
):
    result = []
    vowels_i = 0

    for pair in consonants:
        for c in pair:
            result.append(c + vowels[vowels_i])

            vowels_i = (vowels_i + 1) % len(vowels)

    return result


def visualize(alphabet):
    for i, word in enumerate(alphabet):
        print(f'{i}. {word[0].capitalize()} - {word}')

    convert = lambda n: convert_to_base(n, alphabet)

    print()
    print(fr"""

Some nouns:
- kilometer is {convert(1000)}
- minute is {convert(60)}
- hour is {convert(3600)}
- day is {convert(86400)}

    """.strip())


if __name__ == '__main__':
    visualize(generate_alphabet())