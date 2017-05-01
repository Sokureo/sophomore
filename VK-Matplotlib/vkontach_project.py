import copy
import requests
import json
import re
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

from collections import Counter


def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)


def get_posts(group_id):
    posts = []
    post_ids = []
    item_count = 200

    while len(posts) < item_count:
        result = vk_api('wall.get', owner_id=-group_id, v='5.63', count=100, offset=len(posts)) # Скачиваем стенку
        posts += result['response']["items"] # Получаем массив с постами (200 штук)

    post_texts = [post['text'] for post in posts] # Получаем массив с текстами постов (200 штук)
    for indx, post in enumerate(posts):
        if 'signer_id' in post.keys():
            post_ids.append(post['signer_id'])
        else:
            post_ids.append('None') # и массив с id авторов постов

    fw = open('post_texts.txt', 'w', encoding='utf-8')
    for text in post_texts:
        fw.write(text + '\n-----------------------------------------------------\n\n')
    fw.close()

    return posts, post_texts, post_ids


def get_comments(group_id, posts):
    comments = [[] for post in posts] # Делаем пустой массив с массивами длиной в количество постов, чтобы можно было обращаться по индексу
    comment_ids = []
    comment_len = []
    item_count = 200

    for indx, post in enumerate(posts):
        while len(comments[indx]) < item_count and len(comments[indx]) < posts[indx]['comments']['count']:
            result = vk_api('wall.getComments', owner_id=-group_id, post_id=posts[indx]['id'], v='5.63', count=100, offset=len(comments[indx]))
            comments[indx] += result['response']['items'] # Скачиваем комментарии (200 штук, если есть)
            comment_ids += [res['from_id'] for res in result['response']['items']] # массив с id авторов комментариев
            comment_len += [len(res['text'].split()) for res in result['response']['items']]

    comment_texts = [[] for post in posts]
    for indx, comment in enumerate(comments): # Получаем массив массивов с текстами комментариев
        comment_texts[indx] += [comm['text'] for comm in comment]

    fw = open('comment_texts.txt', 'w', encoding='utf-8')
    for text in comment_texts:
        for t in text:
            fw.write(t + '\n-----------------------------------------------------\n\n')
    fw.close()

    return comments, comment_texts, comment_ids, comment_len


def length(post_texts, comment_texts):
    fw = open('len_info.csv', 'w', encoding='utf-8')
    post_len = []
    comment_av_len = [0 for post in post_texts]

    for indx, text in enumerate(post_texts): # Записываем длину поста и длину комментариев к нему в csv
        fw.write(str(len(text.split())) + ' ')
        post_len.append(len(text.split())) # Создаём массив с длинами постов
        for comm in comment_texts[indx]:
                fw.write(str(len(comm.split())) + ' ')
                comment_av_len[indx] += len(comm.split())
        if len(comment_texts[indx]) != 0:
            comment_av_len[indx] /= len(comment_texts[indx]) # и массив со средними длинами комменатриев к постам
        fw.write('\n')

    fw.close()
    return post_len, comment_av_len


def graph_post_comment(post_len, comment_av_len): # Рисуем график корреляции длины постов и средней длины комментариев к нему
    plt.scatter(post_len, comment_av_len, s=30, alpha=0.7, c='c')
    plt.title('Correlation between length of posts and comments')
    plt.xlabel('Length of Posts')
    plt.ylabel('Average Length of Comments')
    plt.savefig('graph_1_post_comment')
    plt.close()


def get_city_age_post(post_ids, post_len):
    while 'None' in post_ids: # За одну итерацию почему-то не удаляет (только за две)
        for indx, id in enumerate(post_ids):
            if id == 'None':
                del post_ids[indx]
                del post_len[indx] # Удаляем длины постов, у которых нет автора
    post_len_id = post_len

    cities = []
    bdates = []
    ages = []

    for i in range(0, len(post_ids)): # По одному за раз, ибо на самом деле посты пишут только 7 пользователей, а информацию о пользователе он возвращает только один раз за запрос
        user_info = vk_api('users.get', user_ids=(str(post_ids[i])), fields='bdate,city', v='5.63')
        for i in user_info['response']:
            if 'city' in i:
                cities.append(i['city']['title'])
            else:
                cities.append('None') # Делаем массив с городами авторов постов

        for i in user_info['response']:
            if 'bdate' in i:
                bdates.append(i['bdate'])
            else:
                bdates.append('None') # и массив с датами рождения

    for bd in bdates: # Высчитываем возраст (актуально только для мая 2017)
        res = re.search('[0-9]+.([0-9]+).([0-9]+)', bd)
        if res:
            if int(res.group(1)) < 5:
                ages.append(2017 - int(res.group(2)))
            else:
                ages.append(2017 - int(res.group(2)) - 1)
        else:
            ages.append('None')

    return post_len_id, cities, ages


