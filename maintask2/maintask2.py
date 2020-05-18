#lab 2_5 files main task 2
#this program was designed to decrypt text 
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

from fileworks import *

def decryptORD(word, leap):
    ans = "";
    for i in word:
        if i == '\n':
            i = ' '
        if i != " ":
            ans += chr(ord(i)+leap)
        else:
           ans += i
    return ans 

def decryptPermutation(text):
    ans = ""
    word = ""
    counter = 3
    for i in text:
        if i != ' ':
            word += i
        else:
            first_half = word[-counter%len(word):]
            second_half = word[:-counter%len(word)]
            ans += first_half + second_half + " "
            if '.' in word:
                counter += 1
                ans += '\n'
            word = ""

    return ans;
        


def main():
    text = read_frome_file("important.in")
    
    boof = decryptORD(text, -1)
    ans =decryptPermutation(boof)

    print_to_file("important.out",ans)
main()
