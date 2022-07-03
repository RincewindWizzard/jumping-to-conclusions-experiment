from enum import Enum
from loguru import logger


class Color(Enum):
    WHITE = 1
    BLACK = 2

    def __repr__(self):
        return 'W' if self == Color.WHITE else 'B'


UrnType = dict[Color, int]


def urn_repr(urn: UrnType):
    values = ', '.join(
        str(urn[k])
        for k in sorted(
            urn.keys(),
            key=lambda x: x.value)
    )
    return f'Urn({values})'


urns = [
    {
        Color.WHITE: 4,
        Color.BLACK: 6,
    },
    {
        Color.WHITE: 6,
        Color.BLACK: 4,
    }
]


def urn_probability(drawn: tuple[Color]):
    single_urn_probability = 1 / len(urns)
    full_drawn_probability = sum(
        probability(drawn, urn)
        for urn in urns
    ) * single_urn_probability
    logger.debug(f'full_drawn_probability({drawn}) = {full_drawn_probability}')

    return {
        tuple(urn.items()): single_urn_probability * probability(drawn, urn) / full_drawn_probability
        for urn in urns
    }


def certainty(drawn: tuple[Color]):
    return max(urn_probability(drawn).values())


def probability(drawn: tuple[Color], urn: UrnType):
    urn_size = sum(urn.values())
    result = 1
    for color in drawn:
        result *= urn[color] / urn_size
    return result


def main():
    for urn in urns:
        print(f'{urn}: {probability((Color.WHITE,), urn)}')


if __name__ == '__main__':
    main()
