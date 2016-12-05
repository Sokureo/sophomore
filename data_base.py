import os, re

def processing():
    f = open('input.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def mystem_csv(text):
    inp = 'C:\input.txt'
    outp = 'C:\output.csv'     
    os.system(r'C:\mystem.exe -ncid ' + inp + ' ' + outp)

def data_base():
    f = open('output.csv', 'r', encoding = 'utf-8')
    for line in f:
        s = re.split('[,{}]', line)
        print(s)

def main():
    mystem_csv(processing())
    data_base()

if __name__ == '__main__':
    main()
