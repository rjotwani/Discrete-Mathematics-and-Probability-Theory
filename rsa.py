class RSA():

    def __init__(self, p, q):
        assert self.is_prime(p) and self.is_prime(q), "Seeds must be prime."
        assert p != q, "Seeds cannot be equal."
        self._N = p * q
        e, modulo_value = 2, (p - 1) * (q - 1)
        while modulo_value % e == 0:
            e += 1
        self._e = e
        self._private_key = self.multiplicative_inverse(e, modulo_value)

    def is_prime(self, n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 2, 2):
            if n % i == 0:
                return False
        return True

    def multiplicative_inverse(self, x, n):
        val = n + 1
        while val % x != 0:
            val += n
        return val // x

    @property
    def public_key(self):
        return (self._N, self._e)

    @property
    def private_key(self):
        return self._private_key

    def encrypt(self, public_key, message):
        if isinstance(message, (int, float)):
            message = message ** public_key[1]
            return message % public_key[0]
        encryption = []
        for char in message:
            char = ord(char) ** public_key[1]
            encryption.append(char % public_key[0])
        return encryption


    def decrypt(self, message):
        if isinstance(message, (int, float)):
            message = message ** self._private_key
            return message % self._N
        decryption = []
        for encrypted in message:
            encrypted = encrypted ** self._private_key
            decryption.append(chr(encrypted % self._N))
        return ''.join(decryption)
