def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    a1=pow(0,a)
    a//=10
    a2=pow(0,a)
    a//=10
    a3=pow(0,a)
    a//=10
    a4=pow(0,a)
    a//=10
    a5=pow(0,a)
    a=(a1+a2+a3+a4+a5)
    return a==0
x=main(12345)
print(x)