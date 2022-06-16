from random import choice

def get_knikkers():
    knikkers = [
        'geel', 'geel', 'geel',
        'blauw', 'blauw', 'blauw', 'blauw', 'blauw',
        'rood', 'rood', 'rood', 'rood'
    ]
    return knikkers

def trek_knikker():
    knikkers = get_knikkers()
    geel_getrokken = 0
    for x in range(3):
        gekozen = choice(knikkers)
        knikkers.remove(gekozen)
        if gekozen == 'geel':
            geel_getrokken += 1
    if geel_getrokken == 3:
        return True
    return False

def main():
    iteraties = 1000000
    aantal_waar = 0
    for x in range(iteraties):
        if trek_knikker():
            aantal_waar +=1
    print('De kans = {}%'.format(aantal_waar/iteraties))

if __name__ == "__main__":
    main()