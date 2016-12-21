import os, re

def mystem_csv():
    inp = 'input.txt'
    outp = 'output.csv'
    os.system(r'C:\mystem.exe -ncd ' + inp + ' ' + outp)


def processing():
    f = open('output.csv', 'r', encoding = 'utf-8')
    text = f.readlines()
    f.close()
    return text


def data_base_lem(text):
    fw = open('sql_script.sql', 'w', encoding = 'utf-8')
    fw.write('CREATE TABLE text_lem (id INTEGER PRIMARY KEY, wordform VARCHAR (100), lemma VARCHAR (100));' + '\n')
    i = 0
    punctuation = []
    d_lem = {}
    for line in text:
        parsing = re.split('[,{}]', line)
        if len(parsing) > 2:
            if parsing[1] not in d_lem:
                table_line = 'INSERT INTO text_lem (id, wordform, lemma) values ("' + str(i) + '", "' + parsing[0].lower() + '", "' + parsing[1] + '");'
                fw.write(table_line + '\n')
                d_lem[parsing[1]] = i
                i += 1
        else:
            line = line.strip('_\n\\n')
            punctuation.append(line)
    fw.close()
    return d_lem, punctuation


def data_base(text, d_lem, punctuation):
    fw = open('sql_script.sql', 'a', encoding = 'utf-8')
    fw.write('\n' + 'CREATE TABLE text (id INTEGER PRIMARY KEY, wordform VARCHAR (100), punctuation_left VARCHAR (100), punctuation_right VARCHAR (100), text_number INTEGER, id_lemma INTEGER);' + '\n')
    i = 0
    for line in text:
        parsing = re.split('[,{}]', line)
        if len(parsing) > 2:
            for k in d_lem:
                if k == parsing[1]:
                    id = d_lem[parsing[1]]
                    break
            if i == 0:
                table_line = 'INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("' + str(i) + '", "' + parsing[0] + '", "' + ' ' + '", "' + punctuation[i] + '", "' + str(i+1) + '", "' + str(id) + '");'
            else:
                table_line = 'INSERT INTO text (id, wordform, punctuation_left, punctuation_right, text_number, id_lemma) values ("' + str(i) + '", "' + parsing[0] + '", "' + punctuation[i-1] + '", "' + punctuation[i] + '", "' + str(i+1) + '", "' + str(id) + '");'
            fw.write(table_line + '\n')
            i += 1
    fw.close()


def main():
    mystem_csv()
    d_lem, punctuation = data_base_lem(processing())
    data_base(processing(), d_lem, punctuation)

if __name__ == '__main__':
    main()