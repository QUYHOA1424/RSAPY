import random

def is_Prime(n, loop_times = 10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # (n - 1) = (2^k) * q
    k = 0
    q = n - 1
    while q % 2 == 0:
        k = k + 1
        q = q // 2
    # test(n)
    for _ in range(loop_times):
        a = random.randint(1, n - 1)
        x = powMod(a, q, n)  # a^q % n = a^(2^0 * q) % n
        if x == 1 or x == (n - 1):
            continue
        for _ in range(1, k - 1):
            x = powMod(x, 2, n) # x = a^(2^i * q) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def create_large_Prime(bit_length = 500):
    while True:
        random_num = random.getrandbits(bit_length)
        if random_num == 2:
            continue
        random_num = random_num | (1 << (bit_length - 1)) # OR-bitwise: ensure MSB is 1 -> number is exactly 500bit
        random_num = random_num | 1 # OR-bitwise: ensure LSB is 1 -> odd
        if is_Prime(random_num):
            return random_num
        
def generate_rsa_keypair(bit_length = 500):
    # Generate two large prime numbers
    p = create_large_Prime(bit_length)
    q = create_large_Prime(bit_length)
    while p == q:
        q = create_large_Prime(bit_length)
    # n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    # Choose  e randomly coprime with phi
    e = None
    if gcd(65537, phi) == 1:
        e = 65537 # ususally use
    else:
        for e in range(3, phi - 1):
            if gcd(e, phi) == 1:
                break
        if e is None:
            raise ValueError('Unable to find an e coprime with phi.')
    # Compute d (the modular inverse of e)
    d = mod_inverse(e, phi)
    # Return the keypair
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# test with small value
def generate_rsa_keypair_test(p, q, bit_length = 5):
    while p == q:
        q = create_large_Prime(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = None
    for e in range(3, phi - 1):
        if gcd(e, phi) == 1:
            break
    if e is None:
        raise ValueError('Unable to find an e coprime with phi.')
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# Example
if __name__ == "__main__":
    # test
    public_key, private_key = generate_rsa_keypair_test(5, 11, 5)
    print("Test result: ")
    print("    Public key:", public_key)
    print("    Private key:", private_key)
    # actual use
    public_key, private_key = generate_rsa_keypair(512)
    print("Result: ")
    print("    Public key:", public_key)
    print("    Private key:", private_key)
        
