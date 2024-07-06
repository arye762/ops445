#!/usr/bin/env python3
'''Lab 3 Inv 2 Part2 - function operate in os and subprocess modules '''
# Author ID: acimafranca

import subprocess

def free_space():
    # Launch the command to get free disk space
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output, _ = p.communicate()
    # Convert the output to string and strip newline characters
    stdout = output.decode('utf-8').strip()
    return stdout

if __name__ == "__main__":
    print(free_space())

