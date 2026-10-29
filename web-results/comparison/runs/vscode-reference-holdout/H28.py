def check_contract(fn):
    assert fn(1) == 1
    assert fn(65535) == 65535
    assert fn(42) == 42

    for value in (0, 65536, -1):
        try:
            fn(value)
        except ValueError:
            pass
        else:
            assert False, "out-of-range integer was accepted"

    for value in (True, False, 1.5, "80", None):
        try:
            fn(value)
        except TypeError:
            pass
        else:
            assert False, "invalid type was accepted"