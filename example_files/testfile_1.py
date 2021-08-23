def longestUniqueSubsttr(string):
    last_idx = {}
    max_len = 0

    start_idx = 0

    for i in range(0, len(string)):
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)
        max_len = max(max_len, i-start_idx + 1)

        last_idx[string[i]] = i

    return max_len

def sum_of_digits(n):

    s = 0
    while n > 0:
        s, n = s + n%10, n//10
    return s

def prime_gen(max_value=10000):
    listSieve = []
    sieve = [True] * max_value
    for p in range(2, max_value):
        if sieve[p]:
            listSieve.append(p)
            for i in range(p*p, max_value, p):
                sieve[i] = False
    return listSieve


def unpack_bytes_to_double(self, bytes):

    return struct.unpack("d", bytes)[0]
