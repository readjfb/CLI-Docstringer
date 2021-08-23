def longestUniqueSubsttr(string):
    """
    Returns the length of the longest substring of a string without repeating characters.

    Parameters:
        string (str): A string

    Returns:
        max_len (int): The length of the longest substring of string without repeating characters
    """
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
    """
    Returns the sum of the digits of an integer number using loops.

    Parameters:
        n (int): An integer number

    Returns:
        s (int): The sum of the digits of n
    """

    s = 0
    while n > 0:
        s, n = s + n%10, n//10
    return s

def prime_gen(max_value=10000):
    """
    Returns a list of prime numbers up to a maximum value using a sieve.

    Parameters:
        max_value (int) (default=10000): The maximum value to be used in the sieve

    Returns:
        listSieve (list): A list of prime numbers up to max_value
    """
    listSieve = []
    sieve = [True] * max_value
    for p in range(2, max_value):
        if sieve[p]:
            listSieve.append(p)
            for i in range(p*p, max_value, p):
                sieve[i] = False
    return listSieve


def unpack_bytes_to_double(self, bytes):
    """
    Unpacks a byte string into a double

    Parameters:
        bytes (bytes): A byte string

    Returns:
        (float): The unpacked double
    """

    return struct.unpack("d", bytes)[0]
