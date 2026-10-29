def check_contract(fn):
    assert fn(1) == 1
    assert fn(32768) == 32768
    assert fn(65535) == 65535

    for value in (0, 65536, -1):
        try:
            fn(value)
        except ValueError:
            pass
        else:
            raise AssertionError("out-of-range integer was accepted")

    for value in (True, False, 1.0, "80", None, object()):
        try:
            fn(value)
        except TypeError:
            pass
        else:
            raise AssertionError("invalid type was accepted")