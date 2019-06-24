import subprocess

bazaTowary=[]
bazaMagazyn = [] 
bazaKlienci = []
bazaTransakcji = []

transakcja1 = {'id':1, 'idKlienta': 25100, 'data': '19-06-2019', 'towar':'koszulka', 'ceny': 25.5, 'status': 'zrealizowane'}

def dodajK(bazaK, klient):
    if klient in bazaK:
        print('Klient: '+klient['imieNazwisko'] + ' ' + klient['idKlienta']+' już istnieje')
    else:
        bazaK.append(klient)

dodajK(bazaKlienci, {'imieNazwisko':'Robert Makowaki','idKlienta': 25111})
dodajK(bazaKlienci, {'imieNazwisko':'Roman Nijaki','idKlienta': 26255})
dodajK(bazaKlienci, {'imieNazwisko':'Anna Nowakowska','idKlienta': 25100})

def dodajT(bazaT, bazaM, towar, ile):
    if towar in bazaT:
        print(towar['nazwa'] + ' ' + towar['cena']+' już istnieje')
    else:
        bazaT.append(towar)
        bazaM.append({'nazwa': towar['nazwa']+'_'+str(towar['cena']), 'ilosc': ile})

dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'koszulka','cena': 25.50}, 22)
dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'spodnie','cena': 100.00}, 16)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'koszula', 'cena': 45.50}, 113)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'spodenki', 'cena': 55.55}, 13)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'skarpetyMeskie40', 'cena': 8.35}, 25)
dodajT(bazaTowary, bazaMagazyn, {'nazwa':'skarpetyDamski35', 'cena': 7.55}, 33)


#  TOWARY
def dodajTowar():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ilość w magazynie: '))
    dodajT(bazaTowary, bazaMagazyn, {'nazwa': nazwa, 'cena': cena}, ile)

def usunTowar():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    szukanyTowar = {'nazwa': nazwa, 'cena': cena}
    if szukanyTowar in bazaTowary:
        index = bazaTowary.index(szukanyTowar)
        bazaTowary.remove(szukanyTowar)
        print('Usunięto towar: '+szukanyTowar['nazwa'] + ' (cena=' + str(szukanyTowar['cena'])+')')
        bazaMagazyn.remove(bazaMagazyn[index])
    else:
        print('Nie ma takiego towaru: '+szukanyTowar['nazwa'] + ' (cena=' + str(szukanyTowar['cena'])+')')

#  KLIENCI
def dodajKlienta():
    tak = True
    imieNazwisko = str(input('Imie i nazwisko klienta: '))
    while tak==True:
        idKlienta = int(input('Unikalny numer id: '))
        for klient in bazaKlienci:
            if klient['idKlienta']!=idKlienta:
                tak=False
            else:
                tak=True
                print('Taki numer id istnieje !!!')
                break
    dodajK(bazaKlienci,{'imieNazwisko': imieNazwisko, 'idKlienta': idKlienta})

def usunKlienta():
    imieNazwisko = str(input('Podaj imie i nazwisko: '))
    id = int(input('Podaj id klienta: '))
    szukanyKlient = {'imieNazwisko': imieNazwisko, 'idKlienta': id}
    if szukanyKlient in bazaKlienci:
        bazaKlienci.remove(szukanyKlient)
        print('Usunięto klienta: '+szukanyKlient['imieNazwisko']+' (id='+str(szukanyKlient['idKlienta'])+')')
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

