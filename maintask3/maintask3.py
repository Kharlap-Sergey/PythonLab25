#lab 2_5 files main task 3
#this program was designed to delete coments within a code file
#
#version 0.0.1
#kharlap-Sergey 10701219
#5/18/2020

def main():
    fin = open("code.in", "r+")
    fout = open("code.out", "w+")
    for i in fin.readlines():
        pos = i.find("#");
        #print(i)
        if(pos != -1):
            ans = i[:pos]
        else:
            ans = i[:]
        fout.write(ans)
    fout.close()
    fin.close()

main()
