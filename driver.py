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
        
        if len(history) == 0:
            print("History is empty. Please enter a new string.")
            break

        for index, val in history.items():
            print("{}. {}".format(index, val))
        print("\n")
        print("Type 'back' to go back to menu")
        

        choice = raw_input("Choose a number or type 'back': ").strip().lower()  
        
        if choice == "back":
            print("Returning to menu")
            break

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

    try:
        loggerProcess = Popen(["python", "logger.py", log_file], stdin=PIPE, universal_newlines=True)
        encryptionProcess = Popen(["python", "encryption.py"], stdin=PIPE, stdout=PIPE, universal_newlines=True)
    except OSError as e:
        print("Failed to start subprocesses: {}".format(e))
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
            message = raw_input("Enter (1) to input a new string or (2) to choose from history: ").strip()  

            if message == "1":
                password = raw_input("Enter a password: ")
                if password.isalpha():
                    count += 1
                    history[count] = password.upper()
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
                

        elif choice == "encrypt":
            message = raw_input("Enter (1) to input a new string or (2) to choose from history: ").strip()  

            if message == "1":
                newString = raw_input("Enter your new string: ")
                if newString.isalpha():
                    count += 1
                    history[count] = newString.upper()

                    encryptionProcess.stdin.write("ENCRYPT {}\n".format(newString.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "ENCRYPT {}".format(newString.upper()))  
                    log(loggerProcess, result)
                    if result.startswith("RESULT") and len(result.split(" ", 1)) > 1:
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid input. Please enter a valid string(letters only).")

            elif message == "2":   
                val = search_history()
                if val is not None:
                    encryptionProcess.stdin.write("ENCRYPT {}\n".format(val.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "ENCRYPT {}".format(val))  
                    log(loggerProcess, result)
                    
                    if result.startswith("RESULT") and len(result.split(" ", 1)) > 1:
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid selection or history empty. Returning to menu.")
                


        elif choice == "decrypt":
            message = raw_input("Enter (1) to input a new string or (2) to choose from history: ").strip()  

            if message == "1":
                newString = raw_input("Enter your new string: ")
                if newString.isalpha():
                    count += 1
                    history[count] = newString.upper()

                    encryptionProcess.stdin.write("DECRYPT {}\n".format(newString.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "DECRYPT {}".format(newString))  
                    log(loggerProcess, result)
                    if result.startswith("RESULT") and len(result.split(" ", 1)) > 1:
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid input. Please enter a valid string(letters only).")
            elif message == "2":
                val = search_history()
                if val is not None:
                    encryptionProcess.stdin.write("DECRYPT {}\n".format(val.upper()))  
                    encryptionProcess.stdin.flush()
                    result = encryptionProcess.stdout.readline().strip()
                    print(result)
                    log(loggerProcess, "DECRYPT {}".format(val))  
                    log(loggerProcess, result)
                    if result.startswith("RESULT") and len(result.split(" ", 1)) > 1:
                        result = result.split(" ", 1)[1]
                        count += 1
                        history[count] = result
                else:
                    print("Invalid selection or history empty. Returning to menu.")
                

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
            except IOError:
                print("One of the processes has already stopped.")
            finally:
                if loggerProcess.poll() is None:
                    loggerProcess.stdin.close()
                    loggerProcess.wait()
                if encryptionProcess.poll() is None:
                    encryptionProcess.stdin.close()
                    encryptionProcess.wait()


            print("Program has ended. Good bye :)")
            break


if __name__ == "__main__":
    main()


    