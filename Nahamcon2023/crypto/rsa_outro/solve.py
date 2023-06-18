import sympy
from Crypto.Util.number import isPrime

e = 65537
d = 53644719720574049009405552166157712944703190065471668628844223840961631946450717730498953967365343322420070536512779060129496885996597242719829361747640511749156693869638229201455287585480904214599266368010822834345022164868996387818675879350434513617616365498180046935518686332875915988354222223353414730233
phi = 245339427517603729932268783832064063730426585298033269150632512063161372845397117090279828761983426749577401448111514393838579024253942323526130975635388431158721719897730678798030368631518633601688214930936866440646874921076023466048329456035549666361320568433651481926942648024960844810102628182268858421164
ct = 37908069537874314556326131798861989913414869945406191262746923693553489353829208006823679167741985280446948193850665708841487091787325154392435232998215464094465135529738800788684510714606323301203342805866556727186659736657602065547151371338616322720609504154245460113520462221800784939992576122714196812534

# p = 2*q + 1
#phi = (p-1)*(q-1)
#phi = (2*q+1-1)*(q-1)
#phi = 2*q(q-1)
#phi = 2*(q^2) - 2q
#2*(q^2) - 2q - phi = 0

a = 2
b = -2
c = -abs(phi)

x=sympy.Symbol('x')
q = int(max(sympy.solve(a*x**2 + b*x + c, x)))
p = 2*q + 1

assert isPrime(q)
assert isPrime(p)
assert phi == (p-1)*(q-1)

n = p*q
m = pow(ct,d,n)

print(bytes.fromhex(hex(m)[2:]).decode().strip())

#flag{8b76b85e7f450c39502e71c215f6f1fe}