def modyfikujKlienta():
    imieNazwisko = str(input('Podaj imie i nazwisko: '))
    id = int(input('Podaj id klienta: '))
    szukanyKlient = {'imieNazwisko': imieNazwisko, 'idKlienta': id}
    print('Id klienta zostaje bez zmian.')
    noweImieNazwisko = str(input('Podaj NOWE imie i nazwisko: '))
    if szukanyKlient in bazaKlienci:
        index = bazaKlienci.index(szukanyKlient)
        bazaKlienci[index]['imieNazwisko'] = noweImieNazwisko
        print('Zmodyfikowano dane klienta: ' + noweImieNazwisko + ' (id='+str(szukanyKlient['idKlienta'])+')')
    else:
        print('Nie zmodyfikowano, w bazie nie ma takiego klienta.')
        for klient in bazaKlienci:
            if klient['idKlienta'] == id:
                print('W bazie istnije klient o id= '+str(id))
                print('Jest to: '+klient['imieNazwisko'])
                takNie = str(input('Czy temu klientowi zmodyfikować dane Y/N: '))
                if takNie=='Y' or takNie=='y':
                    index = bazaKlienci.index(klient)
                    bazaKlienci[index]['imieNazwisko'] = noweImieNazwisko
                    print('Zmodyfikowano dane klienta: '+noweImieNazwisko+' (id='+str(szukanyKlient['idKlienta'])+')')

#  MAGAZYN
def dodajDoMagazynu():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ile dodać do magazynu: '))
    szukanyTowar = {'nazwa': nazwa, 'cena': cena}
    if szukanyTowar in bazaTowary:
        index = bazaTowary.index(szukanyTowar)
        if ile>=0:
            bazaMagazyn[index]['ilosc'] += ile
            print('Stan magazynowy po zmianie: '+str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
    else:
        print('Nie ma takiego towaru w magazynie.')

def usunZMagazynu():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ile usunąć z magazynu: '))
    szukanyTowar = {'nazwa': nazwa, 'cena': cena}
    if szukanyTowar in bazaTowary:
        index = bazaTowary.index(szukanyTowar)
        if ile>=0 and bazaMagazyn[index]['ilosc']>=ile:
            bazaMagazyn[index]['ilosc'] -= ile
            print('Stan magazynowy po zmianie: '+str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
        else:
            if bazaMagazyn[index]['ilosc'] < ile:
                print('Nie ma tyle w magazynie.')
                takNie = str(input('Czy mam wyzerować stan magazynowy Y/N: '))
                if takNie=='Y' or takNie=='y':
                    bazaMagazyn[index]['ilosc'] = 0
                    print('Stan magazynowy po zmianie: '+str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
    else:
        print('Nie ma takiego towaru w magazynie.')


def wypiszBaze(baza):
    print('-----------------------------------------------')
    for i in range(len(baza)):
        print(baza[i])
    print('-----------------------------------------------')    

def raporty():
    wypiszBaze(bazaKlienci)
    wypiszBaze(bazaTowary)
    wypiszBaze(bazaMagazyn)
    wypiszBaze(bazaTransakcji)

def raportBaza(baza):
    wypiszBaze(baza)

tak=True
subprocess.call("cls", shell = True)
while tak == True :
    print(' MENU: ')
    print('1 - Towary (lista)')
    print('   11 - dodaj towar')
    print('   12 - usuń towar')
    print('2 - Klienci (lista)')
    print('   21 - dodaj klienta')
    print('   22 - usuń klienta')
    print('   23 - modyfikuj klienta')
    print('3 - Magazyn (stan)')
    print('   31 - dodaj do magazynu')
    print('   32 - usuń z magazynu')
    print('4 - Transakcje (lista)')
    print('   41 - dodaj transakcje')
    print('   42 - usuń transakcje')
    print('9 - Raporty')
    print('0 - Koniec')
    wybor = int(input('Twój wybór: '))
    if wybor==11: dodajTowar()
    if wybor==12: usunTowar()
    if wybor==21: dodajKlienta()
    if wybor==22: usunKlienta()
    if wybor==23: modyfikujKlienta()
    if wybor==31: dodajDoMagazynu()
    if wybor==32: usunZMagazynu()
    if wybor==9: raporty()
    if wybor==1: raportBaza(bazaTowary)
    if wybor==2: raportBaza(bazaKlienci)
    if wybor==3: raportBaza(bazaMagazyn)
    if wybor==0: tak=False