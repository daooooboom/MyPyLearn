import sys
import random

chars = '\|/'

def draws(rows, column):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(column)))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")