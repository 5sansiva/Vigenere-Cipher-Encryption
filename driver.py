#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

history = {} #Stores messages
count = 0

def log(logger_process, message):
    loggerProcess.stdin.write(message + "\n")
    loggerProcess.stdin.flush()

def search_history():
    while True:
        print("\nHistory Menu:")
        for count, val in history.items():
            print(f"{count}. {val}")
        print("Choose 0 to go back to menu")
        print("Type 'add' to input a new string to history")

        choice = input("Choose a number, type 'add', or 0 to go back: ").strip().lower()
        if choice == 0:
            print("Returning to menu")
            return None
        
        if choice == "add":
            newString = input("Enter a new string: ")
            history[count + 1] = newString
            count += 1
            print(f"New string '{newString}' added to history.")\
            return newString

        try:
            choice = int(choice)
            if choice in history:
                return history[choice]
            else:
                print("Invalid choice. Please select a valid option")
        except ValueError:
            print("Invalid input. Please enter a valid number or command.")


def main():
    if len(sys.argv) != 2:
        print("Please upload the log file")
        sys.exit(1)

    log_file = sys.argv[1]

    loggerProcess = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encryptionProcess = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    log(loggerProcess, "START Logging Started")

    while True:
        print("\nMenu:")
        print("1. Password")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. History")
        print("5. Quit")

        choice = input("Enter command choice: ").strip().lower()

        if choice == "password":
            message = input("Use a string in history(1) or new string(2): ").strip()

            
            if message == "2":
                password = input("Enter a password: ")
                if password.isalpha():
                    count += 1
                    history[count] = password
                    #Set the password as the passkey in the encryption file
                    encryptionProcess.stdin.write(f"PASS {password}\n")
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    log(loggerProcess, "PASSWORD SET")
                    log(loggerProcess, result)
                else:
                    print("Invalid input. Please enter a valid string(letters only).")
                
            elif message == "1":
                if history:
                    password = search_history()
                    if password:
                        encryptionProcess.stdin.write(f"PASS {password}\n")
                        encryptionProcess.stdin.flush()
                        result = encryptionProcess.stdout.readline().strip()
                        log(loggerProcess, "PASSWORD SET")
                        log(loggerProcess, result)
                    else:
                        print("Invalid history selection.")


        elif choice == "encrypt":
            message = input("Choose a string in new string(1) or history(2): ").strip()

            if message == "1":
                newString = input("Enter your new string: ")

                if newString.isalpha():
                    encryptionProcess.stdin.write(f"ENCRYPT {message}\n")
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, f"ECRYPT {message}")
                    log(loggerProcess, result)
                    if result.startswith("RESULT"):
                        count += 1
                        history[count] = message
                else:
                    print("Invalid input. Please enter a valid string(letters only).")

            elif message == "2":
                val = search_history()
                encryptionProcess.stdin.write(f"ENCRYPT {message}\n")
                encryptionProcess.stdin.flush()
                result = encryptionProcess.stdout.readline().strip()
                print(result)
                log(loggerProcess, f"ECRYPT {message}")
                log(loggerProcess, result)
                
        
        
        
        elif choice == "decrypt":
            message = input("Choose a string in new string(1) or history(2): ").strip()

            if message == "1":
                newString = input("Enter your new string: ")
                if newString.isalpha():
                    encryptionProcess.stdin.write(f"DECRYPT {message}\n")
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, f"DECRYPT {message}")
                    log(loggerProcess, result)
                    if result.startswith("RESULT"):
                        history[count + 1] = message
                else:
                    print("Invalid input. Please enter a valid string(letters only).")
            elif message == "2":
                val = search_history()
                encryptionProcess.stdin.write(f"DECRYPT {message}\n")
                encryptionProcess.stdin.flush()
                result = encryptionProcess.stdout.readline().strip()
                print(result)
                log(loggerProcess, f"DECRYPT {message}")
                log(loggerProcess, result)

        elif choice == "history":
            print("\nHistory")

            if not history:
                print("No history available")
            else:
                for count, val in history.items():
                    print(f"{count}. {val}")
            
        elif choice == "quit":
            log(loggerProcess, "QUIT")
            encryptionProcess.stdin.write("QUIT\n")
            encryptionProcess.stdin.flush()
            loggerProcess.stdin.close()
            encryptionProcess.stdin.close()
            loggerProcess.wait()
            encryptionProcess.wait()
            print("Program has ended. Good bye :)")
            break

if __name__ == "__main__":
    main()

    