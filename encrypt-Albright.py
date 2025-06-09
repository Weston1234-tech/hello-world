alphabet = " abcdefghijklmnopqrstuvwxyz"
get_letter, keyword = 0, []

text = str(input("Enter the text: ")).strip().lower()
key = int(input("Enter the key: "))

if 0 < key <= 26:
    for letter in text:
        if letter in alphabet:
            get_letter = (alphabet.index(letter) + key) % 26
            keyword.append(alphabet[get_letter])
        else:
            keyword.append(letter)
    print("".join(keyword))
else:
        print("Key must be between 1 and 26")
