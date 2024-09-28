import os
from random import choice
from contextlib import contextmanager

COLOURS = {
    'black': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
}

RESET = '\033[0m'


@contextmanager
def print_color(colour: str):
    colour = colour.lower()
    if colour in COLOURS:
        print(COLOURS[colour])
    try:
        yield
    finally:
        print(RESET)


def main() -> None:
    script_loc = os.path.abspath(os.path.dirname(__file__))
    art_dir = os.path.join(script_loc, 'art')
    art_names = os.listdir(art_dir)
    art_decision = choice(art_names)

    art_path = os.path.join(art_dir, art_decision)
    with open(art_path, 'r', encoding='utf8') as f:
        art = [line for line in f]

    colour = col if (col := art[0].strip().lower()) in COLOURS else ''

    quotes_path = os.path.join(script_loc, 'quotes.txt')
    with open(quotes_path, 'r', encoding='utf8') as f:
        quotes = [line.strip() for line in f]
    quote = choice(quotes)

    with print_color(colour):
        print(''.join(art[1:] if colour else art))
        print('-' * (len(quote) + 4))
        print(f'| {quote} |')
        print('-' * (len(quote) + 4))


if __name__ == '__main__':
    main()
