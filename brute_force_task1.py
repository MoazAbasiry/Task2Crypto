import itertools
import string

def decrypt_monoalphabetic(ciphertext, key):
    alphabet = string.ascii_lowercase
    key_map = {k: v for k, v in zip(key, alphabet)}
    return ''.join(key_map.get(c, c) for c in ciphertext)

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_lowercase
    for perm in itertools.permutations(alphabet):
        key = ''.join(perm)
        decrypted_text = decrypt_monoalphabetic(ciphertext, key)
        print(f"Key: {key} -> Decrypted: {decrypted_text}")

cipher_text = "encryptedmessage"
print("Brute Force (only first few keys):")
