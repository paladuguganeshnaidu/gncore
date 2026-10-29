def check_contract(fn):
    # Test valid in-range integers
    for val in (0, 1, 50, 99, 100):
        res = fn(val)
        if type(res) is not int or type(res) is bool:
            raise AssertionError(f"Expected int return type for {val}, got {type(res)}")
        if res != val:
            raise AssertionError(f"Expected {val} to return {val}, got {res}")
            
    # Test clamping below 0
    for val in (-1, -50, -1000):
        res = fn(val)
        if type(res) is not int or type(res) is bool:
            raise AssertionError(f"Expected int return type for {val}, got {type(res)}")
        if res != 0:
            raise AssertionError(f"Expected {val} to clamp to 0, got {res}")
            
    # Test clamping above 100
    for val in (101, 150, 1000):
        res = fn(val)
        if type(res) is not int or type(res) is bool:
            raise AssertionError(f"Expected int return type for {val}, got {type(res)}")
        if res != 100:
            raise AssertionError(f"Expected {val} to clamp to 100, got {res}")
            
    # Test rejection of non-integer and bool inputs with TypeError
    invalid_inputs = (True, False, 0.0, 50.5, 100.0, "50", None, [50], (50,), {"val": 50})
    for bad in invalid_inputs:
        try:
            fn(bad)
        except TypeError:
            pass
        except Exception as e:
            raise AssertionError(f"Expected TypeError for {bad!r}, got {type(e).__name__}")
        else:
            raise AssertionError(f"Expected TypeError for {bad!r}, but no exception was raised")
