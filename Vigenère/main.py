# Vigenère encryption
def vigenere_encrypt(plaintext, key):
    encrypted_text = ''
    key_length = len(key)
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length]) - 65  # Assuming uppercase letters
        if plaintext[i].isalpha():
            encrypted_char = chr(((ord(plaintext[i]) - 65 + shift) % 26) + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += plaintext[i]
    return encrypted_text


# Vigenère decryption
def vigenere_decrypt(ciphertext, key):
    decrypted_text = ''
    key_length = len(key)
    for i in range(len(ciphertext)):
        shift = ord(key[i % key_length]) - 65  # Assuming uppercase letters
        if ciphertext[i].isalpha():
            decrypted_char = chr(((ord(ciphertext[i]) - 65 - shift) % 26) + 65)
            decrypted_text += decrypted_char
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text


# Frequency Analysis Attack
def frequency_analysis(ciphertext):
    letter_frequencies = {}
    for letter in ciphertext:
        if letter.isalpha():
            if letter in letter_frequencies:
                letter_frequencies[letter] += 1
            else:
                letter_frequencies[letter] = 1

    # Sort frequencies
    sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequencies


# Kasiski Examination
def kasiski_examination(ciphertext, key_length):
    repeated_sequences = {}
    for i in range(len(ciphertext) - key_length):
        sequence = ciphertext[i:i + key_length]
        if sequence in repeated_sequences:
            repeated_sequences[sequence].append(i)
        else:
            repeated_sequences[sequence] = [i]

    repeated_sequences = {k: v for k, v in repeated_sequences.items() if len(v) > 1}

    distances = {}
    for seq, indices in repeated_sequences.items():
        for i in range(len(indices) - 1):
            distance = indices[i + 1] - indices[i]
            if distance not in distances:
                distances[distance] = [seq]
            else:
                distances[distance].append(seq)

    return distances


# Known Plaintext Attack
def known_plaintext_attack(plaintext, ciphertext):
    possible_keys = []
    for i in range(len(plaintext)):
        key_char = chr(((ord(ciphertext[i]) - ord(plaintext[i])) % 26) + 65)
        possible_keys.append(key_char)

    return ''.join(possible_keys)


# Example usage
plaintext = "CRYPTO IS SHORT FOR CRYPTOGRAPHY".upper()
key = "ABCD"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

# Test the attacks

# Frequency Analysis Attack
freq_analysis_result = frequency_analysis(encrypted_text)
print("\nFrequency Analysis Result:")
print(freq_analysis_result)

# Kasiski Examination
kasiski_result = kasiski_examination(encrypted_text, 4)
print("\nKasiski Examination Result:")
print(kasiski_result)

# Known Plaintext Attack
known_plaintext_result = known_plaintext_attack(plaintext, encrypted_text)
print("\nKnown Plaintext Attack Result:")
print("Probable key: ",known_plaintext_result)
