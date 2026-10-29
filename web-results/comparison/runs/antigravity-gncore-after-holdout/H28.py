def check_contract(fn):
    for val in (1, 2, 80, 443, 8080, 65534, 65535):
        res = fn(val)
        assert res == val, f"Expected {val}, got {res}"
        assert type(res) is int, f"Expected int return type, got {type(res)}"
        assert not isinstance(res, bool), "Return value must not be bool"

    for val in (0, -1, -80, 65536, 65537, 100000):
        try:
            fn(val)
        except ValueError:
            pass
        except Exception as e:
            raise AssertionError(f"Expected ValueError for {val}, got {type(e).__name__}")
        else:
            raise AssertionError(f"Expected ValueError for {val}, but no exception was raised")

    for val in (True, False, None, "80", "1", 80.0, 1.0, [80], (80,), {"port": 80}):
        try:
            fn(val)
        except TypeError:
            pass
        except Exception as e:
            raise AssertionError(f"Expected TypeError for {val!r}, got {type(e).__name__}")
        else:
            raise AssertionError(f"Expected TypeError for {val!r}, but no exception was raised")