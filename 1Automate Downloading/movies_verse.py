from googlesearch import search

def available_on_movies_verse(name):
    result = search(name+' moviesverse', num_results=10)
    for i in result:
        if 'moviesverse.org.in/download' in i:
            print(name+' found on moviesverse')
            return i
    # print('nope not available!')

while True:
    x = input('enter your movie: ')
    link = available_on_movies_verse(x)

    import requests
    from bs4 import BeautifulSoup
    # searching for the page link
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    buttons = soup.find( class_ = "single_post" )
    button_lins = buttons.find_all(href=True)

    links = []
    for i in button_lins:
        if r'links.mflixblog.xyz' in str(i):
            # print(str(i).split('href="')[1].split('" ')[0])
            links.append(str(i).split('href="')[1].split('" ')[0])
    # print(links)

    gdrivelink = requests.get(links[0])
    soup_ = BeautifulSoup(gdrivelink.content, 'html.parser')
    gdrive=soup_.find(class_='maxbutton-1 maxbutton maxbutton-fast-server-gdrive')#.split('href=')#[1].split(['" '])[0]
    gdrive = str(gdrive).split('href="')[1].split('" ')[0]
    # print(type(gdrive), gdrive)
    print(gdrive)
    import webbrowser
    webbrowser.open(gdrive)
    
    ### here comes the clicking part CLICKEY CLICKEY CLICK

    import pyautogui
    def locate(img):
        while True:
            pyautogui.sleep(0.3)
            click = pyautogui.locateCenterOnScreen(img)
            if not click == None:
                pyautogui.click(click)
                break

    location = r'C:\Users\saket\Documents\GitHub\Pyhton\1Automate Downloading\New folder'

    locate(location + r'\click.png')
    locate(location + r'\click to generate link.png')
    locate(location + r'\get download link.png')
    locate(location + r'\direct_download.png')
    locate(location + r'\download_anyway.png')