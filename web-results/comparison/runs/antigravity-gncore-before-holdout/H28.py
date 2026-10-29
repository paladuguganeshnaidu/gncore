def check_contract(fn):
    # Positive and boundary cases
    for port in (1, 2, 80, 443, 8080, 65534, 65535):
        res = fn(port)
        assert res == port, f"Expected {port}, got {res!r}"

    # Invalid types: must raise TypeError (including bool)
    for invalid_type_val in (True, False, "80", 80.0, None, [80], (80,), {"port": 80}):
        try:
            fn(invalid_type_val)
        except TypeError:
            pass
        except Exception as e:
            raise AssertionError(f"Expected TypeError for {invalid_type_val!r}, got {type(e).__name__}")
        else:
            raise AssertionError(f"Expected TypeError for {invalid_type_val!r}, but no exception was raised")

    # Out of range integers: must raise ValueError
    for out_of_range_val in (0, -1, -80, 65536, 65537, 100000):
        try:
            fn(out_of_range_val)
        except ValueError:
            pass
        except Exception as e:
            raise AssertionError(f"Expected ValueError for {out_of_range_val!r}, got {type(e).__name__}")
        else:
            raise AssertionError(f"Expected ValueError for {out_of_range_val!r}, but no exception was raised")