##F0003b: Bővítsd az előző programot úgy, hogy a kiírás előtt kérdezze meg a születési évedet és a csillagjegyedet, és az előző feladatban megadott mondat után ezt is közölje veled. Megoldás itt.

vezetéknév = input('Mi a vezetékneved?')
keresztnév = input('Mi a keresztneved?')
születésiév  = input('Melyik évben születtél?')
hónap = input('Melyik hónapban születtél?')
nap = input('Melyik nap születtél?')
hely = input('Hol születtél?')
csillagjegy = input('Melyik csillagjegyben születtél?')
print('A te neved ', vezetéknév, ' ', keresztnév, '.', sep='')
print('A te születési éved az ', születésiév, '.', sep='')
print('A te csillagjegyed az a ', csillagjegy, '.', sep='')
print('A te születési hónapod az ', hónap, '.', sep='')
print('A te születési napod az ', nap, '.', sep='')
print('A te születési városod az ', hely, '.', sep='')
print('Tehát te ', hely, ' ', 'születtél', ' ', 'ebben az évben', ' ', születésiév, ' ', 'és ebben a hónapban', ' ', hónap, ' ', 'és ezen a napon', ' ', nap, '.', sep='')
