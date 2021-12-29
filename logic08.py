def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a: int
        b: int
    Returns:
        True if at least one of the numbers 'a' and 'b' is even, False otherwise
    """
    a%=2
    b%=2
    return a==0 or b==0
x=main(5,6)
print(x)