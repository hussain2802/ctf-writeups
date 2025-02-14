

# This file was *autogenerated* from the file solve_mod.sage
from sage.all_cmdline import *   # import sage library

_sage_const_65537 = Integer(65537); _sage_const_2374924730695331980666696108116881030499766801250410405192548099790203981209 = Integer(2374924730695331980666696108116881030499766801250410405192548099790203981209); _sage_const_24061514671443903391690548449273614205558035441569029488091015203490263562130 = Integer(24061514671443903391690548449273614205558035441569029488091015203490263562130); _sage_const_1 = Integer(1); _sage_const_128 = Integer(128); _sage_const_2 = Integer(2)
e = _sage_const_65537 
d = _sage_const_2374924730695331980666696108116881030499766801250410405192548099790203981209 
ct = _sage_const_24061514671443903391690548449273614205558035441569029488091015203490263562130 

phi = (e*d)-_sage_const_1 

list = []
for a,b in factor(phi):
	for _ in range(b):
		list.append(a)

primes = []

print("factoing primes using combinations")
for i in range(len(list)):
	for comb in Combinations(list,i):
		prod = product(comb)
		if is_prime(prod + _sage_const_1 ):
			prime = prod + _sage_const_1 
			if prime.nbits() == _sage_const_128 :
				primes.append(prime)

print(primes)
print("decrypting cipher")

for vals in Combinations(primes):
	n = product(vals)
	try:
		m = bytes.fromhex(hex(pow(ct,d,n))[_sage_const_2 :]).decode()
		if m.isalnum():
			print(m)
			break
	except:
		pass

