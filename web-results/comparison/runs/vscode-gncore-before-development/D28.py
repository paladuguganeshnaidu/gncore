def check_contract(fn):
    assert fn(0) == 0
    assert fn(50) == 50
    assert fn(100) == 100
    assert fn(-1) == 0
    assert fn(-1000) == 0
    assert fn(101) == 100
    assert fn(1000) == 100

    for invalid in (1.5, "50", None, [], {}, True, False):
        try:
            fn(invalid)
        except TypeError:
            pass
        except Exception as error:
            raise AssertionError("wrong exception type") from error
        else:
            raise AssertionError("invalid input was accepted")