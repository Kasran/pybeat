from math import *

def setup(*args):
    HZ = 8000
    note=lambda n: 440*2**((n-69)/12)/HZ
    sine=lambda n:lambda t:sin(t*note(n)*2*pi)

    return lambda t: 127 + (~(t>>13)&1)*20*sine(ord('EGHJGGCE'[(t>>10)%8]))(t)
