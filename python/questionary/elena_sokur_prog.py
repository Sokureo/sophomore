from flask import Flask, render_template, request, redirect, url_for
import json, urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

jarray = []

@app.route('/answers')
def answers():
    data = []
    f = open('answers.json', 'r', encoding='utf-8')
    res = json.load(f)
    f.close()
    for k in sorted(request.args):
        data.append(request.args[k])
    res.append(data)
    f = open('answers.json', 'w', encoding='utf-8')
    f.write('[' + '\n')
    for indx, r in enumerate(res):
        s = json.dumps(r, ensure_ascii=False)
        if indx+1 != len(res):
            f.write(s + ',' + '\n')
        else:
            f.write(s)
    f.write('\n' + ']')
    f.close()
    return render_template('answers.html')

@app.route('/stats')
def stat():
    dictin = {}
    stats = {}
    f = open('answers.json', 'r', encoding='utf-8')
    data = json.load(f)
    number = len(data)
    for answer in data:
        if 'Возраст' in dictin:
            dictin['Возраст'].append(answer[0])
        else:
            dictin['Возраст'] = [answer[0]]
        if 'Место рождения' in dictin:
            dictin['Место рождения'].append(answer[1])
        else:
            dictin['Место рождения'] = [answer[1]]
        if '1. Обломки лыж валялись в лесу.' in dictin:
            dictin['1. Обломки лыж валялись в лесу.'].append(answer[3])
        else:
            dictin['1. Обломки лыж валялись в лесу.'] = [answer[3]]
        if '2. Я поломал лыжи на части.' in dictin:
            dictin['2. Я поломал лыжи на части.'].append(answer[4])
        else:
            dictin['2. Я поломал лыжи на части.'] = [answer[4]]
        if '3. Солдат был ранен осколком.' in dictin:
            dictin['3. Солдат был ранен осколком.'].append(answer[5])
        else:
            dictin['3. Солдат был ранен осколком.'] = [answer[5]]
        if '4. Снаряд разлетелся на осколки.' in dictin:
            dictin['4. Снаряд разлетелся на осколки.'].append(answer[6])
        else:
            dictin['4. Снаряд разлетелся на осколки.'] = [answer[6]]
        if '5. Я поранился осколком стекла.' in dictin:
            dictin['5. Я поранился осколком стекла.'].append(answer[7])
        else:
            dictin['5. Я поранился осколком стекла.'] = [answer[7]]
        if '6. Я отрезал от каравая два ломтя.' in dictin:
            dictin['6. Я отрезал от каравая два ломтя.'].append(answer[8])
        else:
            dictin['6. Я отрезал от каравая два ломтя.'] = [answer[8]]
        if '7. Возле сарая лежали обломки бревна.' in dictin:
            dictin['7. Возле сарая лежали обломки бревна.'].append(answer[9])
        else:
            dictin['7. Возле сарая лежали обломки бревна.'] = [answer[9]]
        if '8. На тарелке лежали куски огурца.' in dictin:
            dictin['8. На тарелке лежали куски огурца.'].append(answer[10])
        else:
            dictin['8. На тарелке лежали куски огурца.'] = [answer[10]]
        if '9. Дайте мне небольшой отрез ткани.' in dictin:
            dictin['9. Дайте мне небольшой отрез ткани.'].append(answer[11])
        else:
            dictin['9. Дайте мне небольшой отрез ткани.'] = [answer[11]]
        if '10. Мне в яичнице попались осколки скорлупы.' in dictin:
            dictin['10. Мне в яичнице попались осколки скорлупы.'].append(answer[12])
        else:
            dictin['10. Мне в яичнице попались осколки скорлупы.'] = [answer[12]]
    for pair in dictin:
        d_freq = {}
        for word in dictin[pair]:
            if word in d_freq:
                d_freq[word]+=1
            else:
                d_freq[word] = 1
        stats[pair] = d_freq
    return render_template('stats.html', number=number, stats=stats)


@app.route('/json')
def data():
    f = open('answers.json', 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return render_template('json.html', data=data)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results')
def results():
    f = open('answers.json', 'r', encoding='utf-8')
    data = json.load(f)
    word = request.args['word']
    results = []
    for answer in data:
        for res in answer:
            if word in res:
                results.append(res)
    if results == []:
        results.append('Извините, по Вашему запросу ничего не найдено.')
    else:
        for indx, res in enumerate(results):
            results[indx] = str(indx+1) + '. ' + res
    return render_template('results.html', results=results, word=word)

if __name__ == '__main__':
    app.run(debug=True)

