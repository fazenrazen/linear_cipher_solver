import math 
import array

"""
FEATURE REQUESTS 
Need to fix
1. Fix the Coprimes list from A
2. Error checking User input of A key 
3. Use a dif file for adding the encryption details
4. Print the A and B Keys

Nice to haves
1. Cipher a page with different ciphers
2. Encrypt with multiple layers of linear cipher
3. Auto key Encrypter 
4. V cipher with keyword solver
5. RSA implementation
6. 
"""

# Need to Fix
# fix the coprimes of A list into a loop
# Error check to user if the number is coprime for A
# add the ciphers in a different file 
# cipher a page

# Nice to haves
# encrypt with multiple layers of linear cipher
# Auto key Encrypter 
# V cipher with keyword solver

# stores the converted encryption 
encrypt_msg = []
# decryption info 
A = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
B = range(0, 26)

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
    print("\nCoefficient of A should be prime w/ 26 (1, 3, 7...)")
    print("Coefficient of B can be any positive integer\n")
    a_key = input("What is the A key? ")
    b_key = input("What is the B key? ")
    
    a_key = int(a_key)
    b_key = int(b_key)
    
    for letters in word:
        encrypt_letter = a_key * letters + b_key
        encrypt_letter = (encrypt_letter % 26) + 97
        encrypt_msg.append(chr(encrypt_letter))

    # Printing the Encrypted message
    print("Your encrypted message is " + ''.join(encrypt_msg))
    
def decrypt():
    word = user_text()
    
    decrypt_msg = []
    
    # this is a slow implementation, fix this 
    for a in A:
        for b in B:
            decrypted_word = ""
            for letter in word:
                decrypted_letter = pow(a, -1, 26) * (letter - b) % 26
                decrypted_letter = decrypted_letter + 97
                decrypted_word += chr(decrypted_letter)
            decrypt_msg.append(decrypted_word + '\n')
    
    
    # Finding the text
    find_text(decrypt_msg)
    
    # Printing the decrypted words
    # print("Your decrypted words are: ")
    # print(''.join(decrypt_msg))
    # print("Number of ways:", len(decrypt_msg))

def find_text(decrypt_msg):
    print("Your decrypted words are: ")
    print(''.join(decrypt_msg))
    print("Number of ways:", len(decrypt_msg))

        
        
def main():
    for i in range(2):
        user_choice = input('1. Encrypt?\n2. Decrypt?\nEnter 1 or 2: ')

        if user_choice == '1':
            encrypt()    
        elif user_choice == '2':
            decrypt()

        print('\n')

main()


