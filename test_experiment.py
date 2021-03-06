from experiment import urns, probability, urn_probability, certainty
from experiment import Color
import itertools
import csv
import math

W = Color.WHITE
B = Color.BLACK


def test_probabilities():
    drawn_results = [
        (W,),
        (W, W,),
        (W, W, W),
        (W, W, W, W),
        (W, W, W, W),
    ]
    for urn in urns:
        print(urn)
        for drawn in drawn_results:
            print(f'{drawn}: {probability(drawn, urn)}')


def test_choose_urn():
    drawn_results = [
        (W,),
        (W, W,),
        (W, W, W),
        (W, W, W, W),
        (W, W, W, W, W),
        (W, W, W, W, W, W),
        (W, W, W, W, W, W, W),
    ]
    for urn in urns:
        print(urn)
        for drawn in drawn_results:
            print(f'{drawn}: {urn_probability(drawn)}')


def cross_product(n=4):
    for i in range(1, n + 1):
        yield from itertools.product([W, B], repeat=i)


def test_create_table():
    width = 15

    result = [
        [
            certainty(tuple([W] * x + [B] * y))
            for y in range(width)
        ]
        for x in range(width)
    ]

    # format numbers
    result = [
        [f'{x * 100:0.2f}%' for x in row]
        for row in result
    ]

    print(result)

    with open('certainties.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow([''] + list(range(width)))

        for i, row in enumerate(result):
            writer.writerow([i] + row)


def test_create_quotes():
    result = [
        (0.5, (1, 1))
    ]
    for x in range(200):
        for y in range(1, x + 1):
            if math.gcd(x, y) == 1:
                result.append((x / (y + x), (x, y)))

    result.sort()
    for t in result[-300:]:
        print(f'{t[0]:0.4f} = {t[1]}')
