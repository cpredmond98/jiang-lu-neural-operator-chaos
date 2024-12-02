from neural_chaos import Precision, equals


def test_fuzzy_equality():
    assert equals(1.0, 1.0, Precision.EXACT)

    assert equals(1.0, 1.0 + 1e-7, Precision.NUMERIC)
    assert not equals(1.0, 1.0 + 1e-7, Precision.EXACT)

    assert equals(1.0, 1.05, Precision.BIOLOGICAL)
    assert not equals(1.0, 1.05, Precision.PHYSICAL)

    assert equals(1.0, 1.0 + 1e-4, Precision.PHYSICAL)
