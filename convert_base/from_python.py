from string import ascii_lowercase, ascii_uppercase, digits

def convert(num, from_base, to_base, digits_list=digits+ascii_uppercase+ascii_lowercase+'_-'):
    if not hasattr(digits_list, '__iter__'):
        raise ValueError(f"Object of type {type(digits_list).__name__} cannot be expressed as a list")
    digits_list = list(digits_list)
    if not isinstance(from_base, int) and isinstance(to_base, int):
        raise ValueError(f"Expected (int, int) as bases; got {(type(from_base).__name__, type(to_base).__name__)}")
    if not 2 <= from_base < len(digits_list) and 2 <= to_base < len(digits_list):
        raise ValueError(f"Expected bases between 2 and {len(digits_list)}; got {(from_base, to_base)}")
    n = 0
    for i, char in enumerate(reversed(str(num))):
        if char not in digits_list:
            raise ValueError(f"Sequence item {i}: {char!r} not in digits")
        n += from_base**i * digits_list.index(char)
    ret = ''
    while n:
        ret += str(int(n % to_base))
        n //= to_base
    return ret[::-1]
