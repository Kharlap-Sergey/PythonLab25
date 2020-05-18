#lab 2_5 files main task 2
#this program was designed analyse text
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

from fileworks import *

def is_letter(char):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    letters += "ёйцукенгшщзхфывапролджжжжжжэъячсмитьбю"
    
    for i in letters:
        if i == char:
            return True

    return False


def separate_text(text):
    word = ""
    words = {}

    for character in text:
        character = character.lower()
        if is_letter(character):
            word += character
        elif len(word) != 0:
            words.setdefault(word, 0)
            words[word] += 1
            word = ""
    
    if len(word) != 0:
        words.setdefault(word, 0)
        words[word] += 1
    return words


def main():
    text = read_frome_file("in.txt")
    if text == -1 :
        print("file doesn't exist!")  
    
    separated_text = separate_text(text)
    
    print("amount of words:\n", len(separated_text), sep = "")
    print("words are len is even:")
    for i in separated_text.keys():
        if len(i) % 2 == 0:
            print(i, end = ' ')

    print()
    print()
    print("dublicated words are:")
    for i in separated_text.keys():
        if separated_text[i] > 1:
            print(i, end = ' ')

    print()
    print()
    ans  = "nothing was found"
    print("the shortest word which started by 'a' is:")
    for i in separated_text.keys():
        if i[0] == 'a' and len(ans) > len(i):
            ans = i
    print(ans)
main()

