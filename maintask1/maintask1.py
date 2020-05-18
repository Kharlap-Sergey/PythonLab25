#lab 2_5 files main task 1
#this program was designed to calculate same words amount
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

def read_frome_file(filename):
    try:
        fin = open(filename, "r")
        text = fin.read()
        fin.close()

        return text
    except:
        return -1


def print_to_file(filename, string):
    try:
        fout = open(filename, "w+")
        fout.write(string);
        fout.close()

        return 1;
    except:
        return -1;


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

def sort_words(words_dict):
    ans = list()
    for i in words_dict.keys():
        ans.append([i, words_dict[i]]);

    ans.sort(key = lambda pattern: pattern[1])

    return ans

def get_string_ansver_representetion(list_words):
    ans = "";
    for wordinf in list_words:
    
        ans += str(wordinf[0]) +'\t' + str(wordinf[1])
        ans += '\n'

    return ans


def main():
    text = read_frome_file("in.txt")
    if text == -1 :
        print("file doesn't exist!")  
    
    separated_text = separate_text(text)
    list_ans = sort_words(separated_text)
    str_ans = get_string_ansver_representetion(list_ans)

    print(print_to_file("out.txt", str_ans))

main()
