import urllib.request, re, html


def processing():
    links = []
    f = open('links.txt', 'r', encoding = 'utf-8')
    for line in f:
        links.append(line)
    f.close()
    return links


def text(links):
    regs = ['</span></p>.*?<p>(.+?)</p>[^</p>]*?</div>.*?<!-- content end  -->',
           '<div class="announce">.*?</div>.*?<p>(.+?)\n</p>  </div>',
            '<div class="story" itemprop="articleBody">.*?<div>(.+?)</div>[^</div>]*?</div>',
            '</strong>. (.+?)</p>[^</p>]*?</div>'
            ]
    texts = []
    for link in links:
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        req = urllib.request.Request(link, headers={'User-Agent':user_agent})
        with urllib.request.urlopen(req) as response:
            html_page = response.read().decode('utf-8')
            for reg in regs:
                regLink = re.compile(reg, flags=re.U | re.DOTALL)
                text = regLink.search(html_page)
                if text:
                    new_text = text.group(1)
                    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
                    regSpace = re.compile('\s', flags=re.U | re.DOTALL)
                    new_text = regTag.sub('', html.unescape(new_text))
                    new_text = regSpace.sub(' ', new_text)
                    texts.append(new_text)
    return texts


def words(texts):
    clean_words = []
    for text in texts:
        words = text.split()
        for indx, word in enumerate(words):
            words[indx] = word.strip(' ,:«».!?')
            if words[indx] == '' or words[indx] == '–':
                words.remove(words[indx])
        clean_words.append(words)
    return clean_words


def words_set(clean_words):
    sets = []
    for words in clean_words:
        sets.append(set(words))
    return sets


def inter_sets(sets):
    fw = open('intersection.txt', 'w', encoding = 'utf-8')
    inter = sets[0] & sets[1] & sets[2] & sets[3]
    for i in sorted(inter):
        fw.write(i + '\n')
    fw.close()


def frequency(sets):
    freq_dict = {}
    for word_set in sets:
        for word in word_set:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
    return freq_dict


def diff_sets(sets, freq_dict):
    fw = open('difference.txt', 'w', encoding = 'utf-8')
    dif = sets[0] ^ sets[1] ^ sets[2] ^ sets[3]
    for i in sorted(dif):
        if freq_dict[i] > 1:
            fw.write(i + '\n')
    fw.close()


def main():
    sets = words_set(words(text(processing())))
    inter_sets(sets)
    diff_sets(sets, frequency(sets))

if __name__ == '__main__':
    main()