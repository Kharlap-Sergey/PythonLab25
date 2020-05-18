#lab 2_5 files main task 3
#this program was designed to decrypt the test
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

from fileworks import *

def is_brakets(char):
    brackets = "\'\""
    
    for i in brackets:
        if i == char:
            return True

    return False


def extract_brekets(text):
    word = ""
    words = []
    FADD = False
    for character in text:
        character = character.lower()
        if FADD:
            word += character
        if is_brakets(character):
            
            if len(word) > 1:
                FADD = False
                words.append(word)
                word = ""
            else:
                word += character
                FADD = True
    
    return words


def main():
    text = read_frome_file("data.in")
    if text == -1 :
        print("file doesn't exist!")  
    
    ans_list = extract_brekets(text)
    
    ans =""
    for i in ans_list:
        ans += i + "\n"
    print_to_file("data.out", ans)
main()


