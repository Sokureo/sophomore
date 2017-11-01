import re

def get_author(html):
    reg = re.compile('<a>Автор статьи.+<strong>([А-Яа-яёЁ ]+)</strong>', flags=re.U | re.DOTALL)
    regex = re.search(reg, html)
    if regex:
        author = regex.group(1)
    else:
        author = 'Noname'
    return(author)
