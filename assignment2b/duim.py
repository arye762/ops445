#!/usr/bin/env python3

import subprocess, sys
import os
import argparse

'''
OPS445 Assignment 2 - Summer 2024
Program: duim.py 

Author: Arie Cimafranca
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description:
This script improves the 'du' command by presenting directory disk usage with visual bar graphs,
showing usage percentages for easier interpretation. It supports human-readable output and
targets specified directories for quick disk usage assessment.

Date: July 28, 2024
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2022")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    command = ['du', '-d', '1', target_directory]

    # Execute the command using subprocess.Popen
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = process.communicate()

        if process.returncode != 0:
            print("Error:", errors)
            return []

        # Split the output into lines and return the list
        return output.strip().split('\n')

    except Exception as e:
        print(f"Failed to run command: {e}")
        return []

def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    if not 0 <= percent <= 100:
        raise ValueError("Percent must be between 0 and 100")

    # Calculate the number of symbols to represent the filled part of the graph
    filled_length = round((percent / 100) * total_chars)

    # Calculate the number of spaces for the unfilled part of the graph
    empty_length = total_chars - filled_length

    # Create the bar graph string
    bar_graph = '=' * filled_length + ' ' * empty_length

    return bar_graph

def call_du_sub(target_directory):
    """ Calls 'du' command on target directory with a depth of 1 and parses the output. """
    command = ['du', '-d', '1', target_directory]

    # Execute the command using subprocess.Popen
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, errors = process.communicate()

        if process.returncode != 0:
            print("Error:", errors)
            return []

        # Split the output into lines and return the list
        return output.strip().split('\n')

    except Exception as e:
        print(f"Failed to run command: {e}")
        return []

def create_dir_dict(alist):
    "gets a list from call_du_sub, returns a dictionary which should have full"
    "directory name as key, and the number of bytes in the directory as the value."
    pass


if __name__ == "__main__":
    pass