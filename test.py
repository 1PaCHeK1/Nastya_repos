
def f(a, b, c):    
    assert isinstance(a, str), "a is not str"
    assert isinstance(b, str), "b is not str"
    assert isinstance(c, str), "c is not str"

f('1', '`2`', '3')