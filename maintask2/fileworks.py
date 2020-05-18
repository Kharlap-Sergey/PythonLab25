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
