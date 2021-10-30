import pyautogui
# import datetime

def locate(img):
    while True:
        click = pyautogui.locateCenterOnScreen(img)
        pyautogui.sleep(0.3)
        # print(datetime.datetime.now().time())
        if not click == None:
            pyautogui.click(click)
            break

location = r'C:\Users\saket\Documents\GitHub\Pyhton\1Automate Downloading'

while True:
    locate(location + r'\click.png')
    locate(location + r'\click to generate link.png')
    locate(location + r'\get download link.png')
    locate(location + r'\direct_download.png')
    locate(location + r'\download_anyway.png')
