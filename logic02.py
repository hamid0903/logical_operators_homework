def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is positive".
    Args:
        a: int
        b: int
    Returns:
        True if each of the numbers 'a' and 'a' is positive, False otherwise
    """
    return a>0 and b>0
x=main(5,6)
print(x)