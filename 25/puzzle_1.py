import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def convert_to_base_10(number: str) -> int:
    """Convert a number in the SNAFU numbering system to base 10.

    Args:
        number (str): Number in SNAFU format.

    Returns:
        int: Number in 10 base format.
    """
    retval = 0
    for i, digit in enumerate(reversed(number)):
        digit_value = SNAFU.index(digit) - 2
        retval += digit_value * 5**i
    return retval

def convert_to_base_snafu(number: int) -> str:
    """Convert a base ten number to the SNAFU numbering system.

    Args:
        number (int): Number in 10 base format.

    Returns:
        str: Number in SNAFU format.
    """
    retval = ""
    while number:
        number, rest = divmod(number + 2, 5)
        retval = SNAFU[rest] + retval
    return retval

if __name__ == "__main__":
    with open(os.path.join(__location__,"input.txt")) as file:
        SNAFU = "=-012"
        lines = [convert_to_base_10(line) for line in (l.strip() for l in file)]
        print(convert_to_base_snafu(sum(lines)))