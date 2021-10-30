from googlesearch import search

def available_on_movies_verse(name):
    result = search(name+' mkvking', num_results=10)
    for i in result:
        if 'mkvking.me' in i:
            print(name+' found on mkvking.me')
            return i

quality = '480'

link = available_on_movies_verse(input('Movie Name: '))

import requests
page = requests.get(link)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

downloads = soup.find( class_ = 'gmr-download-wrap clearfix')
buttons = downloads.find_all(href=True)
# print(buttons)
for i in buttons:
    if 'GoogleDrive '+quality in str(i):
        print('find gdrive 480p link')
        gdrive = str(i).split('href="')[1].split('" ')[0]
        break
# print(gdrive)

import webbrowser
webbrowser.open(gdrive)

import pyautogui
# while True:
#     not_a_robot = pyautogui.locateOnScreen('not_a_robot.png')
#     if not not_a_robot == None:
#         pyautogui.click(not_a_robot)
#         break

# while True:
#     mkv_get_link = pyautogui.locateOnScreen('mkv_get_link.png')
#     if not mkv_get_link == None:
#         pyautogui.click(mkv_get_link)
#         break

# while True:
#     mkv_download = pyautogui.locateOnScreen('mkv_download.png')
#     if not mkv_download == None:
#         pyautogui.click(mkv_download)
#         break


while True:
    drivefire_download = pyautogui.locateOnScreen('drivefire_download.png')
    if not drivefire_download == None:
        pyautogui.click(drivefire_download)
        break


while True:
    mkv_download = pyautogui.locateOnScreen('mkv_download.png')
    if not mkv_download == None:
        pyautogui.click(mkv_download)
        break

# page = requests.get(gdrive)
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)