import requests
from bs4 import BeautifulSoup
import lxml
import json

url = 'https://www.spr.ru/all/'

# req = requests.get(url)
# src = req.text
#
# soup = BeautifulSoup(src, 'lxml')
#
# sections_dict = {}
# sections = soup.find_all(class_='zagolovok')
#
# for item in sections:
#     name = item.text.strip()
#     href = 'http:' + item.get('href')
#     sections_dict[name] = href
#
# with open('sections.json', 'w', encoding='utf-8') as f:
#     json.dump(sections_dict, f, indent=4, ensure_ascii=False)

with open('sections.json', encoding='utf-8') as f:
    all_categories = json.load(f)

for category_title, category_link in all_categories.items():
    rep = [' ', ',', "'", '-']

    for item in rep:
        if item in category_title:
            category_title = category_title.replace(item, '_')

    # req = requests.get(category_link)
    # src = req.text

    # soup = BeautifulSoup(src, 'lxml')
    # table = soup.find(id_='leftside')
    # sections = soup.find_all('div', attrs={'style': 'margin-bottom:7px;'})
    # print(soup)
    # with open(f'data/{category_title}.html', 'w', encoding='utf-8') as f:
    #   f.write(src)
    # category_dict = {}
    # for item in sections:
    #     name = item.text
    #     href = item.get('href')
    #     category_dict[name] = href
    # with open(f'data/{category_title}.json', 'w', encoding='utf-8') as f:
    #     json.dump(category_dict, f, indent=4, ensure_ascii=False)
    #
    # with open(f'data/{category_title}.html', encoding='utf-8') as f:
    #     src = f.read()
    #
    # soup = BeautifulSoup(src, 'lxml')
    # table = soup.find(id_='leftside')
    # sections = soup.find_all('div', attrs={'style': 'margin-bottom:7px;'})
    # category_dict = {}
    #
    # for item in sections:
    #     name = item.text
    #     href = item.find('a').get('href')
    #     category_dict[name] = 'http:' + href
    # print(category_dict)
    #
    # with open(f'data/{category_title}.json', 'w', encoding='utf-8') as f:
    #     json.dump(category_dict, f, indent=4, ensure_ascii=False)

    with open(f'data/{category_title}.json', encoding='utf-8') as f:
        items_page = json.load(f)

    res_dict = {}
    for item_title, item_link in items_page.items():
        rep = [' ', ',', "'", '-']

        for item in rep:
            if item in item_title:
                item_title = item_title.replace(item, '_')

        req = requests.get(item_link)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        items_page_dict = {}

        itemFlex = soup.find_all(class_='itemFlex')

        for item in itemFlex:
            title = item.find(class_='itemFlexInfo').find('b').text
            item_review = {
                'good': item.find(class_='good').text,
                'bad': item.find(class_='bad').text,

            }
            if item != None:
                adress = item.find(class_='filialAddress')
                if adress != None:
                    adress = adress.text

            items_page_dict[title] = {
                'title': title,
                'info': {
                    'item_review': item_review,
                    'adress': adress
                }
            }

        res_dict[item_title] = items_page_dict
        print(res_dict)
        with open(f'data/res/{item_title}', 'w', encoding='utf-8') as f:
            json.dump(res_dict, f, indent=4, ensure_ascii=False)


