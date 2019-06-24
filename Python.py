import subprocess

bazaTowary=[{'nazwa': 'koszulka','cena':25.50},{'nazwa': 'spodnie','cena':100.00}]
bazaMagazyn = [{'nazwa': 'koszulka_25.50','ilosc': 20},{'nazwa': 'spodnie_100.00','ilosc': 10}] 
bazaKlienci = []
bazTransakcje = []

klient1={'imieNazwisko':'Robert Makowaki','idKlienta':25111}
klient2={'imieNazwisko':'Roman Nijaki','idKlienta':26255}


towar1 = {'nazwa': 'koszula','cena':55.55}
transakcja1 = {'id':1, 'klient':'Robert Nowak', 'towary':['koszulka','spodnie'], 'ceny': [25.50, 100.00]}

def dodajK(bazaK, klient):
    if klient in bazaK:
        print('Klient: '+klient['imieNazwisko'] + ' ' + klient['idKlienta']+' już istnieje')
    else:
        bazaK.append(klient)

dodajK(bazaKlienci, klient1)
dodajK(bazaKlienci, klient2)

def dodajT(bazaT, bazaM, towar, ile):
    if towar in bazaT:
        print(towar['nazwa'] + ' ' + towar['cena']+' już istnieje')
    else:
        bazaT.append(towar)
        bazaM.append({'nazwa': towar['nazwa']+'_'+str(towar['cena']), 'ilosc': ile})

dodajT(bazaTowary, bazaMagazyn, {'nazwa':'koszula', 'cena': 45.50}, 113)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'spodenki', 'cena': 55.55}, 13)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'skarpetyMeskie40', 'cena': 8.35}, 25)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'skarpetyDamski35', 'cena': 7.55}, 33)



def pensjaZaMala(baza, minimum):
    ponizejMinimum = []
    for osoba in baza:
        if osoba['pensja'] < minimum:
            ponizejMinimum.append(osoba)
    return ponizejMinimum

def dodajTowar():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ilość w magazynie: '))
    dodajT(bazaTowary, bazaMagazyn, {'nazwa': nazwa, 'cena': cena}, ile)

def dodajKlienta():
    imieNazwisko = str(input('Imie i nazwisko klienta: '))
    idKlienta = int(input('Ilość w magazynie: '))
    dodajK(bazaKlienci,{'imieNazwisko': imieNazwisko, 'idKlienta': idKlienta})

def usunKlienta():
    imieNazwisko = str(input('Podaj imie i nazwisko: '))
    id = int(input('Podaj id klienta: '))
    szukanyKlient = {'imieNazwisko': imieNazwisko, 'idKlienta': id}
    if szukanyKlient in bazaKlienci:
        bazaKlienci.remove(szukanyKlient)
        print('Usunięto klienta: '+szukanyKlient['imieNazwisko']+' (id='+szukanyKlient['idKlienta']+')')
    else:
        print('Nie usunięto, w bazie nie ma takiego klienta.')
    for klient in bazaKlienci:
        if klient['idKlienta'] == id:
            print('W bazie istnije klient o id= '+str(id))
            print('Jest to: '+klient['imieNazwisko'])
            takNie = str(input('Usunąć tego klienta Y/N: '))
            if takNie=='Y' or takNie=='y':
                bazaKlienci.remove(klient)
                print('Usunięto klienta z bazy.')


def raporty():
    print(bazaKlienci)
    print(bazaTowary)
    print(bazaMagazyn)
    print(bazTransakcje)

def raportBaza(baza):
    print(baza)

tak=True
subprocess.call("cls", shell = True)
while tak == True :
    print(' MENU: ')
    print('1 - Towary')
    print('   11 - dodaj towar')
    print('   12 - usuń towar')
    print('   13 - modyfikuj towar')
    print('2 - Klienci')
    print('   21 - dodaj klienta')
    print('   22 - usuń klienta')
    print('   23 - modyfikuj klienta')
    print('9 - Raporty')
    print('0 - Koniec')
 #   print('   91 - lista towarów')
 #   print('   92 - lista klientów')
 #   print('   93 - lista transakcji')
 #   print('   94 - stan magazynu')

    wybor = int(input('Twój wybór: '))
    if wybor==11: dodajTowar()
    if wybor==12: dodajTowar()
    if wybor==21: dodajKlienta()
    if wybor==22: usunKlienta()
    if wybor==9: raporty()
    if wybor==1: raportBaza(bazaTowary)
    if wybor==2: raportBaza(bazaKlienci)
    if wybor==3: raportBaza(bazaMagazyn)
    if wybor==0: tak=False