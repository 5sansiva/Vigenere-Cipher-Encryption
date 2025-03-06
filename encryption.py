#!/usr/bin/env python
import sys

passkey = None

def encrypt(plaintext, passkey):
    encrypt_text = ""
    for i in range(len(plaintext)):
        shift = ord(passkey[i % len(passkey)]) - ord('A')
        new_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
        encrypt_text += new_char
    return encrypt_text

def decrypt(plaintext, passkey):
    decrypt_text = ""
    for i in range(len(plaintext)):
        shift = ord(passkey[i % len(passkey)]) - ord('A')
        new_char = chr(((ord(plaintext[i]) - ord('A') - shift) % 26) + ord('A'))
        decrypt_text += new_char

    return decrypt_text

if __name__ == "__main__":  
    while True:
        command_line = input("Input: ") 
        command_parts = command_line.split(maxsplit=1)
        
        if len(command_parts) == 0:
            continue  
        command = command_parts[0].upper()
        
        if(command == "PASS"):
            if len(command_parts) > 1:
                passkey = command_parts[1].upper()
                print("RESULT")
            else:
                print("ERROR Password not set")
        
        elif(command == "ENCRYPT"):
            if passkey:
                if len(command_parts) > 1:
                    plainText = command_parts[1]
                    encrypted_text = encrypt(plainText, passkey)
                    print(f"RESULT {encrypted_text}")
            else:
                print("ERROR Password not set")
        
        elif(command == "DECRYPT"):
            if passkey:
                if len(command_parts) > 1:
                    cipherText = command_parts[1]
                    decrypted_text = decrypt(plaintext, passkey)
                    print(f"RESULT {decrypted_text}")
            else:
                print("ERROR Password not set")
        
        elif command == "QUIT":
            print("Program has exited")
            break
        else:
            print("Unknown command. Try again")

