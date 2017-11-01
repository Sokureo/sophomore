import html
import os
import re
import urllib.request # :)


def get_page():
    req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(req) as response:
        html_page = response.read().decode('utf-8')
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
    html_page = regTag.sub(' ', html.unescape(html_page))
    return html_page


def get_words(html_page):
    fw = open('input.txt', 'w', encoding = 'utf-8')
    words = html_page.split()
    c_words = set()
    for word in words:
        if word.startswith('с'):
            c_words.add(word.strip(',.—?!:;»…'))
    print("Слова, начинающиеся на с:")
    for word in c_words:
        print(word)
        fw.write(word + '\n')
    fw.close()
    return c_words


def mystem_csv():
    inp = 'input.txt'
    outp = 'output.csv'
    os.system(r'C:\mystem.exe -incd ' + inp + ' ' + outp)


def verbs():
    print('\n' + 'Глаголы:')
    f = open('output.csv', 'r', encoding = 'utf-8')
    text = f.readlines()
    for line in text:
        parsing = re.split('[,{}]', line)
        if len(parsing) > 2:
            if '=V' in parsing[1]:
                print(parsing[0])
    f.close()
    return text


def data_base(text):
    fw = open('sql_script.sql', 'w', encoding = 'utf-8')
    fw.write('CREATE TABLE text (id INTEGER PRIMARY KEY, wordform VARCHAR (100), lemma VARCHAR (100), PoS VARCHAR (100));' + '\n')
    i = 0
    for line in text:
        parsing = re.split('[,{}]', line)
        if len(parsing) > 2:
            table_line = 'INSERT INTO text (id, wordform, lemma, PoS) values ("' + str(i) + '", "' + parsing[0] + '", "' + parsing[1].split('=')[0].strip('?') + '", "' + parsing[1].split('=')[1] + '");'
            fw.write(table_line + '\n')
            i += 1
    fw.close()


def main():
    get_words(get_page())
    mystem_csv()
    data_base(verbs())


if __name__ == '__main__':
    main()
