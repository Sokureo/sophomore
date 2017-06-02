import json
import os
import re
from pymorphy2 import MorphAnalyzer


def get_lemma_list():

    m = MorphAnalyzer()
    lemma_list = {} # словарь, где ключи -- характеристики слова, а значения -- масиив со словами
    fnames = os.listdir('.')
    fw = open('lemma_list.json', 'w', encoding='utf-8')

    for f in fnames:
        print('processing ' + f)

        if f.endswith('.txt'):
            text = open(f, 'r', encoding='utf-8').read()
            text = re.split('[^А-ЯЁа-яё-]+', text)
            for word in text:
                ana = m.parse(word)
                char = str(ana[0].tag).split(' ')[0]
                lemma = ana[0].normal_form
                if char not in lemma_list:
                    lemma_list[char] = [lemma]
                elif char in lemma_list and lemma not in lemma_list[char]:
                    lemma_list[char].append(lemma)

    lemma_list.pop('UNKN')
    lemma_list.pop('PNCT')
    json.dump(lemma_list, fw, ensure_ascii=False)
    fw.close()


get_lemma_list()