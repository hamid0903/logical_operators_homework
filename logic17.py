def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a: int
    Returns:
        True if all digits of a are in ascending order, False otherwise
    """
    a1=a%10
    a//=10

    a2=a%10
    a//=10

    a3=a%10
    a//=10

    a4=a%10
    a5=a//10    
    print(a5,a4,a3,a2,a1)
    return a5>a4>a3>a2>a1
x=main(12345)
print(x)