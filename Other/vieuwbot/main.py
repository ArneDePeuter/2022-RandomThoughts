import webbrowser
import os
import time
vieuws = 1361
link = "https://www.youtube.com/watch?v=es-GzpZcxrc"

aantalperkeer = 20
herhaling = 10

for x in range(herhaling):
    for y in range(aantalperkeer):
        webbrowser.open(link)
        time.sleep(0.45)
    time.sleep(aantalperkeer*2/3)
    os.system("taskkill /im chrome.exe /f")