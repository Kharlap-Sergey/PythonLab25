#lab 2_5 files extra task 1
#this program was designed to figure out that the string is the hex number
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

from fileworks import *

def is_hex_number(string):
    if len(string) < 3:
        return False
    numbers = '0123456789abcdef'
    if string[:2].lower() != 'ox':
        return False
    
    for i in string[2:]:
        if not i.lower() in numbers:
            return False

    return True

def main():
    string = read_frome_file("data.in")
    string = string.rstrip()
    ans = "";
    if is_hex_number(string):
        ans = "the {0} is hex number".format(string)
    else:
        ans = "the {0} isn't hex number".format(string)

    print(ans)
main()

