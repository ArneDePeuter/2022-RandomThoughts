import urllib.request

link = "https://www.youtube.com/watch?v=es-GzpZcxrc"

aantal = True
while aantal:
    urllib.request.urlopen(link)
    print('opened {}'.format(link))
