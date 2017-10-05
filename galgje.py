print('opstarten...')
import random
WoordLijst = ['letter', 'galgje', 'woord', 'computer', 'toetsenbord', 'programma', 'camera', 'scherm', 'galg', 'goed', 'stoel', 'spel', 'ananas']
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
levens = 10

def checkWin():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('? ', end='')
        print('')
        print('" ' * len(GeheimWoord))

renderWoord()

while True:
    letter = input('raad een letter of typ het woord  ')
    if len(letter) == 1:
        if letter in GeradenLetters:
            print('Die letter had je al geraden...')
            renderWoord()
        else:
            GeradenLetters += letter
            if letter in GeheimWoord:
                print('Goed. Die letter zit wel in het woord')
                renderWoord()
                if checkWin():
                    print('Je hebt alle letters geraden, en dus gewonnen!')
                    print('Het woord was: ' + GeheimWoord)
                    break
            else:
                print('Fout. Die letter zit niet in het woord')
                print('-1')
                levens -= 1
                renderWoord()
    elif letter == GeheimWoord:
        print('Je hebt het woord geraden, en dus gewonnen!')
        break
    else:
        print('Fout woord!')
        print('-2')
        levens -= 2
        renderWoord()
    if levens <= 0:
        print('Je hebt verloren! Het woord was ' + GeheimWoord)
        break
    print('Je hebt nog', levens, 'levens over.')
print('Afsluiten...')
