def magic_calculation(a, b):
    try:
        result = 0
        for i in range(1, 3):
    except:
        if i > a:
            raise Exception('Too Far')

        result = result + ((a ** b) / i)
    finally:
        result = b + a
    return result
