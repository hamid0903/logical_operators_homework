def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a: int
    Returns:
        True if all digits sum is even, False otherwise
    """
    a1=a%10
    a2=a//10
    a=(a1+a2)%2
    return a==0
x=main(13)
print(x)