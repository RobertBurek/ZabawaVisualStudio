import subprocess
import datetime

bazaTowary = []
bazaMagazyn = []
bazaKlienci = []
bazaTransakcji = []


# TWORZENIE PRZYKŁADOWYCH DANYCH W BAZACH

def dodajTr(bazaTr, transakcja):
    if transakcja in bazaTr:
        print('Taka transakcja już istnieje')
    else:
        bazaTr.append(transakcja)


dodajTr(bazaTransakcji, {'id': 1, 'idKlienta': 25100, 'data': '24.06.2019 22:16:43',
                         'towar': 'koszulka', 'cena': 25.5, 'ile': 4, 'status': 'zrealizowane'})
dodajTr(bazaTransakcji, {'id': 2, 'idKlienta': 25111, 'data': '25.06.2019 21:17:23',
                         'towar': 'spodnie', 'cena': 100.0, 'ile': 3, 'status': 'zrealizowane'})
dodajTr(bazaTransakcji, {'id': 3, 'idKlienta': 25100, 'data': '26.06.2019 13:23:45',
                         'towar': 'spodnie', 'cena': 100.0, 'ile': 2, 'status': 'zrealizowane'})
dodajTr(bazaTransakcji, {'id': 4, 'idKlienta': 25111, 'data': '27.06.2019 12:12:12',
                         'towar': 'koszulka', 'cena': 25.5, 'ile': 1, 'status': 'zrealizowane'})


def dodajK(bazaK, klient):
    if klient in bazaK:
        print('Klient: '+klient['imieNazwisko'] +
              ' ' + klient['idKlienta']+' już istnieje')
    else:
        bazaK.append(klient)


dodajK(bazaKlienci, {'imieNazwisko': 'Robert Makowiak', 'idKlienta': 25111})
dodajK(bazaKlienci, {'imieNazwisko': 'Roman Nijaki', 'idKlienta': 26255})
dodajK(bazaKlienci, {'imieNazwisko': 'Anna Nowakowska', 'idKlienta': 25100})


def dodajT(bazaT, bazaM, towar, ile):
    if towar in bazaT:
        print(towar['nazwa'] + ' ' + towar['cena']+' już istnieje')
    else:
        bazaT.append(towar)
        bazaM.append({'nazwa': towar['nazwa'] +
                      '_'+str(towar['cena']), 'ilosc': ile})


dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'koszulka', 'cena': 25.50}, 22)
dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'spodnie', 'cena': 100.00}, 16)
dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'koszula', 'cena': 45.50}, 113)
dodajT(bazaTowary, bazaMagazyn, {'nazwa': 'spodenki', 'cena': 55.55}, 13)
dodajT(bazaTowary, bazaMagazyn, {
       'nazwa': 'skarpetyMeskie40', 'cena': 8.35}, 25)
dodajT(bazaTowary, bazaMagazyn, {
       'nazwa': 'skarpetyDamski35', 'cena': 7.55}, 33)


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
        print('Usunięto towar: ' +
              szukanyTowar['nazwa'] + ' (cena=' + str(szukanyTowar['cena'])+')')
        bazaMagazyn.remove(bazaMagazyn[index])
    else:
        print('Nie ma takiego towaru: ' +
              szukanyTowar['nazwa'] + ' (cena=' + str(szukanyTowar['cena'])+')')


#  KLIENCI
def dodajKlienta():
    tak = True
    imieNazwisko = str(input('Imie i nazwisko klienta: '))
    while tak == True:
        idKlienta = int(input('Unikalny numer id: '))
        for klient in bazaKlienci:
            if klient['idKlienta'] != idKlienta:
                tak = False
            else:
                tak = True
                print('Taki numer id istnieje !!!')
                break
    dodajK(bazaKlienci, {'imieNazwisko': imieNazwisko, 'idKlienta': idKlienta})


def usunKlienta():
    imieNazwisko = str(input('Podaj imie i nazwisko: '))
    id = int(input('Podaj id klienta: '))
    szukanyKlient = {'imieNazwisko': imieNazwisko, 'idKlienta': id}
    if szukanyKlient in bazaKlienci:
        bazaKlienci.remove(szukanyKlient)
        print('Usunięto klienta: ' +
              szukanyKlient['imieNazwisko']+' (id='+str(szukanyKlient['idKlienta'])+')')
    else:
        print('Nie usunięto, w bazie nie ma takiego klienta.')
    for klient in bazaKlienci:
        if klient['idKlienta'] == id:
            print('W bazie istnije klient o id= '+str(id))
            print('Jest to: '+klient['imieNazwisko'])
            takNie = str(input('Usunąć tego klienta? Y/N: '))
            if takNie == 'Y' or takNie == 'y':
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
        print('Zmodyfikowano dane klienta: ' + noweImieNazwisko +
              ' (id='+str(szukanyKlient['idKlienta'])+')')
    else:
        print('Nie zmodyfikowano, w bazie nie ma takiego klienta.')
        for klient in bazaKlienci:
            if klient['idKlienta'] == id:
                print('W bazie istnije klient o id= '+str(id))
                print('Jest to: '+klient['imieNazwisko'])
                takNie = str(
                    input('Czy temu klientowi zmodyfikować dane? Y/N: '))
                if takNie == 'Y' or takNie == 'y':
                    index = bazaKlienci.index(klient)
                    bazaKlienci[index]['imieNazwisko'] = noweImieNazwisko
                    print('Zmodyfikowano dane klienta: '+noweImieNazwisko +
                          ' (id='+str(szukanyKlient['idKlienta'])+')')


