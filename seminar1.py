import urllib.request
import re

def processing():
    req = urllib.request.Request('https://yandex.ru/pogoda/moscow')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return(html)

def tempr(html):
    res = re.compile('.[0-9]+ °C', flags = re.U|re.DOTALL)
    tempr = res.findall(html)
    for fil in tempr:
        print("Температура: ", fil)

def overcast(html):
    overcast2 = []
    res = re.compile('<[^<]*?"current-weather__comment">.*?</span><div class="current-weather.*?>', flags = re.U|re.DOTALL)
    overcast = res.findall(html)
    regTag = re.compile('<.*?>', flags = re.U | re.DOTALL)
    for ov in overcast:
        clean_ov = regTag.sub("", ov)
        overcast2.append(clean_ov)
    for ov in overcast2:
        print("Облачность: ", ov)

def sunrise(html):
    sun2 = []
    res = re.compile('<[^<]*?Восход.*?>[0-9]+?:[0-9]+?<.*?>', flags = re.U|re.DOTALL)
    sun = res.findall(html)
    regTag = re.compile('<.*?>', flags = re.U | re.DOTALL)
    for time in sun:
        clean_time = regTag.sub("", time)
        sun2.append(clean_time)
    print(sun2[0])

def sunset(html):
    sun2 = []
    res = re.compile('<[^<]*?Закат.*?>[0-9]+?:[0-9]+?<.*?>', flags = re.U|re.DOTALL)
    sun = res.findall(html)
    regTag = re.compile('<.*?>', flags = re.U | re.DOTALL)
    for time in sun:
        clean_time = regTag.sub("", time)
        sun2.append(clean_time)
    print(sun2[0])

def main():
    html = processing()
    tempr(html)
    overcast(html)
    sunrise(html)
    sunset(html)

if __name__ == '__main__':
    main()
