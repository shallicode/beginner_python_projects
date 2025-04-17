import string

def encryption(cipher_text, word, shift_num):
    end_text = ""
    lowerCase = list(string.ascii_lowercase)
    upperCase = list(string.ascii_uppercase)
    if cipher_text == "decode":
        shift_num *= -1
    for char in word:
        if char in lowerCase:
            position = (lowerCase.index(char) + shift_num)%26
            end_text += lowerCase[position]
        elif char in upperCase:
            position = (upperCase.index(char) + shift_num)%26
            end_text += upperCase[position]
        else:
            end_text += char
    print(f"The cipher is {end_text}\n")
    encryptWord = input("Do you want to continue? Yes/No\n").lower()
    if encryptWord == "yes":
        return True
    else:
        return False

encrypt = True
while encrypt:
    cipher_text = input("What do you want to do?\n")
    word = input("Enter the cipher:\n")
    shift_num = int(input("Enter the shift number:\n"))
    shift_num %= 26
    encrypt = encryption(cipher_text,word,shift_num)