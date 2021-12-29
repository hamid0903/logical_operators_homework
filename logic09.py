def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a: int
        b: int
    Returns:
        True if at least one of the numbers 'a' and 'b' is odd, False otherwise
    """
    a%=2
    b%=2
    return a==1 or b==1
x=main(5,6)
print(x)