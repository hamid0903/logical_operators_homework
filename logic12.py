def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a: int
    Returns:
        True if all digits of a are the same, False otherwise
    """
    a1=a%10
    a//=10
    print(a,a1)
    return a==a1
x=main(12)
print(x)