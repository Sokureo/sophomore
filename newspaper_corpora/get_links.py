import urllib.request
import os
import re

def get_links():
    commonUrl = 'http://udmpravda.ru/'
    links_url = []
    req = urllib.request.Request(commonUrl)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        regLink = re.compile('(?:<a href=")(.+?)(?:">.+?</a>)', flags=re.U | re.DOTALL)
        links = regLink.findall(html)
    for indx, pageUrl in enumerate(links):
        links[indx] = commonUrl + pageUrl
        try:
            page = urllib.request.urlopen(links[indx])
            html = page.read().decode('utf-8')
        except:
            print('Error at', links[indx])
            continue
        if links[indx] not in links_url:
            links_url.append(links[indx])
            
    return links_url

