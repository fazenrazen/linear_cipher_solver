import math 
import array

# stores the converted encryption 
encrypt_msg = []
# decryption info 
A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
B = range(0, 26)

decrypt_msg = []

def user_text():
    # take the users input
    user_text = input('Enter text: ').lower().replace(" ", "")
    
    # converting the text user gives to ascii
    text_to_numbers = []
    
    # converting string to characters
    convert_to_char = [char for char in user_text]
    
    # converting characters to numbers
    for letters in convert_to_char:
        encode_letter = ord(letters) - 97
        text_to_numbers.append(encode_letter)
    
    return text_to_numbers
    
def encrypt():
    word = user_text()
    a_key = input("What is the A key? ")
    b_key = input("What is the B key? ")
    
    a_key = int(a_key)
    b_key = int(b_key)
    
    for letters in word:
        encrypt_letter = a_key * letters + b_key
        encrypt_letter = (encrypt_letter % 26) + 97
        encrypt_msg.append(chr(encrypt_letter))

    print(''.join(encrypt_msg))
    
def decrypt():
    word = user_text()
    
    for a in A:
        for b in B:
            decrypted_word = ""
            for letter in word:
                decrypted_letter = pow(a, -1, 26) * (letter - b) % 26
                decrypted_letter = decrypted_letter + 97
                decrypted_word += chr(decrypted_letter)
            decrypt_msg.append(decrypted_word + '\n')
    
    print(''.join(decrypt_msg))
    print("Number of ways:", len(decrypt_msg))
        
def main():
    for i in range(2):
        user_choice = input('1. Encrypt?\n2. Decrypt?\n')
        
        if user_choice == '1':
            encrypt()    
        elif user_choice == '2':
            decrypt()

        print('\n')


main()

