# Pybeat test module

# A pybeat module must contain a setup method, which is called when pybeat
# imports the module.
#
# - The first argument is the sampling rate in Hz.
# - The second argument is the length in seconds of the render. If pybeat is
#   set to stream the bytes directly to stdout, this is None.
# - Other arguments can be passed at the command line.
#
# The setup method must return an update method. This must take a single
# argument, t (for the current sample number), and return a number (which will
# be rounded and truncated to a byte by pybeat).
def setup(hz, wlen, a_tune=440, *_):
    from math import *

    a_tune = int(a_tune)
    note=lambda n: a_tune*2**((n-69)/12)/hz
    sine=lambda n:lambda t:sin(t*note(n)*2*pi)

    return lambda t: 127 + (~(t>>13)&1)*20*sine(ord('EGHJGGCE'[(t>>10)%8]))(t)
