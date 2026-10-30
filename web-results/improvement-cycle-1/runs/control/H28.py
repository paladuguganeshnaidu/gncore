def check_contract(fn):
    def expect_error(value, expected):
        try:
            fn(value)
        except expected:
            return
        except Exception as exc:
            raise AssertionError(
                'wrong exception for {!r}: expected {}, got {}'.format(
                    value, expected.__name__, type(exc).__name__
                )
            ) from exc
        raise AssertionError(
            'expected {} for {!r}'.format(expected.__name__, value)
        )

    for value in (1, 2, 80, 443, 1024, 32768, 65534, 65535):
        result = fn(value)
        assert isinstance(result, int) and not isinstance(result, bool), (
            'result must remain an integer for {!r}'.format(value)
        )
        assert result == value, 'valid port changed: {!r}'.format(value)

    for value in (True, False, None, '80', '', 80.0, 1.5,
                  b'80', [], {}, (), set(), 1 + 0j):
        expect_error(value, TypeError)

    for value in (-10**100, -65535, -1, 0, 65536, 65537, 10**100):
        expect_error(value, ValueError)
