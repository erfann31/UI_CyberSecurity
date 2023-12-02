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


# Kasiski Examination for finding key length
def kasiski_examination(ciphertext):
    repeated_sequences = {}
    for i in range(len(ciphertext) - 3):
        sequence = ciphertext[i:i + 3]
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


# Function to determine probable key length


# Example usage
plaintext = "CRYPTO IS SHORT FOR CRYPTOGRAPHY. "
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)


