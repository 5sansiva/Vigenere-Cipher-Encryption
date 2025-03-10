#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE

mem = Popen(['python', 'mem.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')

def main():
    if len(sys.argv) != 2:
        print("Please upload the log file")
        sys.exit(1)

    log_file = sys.argv[1]

    loggerProcess = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encryptionProcess = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    history = [] #Stores messages

    def log()
        loggerProcess.stdin.write()
    log("START Logging Started")



while True:
    print("\nMenu:")
    print("1. Password")
    print("2. Encrypt")
    print("3. Decrypt")
    print("4. History")
    print("5. Quit")

    choice = input("Enter command choice: ").strip().lower()

    if choice == "password":
        message = input("Use a string in (1)history or (2) new string: ")

        if message == "2":
            password = input("Enter a password: ")
            
        elif message == "1":
            if history:
                password = search_history(password)


    elif choice == "encrypt":
    elif choice == "decrypt":
    elif choice == "history"
    elif choice == "quit":
        break


for i in range(10,0,-1):
    mem.stdin.write("write\n")
    mem.stdin.write(str(i))
    mem.stdin.write("\n")
    sys.stdout.write("Set to ")
    mem.stdin.write("read\n")
    mem.stdin.flush()
    print(mem.stdout.readline().rstrip())

mem.stdin.write("halt\n")
mem.stdin.flush()

mem.wait()

logger_process.wait()
encryption_process.wait()

if __name__ == "__main__":
    main()

    