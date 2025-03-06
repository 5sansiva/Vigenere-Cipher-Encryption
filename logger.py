#!/usr/bin/env python

import sys 
from datetime import datetime

filename = sys.argv[1]

with open(filename, 'a') as file:
    now = datetime..now()
    formatted_time = now.shrftime("%Y-%m-%d %H:%M")
    file.write(formatted_time + "START Logging Started")
    file.flush()

    while True:
        message = input("Enter log message or enter QUIT to exit: ")
        formatted_time = datetime.now().shrftime("%Y-%m-%d %H:%M")

        if(message == "QUIT"):
            file.write(f"{formatted_time} QUIT {Logging stopped}")
            break
        
        file.write(f"{formatted_time} LOG {message}\n")
        file.flush()



