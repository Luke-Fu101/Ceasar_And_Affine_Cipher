#Build the math logic for 2 ciphers Ceasar Cipher: 
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65) if char.isupper() else chr(((ord(char) - 97 + shift_amount) % 26) + 97)
            result += new_char
        else:
            result += char
    return result

def affine_cipher(text, shift, multiplier):
    result = ""
    if multiplier % 2 != 0 and multiplier % 13 != 0:
        for char in text:
            if char.isalpha():  # Ensure multiplier is coprime to 26
                shift_amount = shift % 26
                new_char = chr(((ord(char) - 65) * multiplier + shift_amount) % 26 + 65) if char.isupper() else chr(((ord(char) - 97) * multiplier + shift_amount) % 26 + 97)
                result += new_char
            else:
                result += char
    return result

        