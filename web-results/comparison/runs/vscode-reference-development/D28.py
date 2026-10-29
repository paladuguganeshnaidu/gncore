def check_contract(fn):
    assert callable(fn)

    cases = [
        (-100, 0),
        (-1, 0),
        (0, 0),
        (1, 1),
        (50, 50),
        (99, 99),
        (100, 100),
        (101, 100),
        (10**12, 100),
    ]
    for value, expected in cases:
        result = fn(value)
        assert type(result) is int
        assert result == expected

    for invalid in (True, False, 1.0, -1.0, "50", None, [], {}, object()):
        try:
            fn(invalid)
        except TypeError:
            pass
        else:
            assert False, "invalid input did not raise TypeError"

    return None