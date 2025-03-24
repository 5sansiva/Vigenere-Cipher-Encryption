# Vigenere-Cipher-Encryption

 # CS4348 Project 1 - Logger, Encryption, and Driver Programs

## Overview
This project implements a system consisting of three interconnected programs using **Python**:
1. **Logger** - Records activity logs.
2. **Encryption Program** - Encrypts and decrypts messages using the Vigenère cipher.
3. **Driver Program** - Coordinates user interaction, launches other programs, and manages communication through pipes.

The programs communicate via pipes using the `subprocess` module in Python.

---

## Setup
Install required packages with:
```
pip install -r requirements.txt
```

---

## Program Breakdown

### 1. Logger
- Takes a log file name as a command-line argument.
- Logs messages with timestamps.
- Continues to log messages from standard input until receiving "QUIT".

### 2. Encryption Program
- Supports commands:
  - `PASS <key>`: Sets the encryption passkey.
  - `ENCRYPT <string>`: Encrypts using the Vigenère cipher.
  - `DECRYPT <string>`: Decrypts the string.
  - `QUIT`: Exits the program.
- Returns results or error messages.

### 3. Driver Program
- Launches logger and encryption programs as separate processes.
- Manages user interaction via a command menu:
  - `password`: Set a passkey.
  - `encrypt`: Encrypt a string.
  - `decrypt`: Decrypt a string.
  - `history`: Show string history.
  - `quit`: Exits the system.
- Logs all actions and results.

---

## Example Interactions

**Encryption Program:**
```
Input: ENCRYPT HELLO
Output: ERROR Password not set

Input: PASS HELLO
Output: RESULT

Input: ENCRYPT HELLO
Output: RESULT OIWWC
```

**Driver Program:**
```

Menu:
1. Password
2. Encrypt
3. Decrypt
4. History
5. Quit
Enter command choice(Type out command): password
Enter (1) to input a new string or (2) to choose from history: 2

History Menu:
History is empty. Please enter a new string.

Menu:
1. Password
2. Encrypt
3. Decrypt
4. History
5. Quit
Enter command choice(Type out command): 1
Invalid choice. Please enter a valid choice!

Menu:
1. Password
2. Encrypt
3. Decrypt
4. History
5. Quit
Enter command choice(Type out command): password
Enter (1) to input a new string or (2) to choose from history: 1
Enter a password: hello
RESULT

Menu:
1. Password
2. Encrypt
3. Decrypt
4. History
5. Quit
Enter command choice(Type out command): quit
Program has ended. Good bye :)



```

---

## Error Handling
- Non-letter characters in strings or passkeys result in errors.
- Input is case-insensitive.
- Commands with missing arguments return an error.

---

## Resources
- Vigenère Cipher: [Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

Happy coding!


