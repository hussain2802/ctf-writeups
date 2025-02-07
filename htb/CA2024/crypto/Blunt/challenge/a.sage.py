

# This file was *autogenerated* from the file a.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0xdd6cc28d = Integer(0xdd6cc28d); _sage_const_0x83e21c05 = Integer(0x83e21c05); _sage_const_0xcfabb6dd = Integer(0xcfabb6dd); _sage_const_0xc4a21ba9 = Integer(0xc4a21ba9)
p = _sage_const_0xdd6cc28d 
g = _sage_const_0x83e21c05 
A = _sage_const_0xcfabb6dd 
B = _sage_const_0xc4a21ba9 

R = IntegerModRing(p)

#A = g^a %p
#B = g^b %p

a = discrete_log(R(A),R(g))
b = discrete_log(R(B),R(g))

print(f"Private Key a: {a}")
print(f"Private Key b: {b}")


C = pow(A, b, p)
assert C == pow(B, a, p)

print(f"Shared Secret: {C}")

