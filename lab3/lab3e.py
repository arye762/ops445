#!/usr/bin/env python3
'''Lab 3 Inv 3 Part 1 Navigate Items in Lists '''
# Author ID: acimafranca


# Global list
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Returns all of items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Returns a list that includes the first and last items in the global object my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Returns a list that includes the second and third items in the global object my_list
    return my_list[1:3]

if __name__ == '__main__':   # Main block
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
