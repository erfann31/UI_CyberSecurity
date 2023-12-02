import math
import collections

# Define the alphabet and its length
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_len = len(alphabet)

def mod_inverse(a, m):
    # Calculate the modular multiplicative inverse of 'a' mod 'm'
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            p = alphabet.index(char)
            c = (a * p + b) % alphabet_len
            ciphertext += alphabet[c]
        else:
            ciphertext += char  # Leave non-alphabet characters unchanged
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = mod_inverse(a, alphabet_len)
    if a_inverse is None:
        return "The provided 'a' value is not coprime to the alphabet length."

    for char in ciphertext:
        if char in alphabet:
            c = alphabet.index(char)
            p = (a_inverse * (c - b)) % alphabet_len
            plaintext += alphabet[p]
        else:
            plaintext += char  # Leave non-alphabet characters unchanged
    return plaintext

def frequency_analysis(ciphertext):
    # Calculate letter frequencies in the ciphertext
    letter_counts = collections.Counter(ciphertext)
    return letter_counts

def statistical_attack(ciphertext):
    letter_frequencies = frequency_analysis(ciphertext)
    most_common_letter = max(letter_frequencies, key=letter_frequencies.get)
    a_inverse = mod_inverse(a, alphabet_len)
    b = (alphabet.index(most_common_letter) - a_inverse * alphabet.index('E')) % alphabet_len
    return a_inverse, b

def brute_force_attack(ciphertext):
    possible_plaintexts = []
    for a in range(1, alphabet_len):
        if math.gcd(a, alphabet_len) == 1:
            for b in range(alphabet_len):
                possible_plaintext = affine_decrypt(ciphertext, a, b)
                possible_plaintexts.append((a, b, possible_plaintext))
    return possible_plaintexts

# Test:
# plaintext = "ALGORITHMSAREQUITEGENERALDEFINITIONSOFARITHMETICPROCESSES"
plaintext = "HELLOWORLD"
a = 3
b = 5
ciphertext = affine_encrypt(plaintext, a, b)
print("Plain Text:", plaintext)
print(f"a: {a} , b: {b}")
print("Encrypted:", ciphertext)

if len(ciphertext) > 16:
    # Perform statistical attack three times
    for i in range(3):
        print(f"\nStatistical Attack {i + 1}:")
        a_inverse, b = statistical_attack(ciphertext)
        print(f"a_inverse={a_inverse}, b={b}")
        decrypted_text = affine_decrypt(ciphertext, a_inverse, b)
        print("Decrypted:", decrypted_text)
        ciphertext = affine_encrypt(decrypted_text, a, b)  # Use the decrypted text for the next attack

else:
    # Perform brute-force attack
    print("\nBrute Force Attack:")
    possible_plaintexts = brute_force_attack(ciphertext)
    for a, b, possible_plaintext in possible_plaintexts:
        print(f"a={a}, b={b}: {possible_plaintext}")
