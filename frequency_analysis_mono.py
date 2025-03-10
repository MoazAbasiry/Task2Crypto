import collections

def frequency_analysis(ciphertext):
    english_freq = 'etaoinshrdlcumwfgypbvkjxqz'  
    cipher_freq = collections.Counter(ciphertext)
    cipher_sorted = ''.join([pair[0] for pair in cipher_freq.most_common()])
    key_map = {cipher_sorted[i]: english_freq[i] for i in range(len(cipher_sorted))}
    return ''.join(key_map.get(c, c) for c in ciphertext)


cipher_text = "encryptedmessage"
print("\nFrequency Analysis:")
print(frequency_analysis(cipher_text))
