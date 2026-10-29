def check_contract(fn):
    test_cases = [
        (-100, 0),
        (-1, 0),
        (0, 0),
        (1, 1),
        (50, 50),
        (99, 99),
        (100, 100),
        (101, 100),
        (250, 100),
    ]
    for inp, expected in test_cases:
        res = fn(inp)
        assert res == expected, f"Expected {expected} for input {inp}, got {res}"
        assert type(res) is int and type(res) is not bool, f"Expected int return type for {inp}, got {type(res)}"

    invalid_inputs = [True, False, 0.0, 50.5, 100.0, "50", None, [], {}, (1,)]
    for invalid in invalid_inputs:
        raised = False
        try:
            fn(invalid)
        except TypeError:
            raised = True
        except Exception as e:
            raise AssertionError(f"Expected TypeError for {invalid!r}, but raised {type(e).__name__}")
        if not raised:
            raise AssertionError(f"Expected TypeError for {invalid!r}, but no exception was raised")
    return True
