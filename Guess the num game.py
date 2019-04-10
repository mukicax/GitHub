# Number guessing game
import random
ime = input('Unesite vase ime: ')
print('Zdravo gosn ' + str(ime) + ' pogodite koji broj sam zamislio od 1 do 20!') 
tajniBroj = random.randint(1,20)

for brojPokusaja in range (1,7):
    print('Pokusaj da pogodis broj: ')
    try:
        a = int(input())
    except:
        print('Motherfucker')
    if a > tajniBroj:
        print('Prevelik broj ')
    elif a < tajniBroj:
        print('Premali broj ')
    else:
        break
if a == tajniBroj:
    print('Vau svaka cast pogodili ste iz ' + str(brojPokusaja) + ' pokusaja, cestitamo!')
else:
    print('Vise srece drugi put, zamislio sam broj ' + str(tajniBroj) + '.')
    
