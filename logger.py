#!/usr/bin/env python

import sys 
from datetime import datetime

filename = sys.argv[1]

with open(filename, 'a') as file:
    while True:
        try:
            message = raw_input().strip()  

            if message == "QUIT":
                formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                file.write("{} [QUIT] Logging stopped\n".format(formatted_time))  
                break

            parts = message.split(' ', 1)
            action = parts[0]

            formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M")

            if len(parts) > 1:
                msg_content = parts[1]
                file.write("{} [{}] {}\n".format(formatted_time, action, msg_content))  
            else:
                file.write("{} [{}]\n".format(formatted_time, action))  

        except EOFError:
            break




