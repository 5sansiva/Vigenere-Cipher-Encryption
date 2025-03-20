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

def decrypt(cipherText, passkey):
    decrypt_text = ""
    for i in range(len(cipherText)):
        shift = ord(passkey[i % len(passkey)]) - ord('A')
        new_char = chr(((ord(cipherText[i]) - ord('A') - shift) % 26) + ord('A'))
        decrypt_text += new_char

    return decrypt_text

if __name__ == "__main__":  
    while True:
        command_line = raw_input()  
        command_parts = command_line.split(' ', 1)

        
        if len(command_parts) == 0:
            continue  
        command = command_parts[0].upper()
        
        if(command == "PASS"):
            if len(command_parts) > 1:
                passkey = command_parts[1].upper()
                sys.stdout.write("RESULT\n")
                sys.stdout.flush()
            else:
                sys.stdout.write("ERROR Password not set\n")
                sys.stdout.flush()
        
        elif(command == "ENCRYPT"):
            if passkey:
                if len(command_parts) > 1:
                    plainText = command_parts[1]
                    if not plainText.isalpha():
                        sys.stdout.write("ERROR Only alphabetic characters allowed\n")
                        sys.stdout.flush()
                        continue
                    encrypted_text = encrypt(plainText, passkey)
                    sys.stdout.write("RESULT {}\n".format(encrypted_text))
                    sys.stdout.flush()
            else:
                sys.stdout.write("ERROR Password not set\n")
                sys.stdout.flush()
        
        elif(command == "DECRYPT"):
            if passkey:
                if len(command_parts) > 1:
                    cipherText = command_parts[1]
                    if not cipherText.isalpha():
                        sys.stdout.write("ERROR Only alphabetic characters allowed\n")
                        sys.stdout.flush()
                        continue
                    decrypted_text = decrypt(cipherText, passkey)
                    sys.stdout.write("RESULT {}\n".format(decrypted_text))
                    sys.stdout.flush()
            else:
                sys.stdout.write("ERROR Password not set\n")
                sys.stdout.flush()
        
        elif command == "QUIT":
            sys.stdout.write("Program has exited\n")
            sys.stdout.flush()
            break
        else:
            sys.stdout.write("Unknown command. Try again\n")
            sys.stdout.flush()

