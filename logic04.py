def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a: int
        b: int
    Returns:
        True if each of the numbers 'a' and 'b' is even, False otherwise
    """
    a%=2
    b%=2
    return a==0 and b==0
x=main(8,6) 
print(x)