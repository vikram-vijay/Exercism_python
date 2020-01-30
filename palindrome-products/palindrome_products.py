def largest(min_factor, max_factor):
    return is_palindrome(min_factor, max_factor, small=False)


def smallest(min_factor, max_factor):
    return is_palindrome(min_factor, max_factor)


def is_palindrome(min_factor, max_factor, small=True):
    if min_factor > max_factor:
        raise ValueError("min_factor should be less than of equal to max_factor")
    args = (min_factor ** 2, max_factor ** 2 + 1) if small else (max_factor ** 2, min_factor ** 2 - 1, -1)

    for num in range(*args):
        num_str = str(num)
        if num_str == num_str[::-1] and any(
                min_factor <= num // var1 <= max_factor for var1 in range(min_factor, max_factor + 1) if
                num % var1 == 0):
            return num, ((var2, num // var2) for var2 in range(min_factor, max_factor + 1) if
                         num % var2 == 0 and min_factor <= var2 <= num // var2 <= max_factor)
    return None, []