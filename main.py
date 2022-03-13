def split_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def convert_to_base(number, alphabet):
    return ''.join(alphabet[n] for n in split_to_base(number, len(alphabet)))


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
    visualize('plap be tib dmo fat ve knid go shaf jre siv zo'.split())