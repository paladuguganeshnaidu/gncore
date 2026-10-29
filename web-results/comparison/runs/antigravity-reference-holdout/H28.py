def check_contract(fn):
    def assert_valid(val, expected):
        res = fn(val)
        assert res == expected, f"Expected {expected}, got {res}"
        assert type(res) is int and not isinstance(res, bool), "Return must be int, not bool"

    def assert_raises(val, expected_exc):
        try:
            fn(val)
        except expected_exc:
            return
        except Exception as e:
            raise AssertionError(f"Expected {expected_exc.__name__} for {val!r}, got {type(e).__name__}") from e
        raise AssertionError(f"Expected {expected_exc.__name__} for {val!r}, but no exception was raised")

    # Boundary and positive valid cases
    assert_valid(1, 1)
    assert_valid(65535, 65535)
    assert_valid(80, 80)
    assert_valid(443, 443)
    assert_valid(8080, 8080)

    # Out of range integer cases (ValueError)
    assert_raises(0, ValueError)
    assert_raises(-1, ValueError)
    assert_raises(-80, ValueError)
    assert_raises(65536, ValueError)
    assert_raises(70000, ValueError)

    # Invalid types (TypeError)
    assert_raises(True, TypeError)
    assert_raises(False, TypeError)
    assert_raises(80.0, TypeError)
    assert_raises(1.0, TypeError)
    assert_raises("80", TypeError)
    assert_raises(None, TypeError)
    assert_raises([80], TypeError)
    assert_raises((80,), TypeError)