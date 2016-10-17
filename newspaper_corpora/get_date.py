import re

def get_date(html):
    monthes = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 10,
    'декабря': 12
                }

    reg = re.compile("<span class='date'>([0-9]{1,2}) ([А-Яа-яЁё]+?) ([0-9]{4})</span>", flags=re.U | re.DOTALL)
    regex = re.search(reg, html)
    if regex:
        date = regex.group(1)
        month = regex.group(2)
        year = regex.group(3)
    
        for k in monthes:
            if month == k:
                month = str(monthes[k])
        date = date + '.' + month + '.' + year
    else:
        date = 'Nodate'
        month = 'Nomonth'
        year = 'Noyear'
    return(date, month, year)
