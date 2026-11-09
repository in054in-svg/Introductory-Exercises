def c_to_f(celsius):
    return celsius * 1.8 + 32

def describe(celsius):
    if celsius > 30:
        return 'hot'
    elif celsius < 15:
        return 'cold'
    else:
        return 'pleasant'