import urllib.request
import os
import re
import get_date
import get_author
import get_artname
import get_links
import time

def get_page(link):
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return(html)

def get_article(html):
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
    regScript = re.compile('<script.+?>.*?</script>', flags=re.U | re.DOTALL)
    regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)
    regSpace = re.compile('\s', flags=re.U | re.DOTALL)
    article = regScript.sub('', html)
    article = regComment.sub('', article)
    article = regTag.sub('', article)
    article = regSpace.sub(' ', article)
    return article

def metadata(path, author, header, artname, date, topic, link, year):
    row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\tУдмуртская правда\t\t%s\tгазета\tРоссия\tУдмуртская Республика\tru\n'
    path = path + os.sep + artname + '.txt'
    fa = open('C:' + os.sep + 'Udmurtskaya_pravda' + os.sep + 'metadata.csv', 'a', encoding = 'utf-8')
    fa.write(row %(path, author, header, date, topic, link, year))
    fa.close()

def foldering_plain(article, path, header, artname, author, date, topic, link):
    row = '@au %s\n@ti %s\n@da %s\n@topic %s\n@url %s\n%s'
    if not os.path.exists(path):
        os.makedirs(path)
    fw = open(path + os.sep + artname + '.txt', 'w', encoding = 'utf-8')
    fw.write(row %(author, header, date, topic, link, article))
    fw.close()
        
def foldering_mystem_xml():
    for root, dirs, files in os.walk('C:' + os.sep + 'Udmurtskaya_pravda' + os.sep + 'plain'):
        for fl in files:
            rout = root.replace('plain', 'mystem-xml')
            if not os.path.exists(rout):
                os.makedirs(rout)
            inp = root + os.sep + fl
            outp = inp.replace('plain', 'mystem-xml')
            outp = outp.replace('.txt', '.xml') 
            os.system(r'C:\mystem.exe -ncid --format xml ' + inp + ' ' + outp)

def foldering_mystem_txt():
    for root, dirs, files in os.walk('C:' + os.sep + 'Udmurtskaya_pravda' + os.sep + 'plain'):
        for fl in files:
            rout = root.replace('plain', 'mystem-plain')
            if not os.path.exists(rout):
                os.makedirs(rout)
            inp = root + os.sep + fl
            outp = inp.replace('plain', 'mystem-plain')        
            os.system(r'C:\mystem.exe -ncid ' + inp + ' ' + outp)
                
def main():
    if not os.path.exists('C:' + os.sep + 'Udmurtskaya_pravda'):
        os.makedirs('C:' + os.sep + 'Udmurtskaya_pravda')
    links = get_links.get_links()
    for link in links:
        html = get_page(link)
        article = get_article(html)
        date, month, year = get_date.get_date(html)
        author = get_author.get_author(html)
        header, topic, artname = get_artname.get_artname(html, link)
        path = 'C:' + os.sep + 'Udmurtskaya_pravda' + os.sep + 'plain' + os.sep + year + os.sep + month 
        metadata(path, author, header, artname, date, topic, link, year)
        foldering_plain(article, path, header, artname, author, date, topic, link)                      
        time.sleep(2)
    foldering_mystem_txt()
    foldering_mystem_xml()
    
if __name__ == '__main__':
    main()


