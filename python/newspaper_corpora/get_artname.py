import re
import random 

def get_artname(html, pageURL):
    reg = re.compile("<title>\nУдмуртская правда\n»(?: ([0-9А-ЯЁа-яё ,.!?:;«»-]+) »)? ([0-9А-ЯЁа-яё ,.!?:;«»-]+)\n</title>", flags=re.U | re.DOTALL)
    regex = re.search(reg, html)
    if regex:
        topic = regex.group(1)
        header = regex.group(2)
    else:
        topic = 'Notopic'
        header = 'Noheader'

    reg = re.compile("([0-9A-Za-z]+)$", flags=re.U | re.DOTALL)
    regex = re.search(reg, pageURL)
    if regex:
        artname = regex.group(1)
        if artname == 'xml' or artname == '2016':
            artname = artname + str(random.randint(0,1000))        
    else:
        artname = 'Noartname'
        
    return(header, topic, artname)
