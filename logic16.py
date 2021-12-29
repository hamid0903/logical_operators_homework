def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    x1=pow(0,a)
    a//=10
    x2=pow(0,a)
    a//=10
    x3=pow(0,a)
    a//=10
    x4=pow(0,a)
    a//=10
    x5=pow(0,a)
    a=5-(x1+x2+x3+x4+x5)
    return a==5
x=main(1234)
print(x)