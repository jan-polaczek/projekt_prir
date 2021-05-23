import sys
import random


def char_range(n):
    for ch in range(ord('A'), ord('A') + n):
        yield chr(ch)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    min_dist = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    max_dist = int(sys.argv[3]) if len(sys.argv) > 3 else 15
    output_file = sys.argv[4] if len(sys.argv) > 4 else 'data.dat'

    cities = [c for c in char_range(n)]
    paths = []

    for i, city in enumerate(cities):
        for other_city in cities[i + 1:]:
            dist = random.randint(min_dist, max_dist)
            path = f'{city} {other_city} {dist}'
            paths.append(path)

    with open(output_file, 'w') as f:
        f.write(' '.join(cities) + '\n')
        for path in paths:
            f.write(path + '\n')


if __name__ == '__main__':
    main()