def graph_city_post(post_len_id, cities):
    dict_cities = {}
    post_len_id_cit = copy.copy(post_len_id)

    while 'None' in cities:
        for indx, c in enumerate(cities):
            if c == 'None':
                del cities[indx]
                del post_len_id_cit[indx] # Удаляем длины постов, у которых нет города

    freq_city_dict = Counter(cities) # Создаём частотный словарь городов

    for indx, c in enumerate(cities):
        if c in dict_cities:
            dict_cities[c] += post_len_id_cit[indx]
        else:
            dict_cities[c] = post_len_id_cit[indx]

    for c in dict_cities.keys():
        dict_cities[c] /= freq_city_dict[c] # Высчитываем среднюю длину поста для каждого города

    keys = [key for key in dict_cities.keys()]
    values = [value for value in dict_cities.values()]

    plt.figure(figsize=(20, 10))
    plt.bar(range(len(values)), values)
    plt.xticks(range(len(keys)), keys, rotation='vertical')
    plt.title('Correlation between city and average length of post')
    plt.ylabel('Average Length of Post')
    plt.savefig('graph_2_city_post')
    plt.close()


def get_city_age_comment(comment_ids):
    cities_comm = []
    bdates_comm = []
    ages_comm = []

    for i in range(0, len(comment_ids)): # По одному за раз, ибо информацию об одном пользователе он возвращает только один раз за запрос
        user_info = vk_api('users.get', user_ids=(str(comment_ids[i])), fields='bdate,city', v='5.63')
        for i in user_info['response']:
            if 'city' in i:
                cities_comm.append(i['city']['title'])
            else:
                cities_comm.append('None') # Делаем массив с городами авторов комментариев

        for i in user_info['response']:
            if 'bdate' in i:
                bdates_comm.append(i['bdate'])
            else:
                bdates_comm.append('None') # и массив с датами рождения

    for bd in bdates_comm: # Высчитываем возраст (актуально только для мая 2017)
        res = re.search('[0-9]+.([0-9]+).([0-9]+)', bd)
        if res:
            if int(res.group(1)) < 5:
                ages_comm.append(2017 - int(res.group(2)))
            else:
                ages_comm.append(2017 - int(res.group(2)) - 1)
        else:
            ages_comm.append('None')

    return cities_comm, ages_comm


def graph_city_comm(cities_comm, comment_len):
    dict_cities_comm = {}
    freq_city_dict_comm = {}
    comment_len_cit = copy.copy(comment_len)

    while 'None' in cities_comm:
        for indx, c in enumerate(cities_comm):
            if c == 'None':
                del cities_comm[indx]
                del comment_len_cit[indx] # Удаляем длины комментариев, у которых нет города

    for c in cities_comm: # Создаём частотный словарь городов (Counter не смог)
        if c in freq_city_dict_comm:
            freq_city_dict_comm[c] += 1
        else:
            freq_city_dict_comm[c] = 1

    for indx, c in enumerate(cities_comm):
        if c in dict_cities_comm:
            dict_cities_comm[c] += comment_len_cit[indx]
        else:
            dict_cities_comm[c] = comment_len_cit[indx]

    for c in dict_cities_comm.keys():
        dict_cities_comm[c] /= freq_city_dict_comm[c] # Высчитываем среднюю длину комментария для каждого города

    keys = [key for key in dict_cities_comm.keys()]
    values = [value for value in dict_cities_comm.values()]

    plt.figure(figsize=(20, 10))
    plt.bar(range(len(values)), values)
    plt.xticks(range(len(keys)), keys, rotation='vertical')
    plt.title('Correlation between city and average length of comment')
    plt.ylabel('Average Length of Comment')
    plt.savefig('graph_3_city_comment')
    plt.close()

    plt.figure(figsize=(20, 10))
    plt.bar(range(len(values[:20])), values[:20]) # Для наглядности берём первые двадцать
    plt.xticks(range(len(keys[:20])), keys[:20], rotation='vertical')
    plt.title('Correlation between city and average length of comment')
    plt.ylabel('Average Length of Comment')
    plt.savefig('graph_4_city_comment_20')
    plt.close()


