def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a: int
    Returns:
        True if all digits sum is odd, False otherwise
    """
    a1=a%10
    a//=10
    a2=a%10
    a3=a//10
    a=(a1+a2+a3)%2
    return a==1
x=main(123)
print(x)