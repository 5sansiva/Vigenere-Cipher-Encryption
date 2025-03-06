#!/usr/bin/env python

import sys
from datetime import datetime

filename = sys.argv[1]
mode = sys.stdin.readline().rstrip()  
memloc = 0

with open(filename, 'a') as file:
    
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M")
    file.write(f"{formatted_time} [START] Logging Started\n")
    file.flush()

    while mode != "halt":
        
        formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        if mode == "read":
            
            file.write(f"{formatted_time} [READ] {memloc}\n")
            sys.stdout.flush()
        elif mode == "write":
            
            memloc = int(sys.stdin.readline().rstrip())
            file.write(f"{formatted_time} [WRITE] {memloc}\n")
        
        
        mode = sys.stdin.readline().rstrip()

    
    formatted_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    file.write(f"{formatted_time} [QUIT] Logging stopped\n")
    file.flush()



