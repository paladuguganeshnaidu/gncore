def check_contract(fn):
    assert fn(1) == 1
    assert fn(32768) == 32768
    assert fn(65535) == 65535

    def expect(exception_type, value):
        try:
            fn(value)
        except exception_type:
            return
        except Exception as error:
            raise AssertionError("wrong exception type") from error
        raise AssertionError("expected an exception")

    for value in (0, -1, 65536, 10**100):
        expect(ValueError, value)
    for value in (True, False, 1.0, "80", None, [], {}, object()):
        expect(TypeError, value)