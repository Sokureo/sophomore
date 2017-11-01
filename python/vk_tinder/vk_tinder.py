import json
import re
import requests
from rutermextract import TermExtractor
import conf
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results')
def results():
    term_extractor = TermExtractor()
    group_id = request.args['group'].strip('vk.com/clubvk.com/group')  # 122739405
    members = get_members(group_id)
    main_user = request.args['main_user'].strip('vk.com/')  #792255
    if main_user in members:
        members.remove(main_user)
    result = vk_tinder(main_user, members, term_extractor)

    i = 1
    to_show = []
    for k in sorted(result, reverse=True):
        for res in result[k]:
            if i <= 5:
                member = vk_api('users.get', user_ids=res, v='5.63', fields='photo_200_orig, first_name, last_name', access_token=conf.access_token)
                if 'response' in member:
                    to_show.append([str(i) + '.    ', member['response'][0]['first_name'] + ' ' + member['response'][0]['last_name'],
                                member['response'][0]['photo_200_orig'], 'vk.com/' + str(res), 'Количество очков: ' + str(k)])
                    i += 1
            else:
                break

    return render_template('results.html', results=to_show)


def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def get_age(bdate):

     # Высчитываем возраст (актуально только для июня 2017)
    res = re.search('[0-9]+.([0-9]+).([0-9]+)', bdate)
    if res:
        if int(res.group(1)) < 6:
            age = 2017 - int(res.group(2))
        else:
            age = 2017 - int(res.group(2)) - 1
    else:
        age = None
    return age


def get_members(group_id):
    members = []
    item_count = 1000

    while item_count == 1000:
        result = vk_api('groups.getMembers', group_id=group_id, v='5.63', count=1000, offset=len(members))
        members += result['response']['items']
        item_count = len(result['response']['items'])

    return members


def how_close(memb_1, memb_2):
    points = 0

    for indx, thing in enumerate(memb_1):
        if type(thing) == list and type(memb_2[indx]) == list:
            for el in thing:
                if el != '' and el != None and el in memb_2[indx]:
                    points += 1
        elif thing != '' and thing != None and thing == memb_2[indx]:
                points += 1

    return points


def get_user_info(member, term_extractor):

    member_info = [None for n in range(21)]
    fields = 'bdate, city, country, home_town, universities, status, followers_count,' \
             'relation, personal, connections, interests, music, movies, books, about, quotes'

    groups = vk_api('groups.get', user_id=member, v='5.63', access_token=conf.access_token)
    info = vk_api('users.get', user_ids=member, v='5.63', fields=fields, access_token=conf.access_token)

    if 'response' in info and 'response' in groups:
        group = groups['response']["items"] if 'response' in groups else None
        age = get_age(info['response'][0]['bdate']) if 'bdate' in info['response'][0] else None
        city = info['response'][0]['city']['id'] if 'city' in info['response'][0] else None
        country = info['response'][0]['country']['id'] if 'country' in info['response'][0] else None
        followers = info['response'][0]['followers_count'] if 'followers_count' in info['response'][0] else None
        home_town = info['response'][0]['home_town'] if 'home_town' in info['response'][0] else None
        relation = info['response'][0]['relation'] if 'relation' in info['response'][0] else None
        political = info['response'][0]['personal']['political'] if 'personal' in info['response'][0] \
                        and 'political' in info['response'][0]['personal'] else None
        religion = info['response'][0]['personal']['religion'] if 'personal' in info['response'][0] \
                        and 'religion' in info['response'][0]['personal'] else None
        interests = info['response'][0]['interests'].split(', ') if 'interests' in info['response'][0] else None
        music = info['response'][0]['music'].split(', ') if 'music' in info['response'][0] else None
        movies = info['response'][0]['movies'].split(', ') if 'movies' in info['response'][0] else None
        books = info['response'][0]['books'].split(', ') if 'books' in info['response'][0] else None
        uni = info['response'][0]['universities'][0]['id'] if 'universities' in info['response'][0] \
                        and len(info['response'][0]['universities']) > 0 and 'id' in info['response'][0]['universities'][0] else None
        fac = info['response'][0]['universities'][0]['faculty_name'] if 'universities' in info['response'][0] \
                       and len(info['response'][0]['universities']) > 0 and 'faculty_name' in info['response'][0]['universities'][0] else None
        chair = info['response'][0]['universities'][0]['chair_name'] if 'universities' in info['response'][0] \
                        and len(info['response'][0]['universities']) > 0 and 'chair_name' in info['response'][0]['universities'][0] else None
        graduation = info['response'][0]['universities'][0]['graduation'] if 'universities' in info['response'][0] \
                       and len(info['response'][0]['universities']) > 0 and 'graduation' in info['response'][0]['universities'][0] else None
        education_status = info['response'][0]['universities'][0]['education_status'] if 'universities' in info['response'][0] \
                       and len(info['response'][0]['universities']) > 0and 'education_status' in info['response'][0]['universities'][0] else None
        status = [i.normalized for i in term_extractor(info['response'][0]['status'])] if 'status' in info['response'][0] else None
        about = [i.normalized for i in term_extractor(info['response'][0]['about'])] if 'about' in info['response'][0] else None
        quotes = [i.normalized for i in term_extractor(info['response'][0]['quotes'])] if 'quotes' in info['response'][0] else None

        member_info = [group, age, city, country, followers, home_town, relation, political, religion, interests, music,
                        movies, books, uni, fac, chair, graduation, education_status, status, about, quotes]

    return member_info


def vk_tinder(main_user, members, term_extractor):

    closeness = {}
    main_user_info = get_user_info(main_user, term_extractor)

    for memb in members:
        memb_info = get_user_info(memb, term_extractor)
        points = how_close(main_user_info, memb_info)
        if points in closeness:
            closeness[points].append(memb)
        else:
            closeness[points] = [memb]

    return closeness


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

