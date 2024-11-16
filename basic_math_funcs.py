# Calculate a^b mod m
def powMod(a, b, m):
	x = []
	while b != 0:
		x.append(b & 1)
		b = b >> 1
	sz = len(x)
	po = [a%m]
	for i in range(1,sz):
		p = (po[i-1]*po[i-1])%m
		po.append(p)
	r = 1
	for i in range(sz):
		if(x[i] != 0):
			r*= po[i]
			r%= m
	return r

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# return gcd,x,y where a.x + b.y = gcd
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd( b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# return e^-1 (mod phi)
def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

if __name__ == "__main__":
	a = 7
	b = 5
	c = 8
	gcd0 = gcd(a,b)
	gcd1, x, y = extended_gcd(a,b)
	mod_inverse = mod_inverse(a, b)
	r = powMod(a,b,c)


	print(f"With a = {a}, b = {b}, c = {c}, we have: ")
	print(f"gcd(a, b) = {gcd0}")
	print(f"x = {x}, y = {y}, such that: a.x + b.y = {gcd1}")
	print(f"modular inverse of a in GF(b) is {mod_inverse}")
	print(f"a^b mod c = {r}")