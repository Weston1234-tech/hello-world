alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted_text = []

cipher_text = input("Enter the text: ").strip().lower()
key = int(input("Enter the key: "))

if 1 <= key <= 26:
    for letter in cipher_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = (index - key) % 26
            decrypted_text.append(alphabet[shifted_index])
        else:
            decrypted_text.append(letter)

else:
        print("Key must be between 1 and 26")
print("Decrypted text:", "".join(decrypted_text))
