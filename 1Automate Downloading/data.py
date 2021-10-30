# Full name:
# Language:
# Subtitle:
# Release Date:
# Size:
# Quality:



# data = str(soup).split('<ul>')[1].split('</ul>')[0].split('\n')
# print(''        ,                          data[1].split('</strong>')[1].split('</li>')[0])
# print(''        ,                          data[2].split('</strong>')[1].split('</li>')[0])
# print(''        ,                          data[3].split('</strong>')[1].split('</li>')[0])
# print(''        ,                          data[4].split('</strong>')[1].split('</li>')[0])
# print(''        ,                          data[5].split('</strong>')[1].split('</li>')[0])
# print(''        ,                          data[6].split('</strong>')[1].split('</li>')[0])



# import requests
# import webbrowser
# from bs4 import BeautifulSoup
# from googlesearch import search

# def available_on_movies_verse(name):
#     result = search(name+' moviesverse', num_results=10)
#     for i in result:
#         if 'moviesverse.org.in/download' in i:
#             print(name+' found on moviesverse')
#             return i
#     # print('nope not available!')

# x='Endgame'   #input('enter your movie: ')
# link = available_on_movies_verse(x)

# page = requests.get(link)
# soup = BeautifulSoup(page.content, 'html.parser')

# buttons = soup.find( class_ = "inline canwrap" )
# button_lins = buttons.find_all('a', href=True)
# print(len(button_lins))

# # if not link == None:
# #     webbrowser.open(link)
