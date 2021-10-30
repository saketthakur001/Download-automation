
from googlesearch import search
import requests
import webbrowser
from bs4 import BeautifulSoup

def anime_search():
    pass
    # result = search(name+" myanimelist", num_results=0)[0].split('/')
    # if result[-3] == "anime":
    #     anime = result[-1].replace('_', ' ')


def gogoanime(name, ep):
    print(name + ' dub gogoanime episode '+str(ep))
    gogoresult = search(name + ' dub gogoanime episode '+str(ep), num_results=5)
    for i in gogoresult:
        if 'gogoanime.ai' in i:
            print(i)
            result = i
            break
    return result
    # episode = gogoresult.split('/')[-1].split('-')[-1]
    # print("episode-"+ episode, gogoresult)

# print(anime, episode)
anime_link = gogoanime('death note', 5)
page = requests.get(anime_link)
page = BeautifulSoup(page.content, 'html.parser')
# button = str(page.find( class_ = "dowloads" )).split('href="')[1].split('" ')[0]
# download = requests.get(button)
# page = BeautifulSoup(download.content, 'html.parser')


###    request for the download button
# button = str(page.find( class_ = "dowloads" )).split('href="')[1].split('" ')[0]
# download = requests.get(button)
# page = BeautifulSoup(download.content, 'html.parser')
# button = str(page.find_all('a')).split('</a>')
# for i in button:
#     if '480P' in str(i):
#         button = str(i).split('href="')[1].split('">')[0]
#         print(button)