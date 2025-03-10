import string

def playfair_matrix(keyword):
    matrix = []
    seen = set()
    keyword = keyword.lower().replace('j', 'i')
    for char in keyword + string.ascii_lowercase:
        if char not in seen and char in string.ascii_lowercase and char != 'j':
            matrix.append(char)
            seen.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_encrypt_decrypt(text, matrix, mode='encrypt'):
    def find_position(letter):
        for i, row in enumerate(matrix):
            if letter in row:
                return i, row.index(letter)
    text = text.lower().replace('j', 'i')
    text_pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    new_text = ''
    for pair in text_pairs:
        row1, col1 = find_position(pair[0])
        row2, col2 = find_position(pair[1])
        if row1 == row2:
            col1 = (col1 + (1 if mode == 'encrypt' else -1)) % 5
            col2 = (col2 + (1 if mode == 'encrypt' else -1)) % 5
        elif col1 == col2:
            row1 = (row1 + (1 if mode == 'encrypt' else -1)) % 5
            row2 = (row2 + (1 if mode == 'encrypt' else -1)) % 5
        else:
            col1, col2 = col2, col1
        new_text += matrix[row1][col1] + matrix[row2][col2]
    return new_text

print("\nPlayfair Cipher:")
keyword = "keyword"
playfair_m = playfair_matrix(keyword)
print(playfair_encrypt_decrypt("hello", playfair_m, mode='encrypt'))
