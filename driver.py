#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

history = {}  # Stores messages
count = 0

def log(loggerProcess, message):
    loggerProcess.stdin.write(message + "\n")
    loggerProcess.stdin.flush()  

def search_history():
    global count
    while True:
        print("\nHistory Menu:")
        for index, val in history.items():
            print("{}. {}".format(index, val))
        print("\n")
        print("Type 'back' to go back to menu")
        print("Type 'add' to input a new string to history")

        choice = raw_input("Choose a number, type 'add' or 'back': ").strip().lower()  
        
        if choice == "back":
            print("Returning to menu")
            return None
        
        if choice == "add":
            newString = raw_input("Enter a new string: ")
            count += 1
            history[count] = newString
            print("New string '{}' added to history.".format(newString))
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
    global count
    if len(sys.argv) != 2:
        print("Please upload the log file")
        sys.exit(1)

    log_file = sys.argv[1]

    loggerProcess = Popen(["python", "logger.py", log_file], stdin=PIPE, universal_newlines=True)
    encryptionProcess = Popen(["python", "encryption.py"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

    if loggerProcess.poll() is not None or encryptionProcess.poll() is not None:
        print("Failed to start subprocesses. Check your files.")
        sys.exit(1)
    
    log(loggerProcess, "START Logging Started")

    while True:
        print("\nMenu:")
        print("1. Password")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. History")
        print("5. Quit")

        choice = raw_input("Enter command choice(Type out command): ").strip().lower()  

        if choice == "password":
            message = raw_input("Enter a new string(1) or choose from history(2): ").strip()  

            if message == "1":
                password = raw_input("Enter a password: ")
                if password.isalpha():
                    count += 1
                    history[count] = password
                    # Set the password as the passkey in the encryption file
                    encryptionProcess.stdin.write("PASS {}\n".format(password))
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "PASSWORD SET")
                    log(loggerProcess, result)
                else:
                    print("Invalid input. Please enter a valid string(letters only).")
                
            elif message == "2":
                if len(history) != 0:
                    password = search_history()
                    if password:
                        encryptionProcess.stdin.write("PASS {}\n".format(password))
                        encryptionProcess.stdin.flush()
                        result = encryptionProcess.stdout.readline().strip()
                        print(result)
                        log(loggerProcess, "PASSWORD SET")
                        log(loggerProcess, result)
                    else:
                        print("Invalid history selection.")
                else:
                    print("History is empty. Please enter a new password")

        elif choice == "encrypt":
            message = raw_input("Enter a new string(1) or choose from history(2): ").strip()  

            if message == "1":
                newString = raw_input("Enter your new string: ")

                if newString.isalpha():
                    encryptionProcess.stdin.write("ENCRYPT {}\n".format(newString.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "ENCRYPT {}".format(newString))  
                    log(loggerProcess, result)
                    if result.startswith("RESULT"):
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid input. Please enter a valid string(letters only).")

            elif message == "2":
                val = search_history()
                encryptionProcess.stdin.write("ENCRYPT {}\n".format(val.upper()))  
                encryptionProcess.stdin.flush()
                result = encryptionProcess.stdout.readline().strip()
                print(result)
                log(loggerProcess, "ENCRYPT {}".format(val))  
                log(loggerProcess, result)
                if result.startswith("RESULT"):
                    result = result.split(" ", 1)[1]
                    count += 1
                    history[count] = result

        elif choice == "decrypt":
            message = raw_input("Enter a new string(1) or choose from history(2): ").strip()  

            if message == "1":
                newString = raw_input("Enter your new string: ")
                if newString.isalpha():
                    encryptionProcess.stdin.write("DECRYPT {}\n".format(newString.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "DECRYPT {}".format(newString))  
                    log(loggerProcess, result)
                    if result.startswith("RESULT"):
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid input. Please enter a valid string(letters only).")
            elif message == "2":
                val = search_history()
                encryptionProcess.stdin.write("DECRYPT {}\n".format(val.upper()))  
                encryptionProcess.stdin.flush()
                result = encryptionProcess.stdout.readline().strip()
                print(result)
                log(loggerProcess, "DECRYPT {}".format(val))  
                log(loggerProcess, result)
                if result.startswith("RESULT"):
                    result = result.split(" ", 1)[1]
                    count += 1
                    history[count] = result

        elif choice == "history":
            print("\nHistory")

            if not history:
                print("No history available")
            else:
                for index, val in history.items():
                    print("{}. {}".format(index, val))
            
        elif choice == "quit":
            try:
                log(loggerProcess, "QUIT")
                encryptionProcess.stdin.write("QUIT\n")
                encryptionProcess.stdin.flush()
            finally:
                loggerProcess.stdin.close()
                encryptionProcess.stdin.close()
                loggerProcess.wait()
                encryptionProcess.wait()

            print("Program has ended. Good bye :)")
            break


if __name__ == "__main__":
    main()


    