from math import log2
from fractions import Fraction

def float_to_bin(v):
    f = Fraction(str(v))
    e = log2(f.denominator)
    assert e == int(e), '有限の２進数で表現できません'
    e = int(e)
    s = bin(f.numerator)
    return s[2:-e] + '.' + s[-e:]
