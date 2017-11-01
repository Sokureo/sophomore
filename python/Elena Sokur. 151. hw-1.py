import urllib.request
import re

def processing():
    req = urllib.request.Request('http://udmpravda.ru/')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return(html)

def titles(html):
    titles2 = []
    res = re.compile('<[^<]*?>[а-яА-ЯЁё0-9 ]+?(?:</a>|</h[0-9]?>|</title>)', flags = re.U|re.DOTALL)
    titles = res.findall(html)
    regTag = re.compile('<.*?>', flags = re.U | re.DOTALL)
    regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
    for t in titles:
        clean_t = regSpace.sub("", t)
        clean_t = regTag.sub("", t)
        titles2.append(clean_t)
    fw = open('titles.txt', 'w')
    for t in titles2:
        fw.write(t)
        fw.write('\n')
    fw.close()

def main():
    html = processing()
    titles(html)

if __name__ == '__main__':
    main()