def graph_age(post_len_id, ages, comment_len, ages_comm):
    dict_ages = {}
    dict_ages_comm = {}
    freq_ages_dict_comm = {}

    while 'None' in ages:
        for indx, a in enumerate(ages):
            if a == 'None':
                del ages[indx]
                del post_len_id[indx] # Удаляем длины постов, у которых нет возраста

    freq_ages_dict = Counter(ages) # Создаём частотный словарь возрастов

    for indx, a in enumerate(ages):
        if a in dict_ages:
            dict_ages[a] += post_len_id[indx]
        else:
            dict_ages[a] = post_len_id[indx]

    for a in dict_ages.keys():
        dict_ages[a] /= freq_ages_dict[a] # Высчитываем среднюю длину поста для каждого возраста

    keys_age = []
    values_age = []
    for key in sorted(dict_ages): # Чтобы не получалась ломаная фигура, сортируем по возрастанию координаты
        keys_age.append(key)
        values_age.append(dict_ages[key])

    while 'None' in ages_comm:
        for indx, a in enumerate(ages_comm):
            if a == 'None':
                del ages_comm[indx]
                del comment_len[indx] # Удаляем длины комментариев, у которых нет возраста

    for a in ages_comm: # Создаём частотный словарь возрастов (Counter не смог)
        if a in freq_ages_dict_comm:
            freq_ages_dict_comm[a] += 1
        else:
            freq_ages_dict_comm[a] = 1

    for indx, a in enumerate(ages_comm):
        if a in dict_ages_comm:
            dict_ages_comm[a] += comment_len[indx]
        else:
            dict_ages_comm[a] = comment_len[indx]

    for a in dict_ages_comm.keys():
        dict_ages_comm[a] /= freq_ages_dict_comm[a] # Высчитываем среднюю длину комментария для каждого возраста

    keys_comm_age = []
    values_comm_age = []
    for key in sorted(dict_ages_comm):
        keys_comm_age.append(key)
        values_comm_age.append(dict_ages_comm[key])

    plt.plot(keys_age, values_age, c='c', label='Посты')
    plt.plot(keys_comm_age, values_comm_age, c='g', label='Комментарии')
    plt.title('Correlation between age and average length of post or comment')
    plt.xlabel('Ages')
    plt.ylabel('Average Length of Post or Comment')
    plt.legend()
    plt.grid(True, color='orchid')
    plt.savefig('graph_5_age_post_comment')
    plt.close()

    plt.plot(keys_age[:20], values_age[:20], c='c', label='Посты') # Для наглядности берём первые двадцать
    plt.plot(keys_comm_age[:20], values_comm_age[:20], c='g', label='Комментарии')
    plt.title('Correlation between age and average length of post or comment')
    plt.xlabel('Ages')
    plt.ylabel('Average Length of Post or Comment')
    plt.legend()
    plt.grid(True, color='orchid')
    plt.savefig('graph_6_age_post_comment_20')
    plt.close()


def main():
    group_id = 25557243 # BadComedian
    posts, post_texts, post_ids = get_posts(group_id)
    comments, comment_texts, comment_ids, comment_len = get_comments(group_id, posts)
    post_len, comment_av_len = length(post_texts, comment_texts)
    graph_post_comment(post_len, comment_av_len)
    post_len_id, cities, ages = get_city_age_post(post_ids, post_len)
    graph_city_post(post_len_id, cities)
    cities_comm, ages_comm = get_city_age_comment(comment_ids)
    graph_city_comm(cities_comm, comment_len)
    graph_age(post_len_id, ages, comment_len, ages_comm)

if __name__ == '__main__':
    main()