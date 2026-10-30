def check_contract(fn):
    class PortInteger(int):
        pass

    for value in (1, 2, 80, 443, 32768, 65534, 65535, PortInteger(8080)):
        result = fn(value)
        assert isinstance(result, int) and not isinstance(result, bool), (
            "valid port must return an integer", value, result
        )
        assert result == value, ("valid port changed", value, result)

    for value in (0, -1, -(10 ** 40), 65536, 65537, 10 ** 40):
        try:
            fn(value)
        except ValueError:
            pass
        else:
            raise AssertionError(("expected ValueError", value))

    for value in (True, False, None, "80", "", 80.0, 1.0, 65535.0,
                  b"80", [], {}, (), 80 + 0j):
        try:
            fn(value)
        except TypeError:
            pass
        else:
            raise AssertionError(("expected TypeError", value))
