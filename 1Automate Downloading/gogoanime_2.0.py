#verson 2.0
from googlesearch import search

def check_anime_spell(name):
    result = search(name + ' myanimelist', num_results=10)
    for link in result:
        link = link.split('/')
        if link[-3] == 'anime' and link[-4] == 'myanimelist.net':
            return link[-1].replace('_', ' ')

def audo_dl(link):
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    button = soup.find(class_ = 'dowloads')
    stream_link = str(button).split('href="')[1].split('" ')[0]
    print(stream_link)
    page = requests.get(stream_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    dl_links = soup.find(class_="clr")
    print(dl_links)

def gogo_finder(name):
    try:
        # result = search(name+' gogoanime '+str(ep),num_results=10)
        result = search(name+' gogoanime.pe',num_results=10)
    except:
        print('NO internet')
    for link in result:
        l = link.split('/')
        if 'gogoanime.pe' == l[-2] and l[-1].split('-')[-3] == 'dub':
            print(link)
            break



    # for link in result:
    #     link = link.split('/')
    #     print(link)

gogo_finder('death note')


# print(
# check_anime_spell('death nite'))

    # gogoresult = search(name + ' dub gogoanime episode '+str(ep), num_results=5)
    # for i in gogoresult:
    #     if 'gogoanime.ai' in i:
    #         print(i)
    #         result = i
    #         break
    # return result