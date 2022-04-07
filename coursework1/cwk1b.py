# Vigenere Cipher

def ext_vigenere(text, key, option):  # Sets up main function
    conversion_array = []  # Sets up array to convert numbers to letters
    text_array = []  # Stores the inputted text as numbers
    key_array = []  # Stores the key as numbers
    for i in range(1, 127):
        conversion_array.append(i)
        i += 1
    for j in text:
        k = ord(j)
        text_array.append(k)
    for m in key:
        a = ord(m)
        key_array.append(a)

    if option.lower() == "encrypt":
        s = 0
        d = 0
        f = 0
        cipher_text = []
        text_length = len(text)
        key_length = len(key)
        for s in range(0, text_length):
            deviations = key_array[d] - 32
            new_cipherchar = text_array[f] + deviations
            if new_cipherchar > 126:
                new_cipherchar = (new_cipherchar - 126) + 32
            cipher_text.append(chr(new_cipherchar))
            d += 1
            f += 1
            if d >= key_length:
                d = 0
        for x in range(len(cipher_text)):
            returned_text = "".join(cipher_text)
        return returned_text

    elif option.lower() == "decrypt":
        s = 0
        d = 0
        f = 0
        plain_text = []
        text_length = len(text)
        key_length = len(key)
        for s in range(0, text_length):
            deviations = key_array[d] - 32
            new_plainchar = text_array[f] - deviations
            if new_plainchar < 32:
                new_plainchar = (127-(deviations-(text_array[f]-32)))
            plain_text.append(chr(new_plainchar))
            d += 1
            f += 1
            if d >= key_length:
                d = 0
        for x in range(len(plain_text)):
            returned_text = "".join(plain_text)
        return returned_text

    elif option.lower() != "encrypt":
        return "Invalid option!"

    elif option.lower() != "decrypt":
        return "Invalid option!"


# print(ext_vigenere("<UcY6dK`", "testing", "endecrypt"))
