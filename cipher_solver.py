import math 
import array

"""
FEATURE REQUESTS 
Need to fix


Nice to haves
1. Cipher a page with different ciphers
2. Encrypt with multiple layers of linear cipher
3. Auto key Encrypter 
4. V cipher with keyword solver
5. RSA implementation
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

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1
   
def encrypt():
    print('\nEncrypting!\n')
    
    # stores the converted encryption 
    encrypt_msg = []
    
    word = user_text()
    print("\nCoefficient of A should be prime w/ 26 (1, 3, 7...)")
    print("Coefficient of B can be any positive integer\n")
    
    a_key = int(input("What is the A key? "))
    b_key = int(input("What is the B key? "))
    
    a_coprime = bool() 

    # Checks if the A key is Coprime with 26
    while a_coprime != True:
        a_coprime = is_coprime(a_key, 26)
        
        if(a_coprime == False):
            a_key = print('\nA_key is NOT coprime with 26\n')
            a_key = int(input('Reenter A_key: '))
    
    # Encryption Algorithm
    for letters in word:
        encrypt_letter = a_key * letters + b_key
        encrypt_letter = (encrypt_letter % 26) + 97
        encrypt_msg.append(chr(encrypt_letter))

    # Printing the Encrypted message
    print("Your encrypted message is " + ''.join(encrypt_msg))
    
def decrypt():
    word = user_text()
    
    # this is a slow implementation, fix this 
    for a in A:
        for b in B:
            decrypted_word = ""
            for letter in word:
                decrypted_letter = pow(a, -1, 26) * (letter - b) % 26
                decrypted_letter = decrypted_letter + 97
                decrypted_word += chr(decrypted_letter)
            decrypt_msg.append(decrypted_word + ' a key: ' + str(a) + ' b key: ' + str(b) + '\n')
    
    # Printing the decrypted words
    print("Your decrypted words are: ")
    print(''.join(decrypt_msg))
    print("Number of ways:", len(decrypt_msg))
  
def main():
    
    # Initial user choice
    user_input = ''
    
    # loop choices until exit
    while user_input != '3':
        print('1. Encrypt?')
        print('2. Decrypt?')
        print('3. Exit\n')
            
        # Take User_input
        user_input = input('Enter 1, 2, or 3: ')
        
        if user_input == '1':
            encrypt()    
        elif user_input == '2':
            decrypt()
        print('\n')
    
main()