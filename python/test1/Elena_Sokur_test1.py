import re, os, html, json
from flask import Flask, render_template, request

app = Flask(__name__)

def thai():
    lst = []
    dictin = {}
    regex = re.compile("<tr><td class=th><a href='/id/.+?'>(.+?)</a></td><td>.+?</td><td>(.+?)</td></tr>", flags=re.U | re.DOTALL)
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
    reg1 = re.compile('\xa0', flags=re.U | re.DOTALL)
    for root, dirs, files in os.walk('.\\thai_pages'):
        for fl in files:
            f = open(root + os.sep + fl, 'r', encoding = 'utf-8')
            text = f.read()
            words = regex.findall(text)
            for word in words:
                for w in word:
                    clean_word = regTag.sub("", w)
                    clean_word = reg1.sub("", clean_word)
                    lst.append(clean_word)
    for i in range(0, len(lst), 2):
        lst[i] = html.unescape(lst[i])
        lst[i+1] = html.unescape(lst[i+1])
        dictin[lst[i]] = lst[i+1]
    return dictin

def processing_thai(dictin):
    f = open('thai_dictionary.json', 'w', encoding='utf-8')
    s = json.dumps(dictin, ensure_ascii=False)
    f.write(s)
    f.close()

def english(dictin):
    eng_dictin = {}
    for word in dictin:
        if dictin[word] not in eng_dictin:
            eng_dictin[dictin[word]] = [word]
        else:
            eng_dictin[dictin[word]].append(word)
    return eng_dictin

def processing_eng(eng_dictin):
    f = open('english_dictionary.json', 'w', encoding='utf-8')
    s = json.dumps(eng_dictin, ensure_ascii=False)
    f.write(s)
    f.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    f = open('english_dictionary.json', 'r', encoding='utf-8')
    data = json.load(f)
    word = request.args['word']
    results = []
    for eng in data:
        if word in eng:
            for w in data[eng]:
                results.append(w)
    if results == []:
        results.append('Извините, по Вашему запросу ничего не найдено.')
    else:
        for indx, res in enumerate(results):
            results[indx] = str(indx+1) + '. ' + res
    return render_template('results.html', results=results)

def main():
    processing_thai(thai())
    processing_eng(english(thai()))

if __name__ == '__main__':
    main()
    app.run(debug=True)