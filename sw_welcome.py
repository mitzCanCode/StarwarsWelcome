import argparse
import os
from random import choice
from contextlib import contextmanager

SCRIPT_LOC = os.path.abspath(os.path.dirname(__file__))
ART_DIR = os.path.join(SCRIPT_LOC, 'art')
QUOTES_PATH = os.path.join(SCRIPT_LOC, 'quotes.txt')
ART_ASSETS = os.listdir(ART_DIR)
with open(QUOTES_PATH, 'r', encoding='utf8') as f:
    QUOTE_ASSETS = [line.strip() for line in f]

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


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
            prog='StarWarsWelcome',
            description='A simple script that displays'
            ' coloured ascii art of starwars characters'
            ' and some pre ai generated quotes. The'
            ' ascii art is not mine.',
    )

    parser.add_argument('art',
                       help='The path to the ascii art'
                       ' to be displayed. One is chosen'
                       ' at random if not provided.',
                       type=str,
                       nargs='?',
                       default='',)
    parser.add_argument('quote',
                       help='The quote to be displayed.'
                       ' One is chosen from quotes.txt'
                       ' at random if not provided.',
                       type=str,
                       nargs='?',
                       default='',)
    parser.add_argument('--colour',
                        help='Override predefined art'
                        ' colour.',
                        choices=COLOURS.keys())

    return parser.parse_args()


@contextmanager
def print_color(colour: str):
    if colour in COLOURS:
        print(COLOURS[colour])
    try:
        yield
    finally:
        print(RESET)


def main() -> None:
    args = cli()

    art_decision = '' if args.art else choice(ART_ASSETS)
    quote = args.quote if args.quote else choice(QUOTE_ASSETS)

    art_path = args.art if args.art else os.path.join(ART_DIR, art_decision)
    with open(art_path, 'r', encoding='utf8') as f:
        art = [line for line in f]

    defined_colour = col if (col := art[0].strip().lower()) in COLOURS else ''

    colour = args.colour if args.colour else defined_colour

    with print_color(colour):
        print(''.join(art[1:] if colour else art))
        print('-' * (len(quote) + 4))
        print(f'| {quote} |')
        print('-' * (len(quote) + 4))


if __name__ == '__main__':
    main()
