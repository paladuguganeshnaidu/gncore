def check_contract(fn):
    class PortInteger(int):
        pass

    for value in (1, 2, 22, 80, 443, 1024, 32768, 65534, 65535,
                  PortInteger(8080)):
        actual = fn(value)
        assert isinstance(actual, int) and not isinstance(actual, bool), (
            "valid port must return an integer", value, actual
        )
        assert actual == value, ("port changed", value, actual)

    def raises(expected, value):
        try:
            fn(value)
        except expected:
            return
        raise AssertionError(("expected exception", expected.__name__, value))

    for value in (0, -1, -65535, -(10 ** 100), 65536, 65537, 10 ** 100):
        raises(ValueError, value)

    for value in (
        True, False, None, "", "1", "443", "65535", " 80 ",
        1.0, 443.0, 65535.0, -1.5, 0.0, float("nan"),
        float("inf"), b"80", 80 + 0j, [], [80], (), {}, {80}, object()
    ):
        raises(TypeError, value)