def wyszukajKlientaId():
    idKlienta = int(input('Podaj id klienta: '))
    for i in range(len(bazaKlienci)):
        if bazaKlienci[i]['idKlienta'] == idKlienta:
            klient = bazaKlienci[i]
            tak = True
            break
        else:
            tak = False
    if tak == True:
        print(klient)
    else:
        print('Brak klienta w bazie o takim id.')


#  MAGAZYN
def dodajDoMagazynu():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ile dodać do magazynu: '))
    szukanyTowar = {'nazwa': nazwa, 'cena': cena}
    if szukanyTowar in bazaTowary:
        index = bazaTowary.index(szukanyTowar)
        if ile >= 0:
            bazaMagazyn[index]['ilosc'] += ile
            print('Stan magazynowy po zmianie: ' +
                  str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
    else:
        print('Nie ma takiego towaru w magazynie.')


def usunZMagazynu():
    nazwa = str(input('Nazwa towaru: '))
    cena = float(input('Cena towaru: '))
    ile = int(input('Ile usunąć z magazynu: '))
    szukanyTowar = {'nazwa': nazwa, 'cena': cena}
    if szukanyTowar in bazaTowary:
        index = bazaTowary.index(szukanyTowar)
        if ile >= 0 and bazaMagazyn[index]['ilosc'] >= ile:
            bazaMagazyn[index]['ilosc'] -= ile
            print('Stan magazynowy po zmianie: ' +
                  str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
        else:
            if bazaMagazyn[index]['ilosc'] < ile:
                print('Nie ma tyle w magazynie.')
                takNie = str(input('Czy mam wyzerować stan magazynowy? Y/N: '))
                if takNie == 'Y' or takNie == 'y':
                    bazaMagazyn[index]['ilosc'] = 0
                    print('Stan magazynowy po zmianie: ' +
                          str(bazaMagazyn[index]['ilosc'])+'  - towar: '+szukanyTowar['nazwa'])
    else:
        print('Nie ma takiego towaru w magazynie.')


#  TRANSAKCJE
def dodajTransakcje():
    idKlienta = int(input('Podaj id klienta: '))
    for i in range(len(bazaKlienci)):
        if bazaKlienci[i]['idKlienta'] == idKlienta:
            klient = bazaKlienci[i]
            print(klient)
            jestKlient = True
            break
        else:
            jestKlient = False
    if jestKlient == False:
        print('Nie ma klienta o takim id.')
        imieNazwisko = str(input('Podaj imie i nazwisko: '))
        for j in range(len(bazaKlienci)):
            if bazaKlienci[j]['imieNazwisko'] == imieNazwisko:
                klient = bazaKlienci[j]
                jestKlient = True
                break
            else:
                jestKlient = False
    if jestKlient == False:
        print('Nie ma klienta o takim danych.')
        print('Wyszukaj klienta na liście - opcja (2).')
    else:
        takNie = str(input('Dotyczy klienta: ' +
                           klient['imieNazwisko']+' ('+str(klient['idKlienta'])+')? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            tak = True
            while tak == True:
                nazwa = str(input('Nazwa towaru: '))
                cena = float(input('Cena towaru: '))
                stanMagazynu = -1
                for index in range(len(bazaMagazyn)):
                    if bazaMagazyn[index]['nazwa'] == nazwa+'_'+str(cena):
                        stanMagazynu = bazaMagazyn[index]['ilosc']
                        tak = False
                        break
                if stanMagazynu == -1:
                    print('Nie ma takiego towaru w sprzedaży.')
                    takNie = str(input('Chcesz spróbować jeszcze raz? Y/N: '))
                    if takNie == 'Y' or takNie == 'y':
                        tak = True
                    else:
                        tak = False
            ile = int(input('Ile sztuk: '))
            if stanMagazynu < ile:
                print('Niewystarczająca ilość w magazynie.')
                print('Status: "czeka na dostawę"')
                status = 'czeka na dostawę'
            if stanMagazynu >= ile:
                status = 'zrealizowane'
                stanMagazynu -= ile
                bazaMagazyn[index]['ilosc'] = stanMagazynu
 #           dataCzas = str(input('Data transakcji DD-MM-RRRR: '))
            dataCzas = str(
                datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
            id = bazaTransakcji[len(bazaTransakcji)-1]['id']+1
            transakcja = {'id': id, 'idKlienta': klient['idKlienta'], 'data': dataCzas,
                          'towar': nazwa, 'cena': cena, 'ile': ile, 'status': status}
            dodajTr(bazaTransakcji, transakcja)
            print('Dodano transakcję nr='+str(id)+' ze statusem ('+status+')')


def transakcjeKlienta():
    idKlienta = int(input('Podaj id klienta: '))
    for i in range(len(bazaTransakcji)):
        if bazaTransakcji[i]['idKlienta'] == idKlienta:
            print(bazaTransakcji[i])


def transakcjeKlientaId(id):
    licznik = 0
    for i in range(len(bazaTransakcji)):
        if bazaTransakcji[i]['idKlienta'] == id:
            print(bazaTransakcji[i])
            licznik += 1
    if licznik == 0:
        print('Nie ma klienta lub klient nie ma transakcji.')


def usunTransakcje():
    idKlienta = int(input('Podaj id klienta: '))
    transakcjeKlientaId(idKlienta)
    idTransakcji = int(input('Podaj id transakcji: '))
    for index in range(len(bazaTransakcji)):
        if bazaTransakcji[index]['id'] == idTransakcji:
            print('Transakcja przed zmianą:')
            print(bazaTransakcji[index])
            jestTransakcja = True
            break
        else:
            jestTransakcja = False
    if jestTransakcja == False:
        print('Nie ma transakcji o takim id.')
    else:
        takNie = str(input('Czy jesteś pewien? Y/N: '))
        if takNie == 'Y' or takNie == 'y':
            for i in range(len(bazaMagazyn)):
                if bazaMagazyn[i]['nazwa'] == bazaTransakcji[index]['towar']+'_'+str(bazaTransakcji[index]['cena']):
                    print('Stan magazynowy przed zmianą: ' +
                          str(bazaMagazyn[i]['ilosc']))
                    bazaMagazyn[i]['ilosc'] += bazaTransakcji[index]['ile']
                break
            status = 'reklamacja '+str(bazaTransakcji[index]['ile'])+' szt.'
            bazaTransakcji[index]['ile'] = 0
            bazaTransakcji[index]['status'] = status
            print('Transakcja po zmianie:')
            print(bazaTransakcji[index])
            print('Stan magazynowy po zmianą: '+str(bazaMagazyn[i]['ilosc']))


def wypiszBaze(baza):
    print('-----------------------------------------------')
    for i in range(len(baza)):
        print(str(i+1)+') '+str(baza[i]))
    print('-----------------------------------------------')


def raporty():
    wypiszBaze(bazaKlienci)
    wypiszBaze(bazaTowary)
    wypiszBaze(bazaMagazyn)
    wypiszBaze(bazaTransakcji)


def raportBaza(baza):
    wypiszBaze(baza)


tak = True
subprocess.call("cls", shell=True)
while tak == True:
    print(' MENU: ')
    print('1 - Towary (lista)')
    print('   11 - dodaj towar')
    print('   12 - usuń towar')
    print('2 - Klienci (lista)')
    print('   21 - dodaj klienta')
    print('   22 - usuń klienta')
    print('   23 - modyfikuj klienta')
    print('   24 - wyszukaj po id')
    print('3 - Magazyn (stan)')
    print('   31 - dodaj do magazynu')
    print('   32 - usuń z magazynu')
    print('4 - Transakcje (lista)')
    print('   41 - dodaj transakcje')
    print('   42 - usuń transakcje')
    print('   43 - transakcje klienta')
    print('9 - Raporty (wszystkie)')
    print('0 - Koniec')
    wybor = int(input('Twój wybór: '))
    if wybor == 11:
        dodajTowar()
    if wybor == 12:
        usunTowar()
    if wybor == 21:
        dodajKlienta()
    if wybor == 22:
        usunKlienta()
    if wybor == 23:
        modyfikujKlienta()
    if wybor == 24:
        wyszukajKlientaId()
    if wybor == 31:
        dodajDoMagazynu()
    if wybor == 32:
        usunZMagazynu()
    if wybor == 41:
        dodajTransakcje()
    if wybor == 42:
        usunTransakcje()
    if wybor == 43:
        transakcjeKlienta()
    if wybor == 9:
        raporty()
    if wybor == 1:
        raportBaza(bazaTowary)
    if wybor == 2:
        raportBaza(bazaKlienci)
    if wybor == 3:
        raportBaza(bazaMagazyn)
    if wybor == 4:
        raportBaza(bazaTransakcji)
    if wybor == 0:
        tak = False
