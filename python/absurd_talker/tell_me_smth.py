import json
import random
import re
from pymorphy2 import MorphAnalyzer


def get_punct(word):

    rus = '[А-ЯЁа-яё]'
    punct = ''
    for l in word[::-1]:
        if not re.search(rus, l):
            word = word[:len(word)-1]
            punct = l + punct
    return word, punct


def answer(text, lemma_list, m):

    words = text.split()
    answer = ''
    for word in words:
        word, punct = get_punct(word)
        ana = m.parse(word)
        char = str(ana[0].tag).split(' ')[0]

        if char != 'PREP' and char.split(',')[0] != 'NPRO':
            if char in lemma_list:
                word = random.choice(lemma_list[char])
        if type(m.parse(word)) == list:
            word = m.parse(word)[0]
        else:
            word = m.parse(word)

        if ' ' in str(ana[0].tag):
            grams = str(ana[0].tag).split(' ')[1].split(',')
            for gr in grams:
                try:
                    word = word.inflect({gr})
                except:
                    pass

        answer = answer + word.word + punct + ' '
    return(answer)


def chat_bot():

    f = open('lemma_list.json')
    lemma_list = json.load(f)
    f.close()

    m = MorphAnalyzer()
    text = ' '

    while text:
        text = input('Tell me smth!\n')
        print(answer(text, lemma_list, m))


def main():
    chat_bot()


if __name__ == '__main__':
    main()