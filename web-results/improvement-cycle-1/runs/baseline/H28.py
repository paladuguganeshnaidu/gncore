def check_contract(fn):
    class IntegerSubclass(int):
        pass

    def valid(value):
        result = fn(value)
        assert isinstance(result, int) and not isinstance(result, bool), (value, result)
        assert result == value, (value, result)

    def raises(value, expected):
        try:
            fn(value)
        except Exception as error:
            assert isinstance(error, expected), (value, expected, type(error))
        else:
            raise AssertionError(('expected exception', value, expected))

    for value in (1, 2, 80, 443, 1024, 32768, 65534, 65535, IntegerSubclass(8080)):
        valid(value)
    for value in (0, -1, -65535, 65536, 65537, 10 ** 100):
        raises(value, ValueError)
    for value in (True, False, None, '80', '', b'80', 1.0, 65535.0, 0.0,
                  -1.0, float('nan'), float('inf'), 80 + 0j, [], {}, (), set()):
        raises(value, TypeError)
    valid(1)
    valid(65535)
    valid(8080)
