from enum import Enum, auto


def hello() -> str:
    return "Hello from neural-chaos!"


class Precision(Enum):
    EXACT = auto()
    NUMERIC = auto()
    PHYSICAL = auto()
    BIOLOGICAL = auto()


def equals(a: float, b: float, precision: Precision = Precision.EXACT) -> bool:
    match precision:
        case Precision.EXACT:
            return abs(a - b) == 0.0
        case Precision.NUMERIC:
            return abs(a - b) < 1e-6
        case Precision.PHYSICAL:
            return abs(a - b) < 1e-3
        case Precision.BIOLOGICAL:
            return abs(a - b) < 1e-1
