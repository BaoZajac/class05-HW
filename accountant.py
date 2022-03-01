'''
Prosty system księgowy/magazyn

Napisz program (accountant.py), który będzie rejestrował historia_operacji na koncie firmy i stan magazynu.
Program jest wywoływany w następujący sposób:
a) python accountant.py saldo <int wartosc> <str komentarz>
b) python accountant.py sprzedaż <str identyfikator produktu> <int cena> <int liczba sprzedanych>
c) python accountant.py zakup <str identyfikator produktu> <int cena> <int liczba zakupionych>
d) python accountant.py konto
e) python accountant.py magazyn <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
f) python accountant.py przegląd

Działanie programu będzie zależne od podanych argumentów
Niezależnie od trybu program zawsze będzie działał w następujący sposób
I. Program pobierze rodzaj akcji (ciąg znaków).
    Dozwolone akcje to "saldo", zakup", "sprzedaż".
    Jeśli użytkownik wprowadzi inną akcję, program powinien zwrócić błąd i zakończyć działanie.

    saldo: program pobiera dwie linie: zmiana na koncie firmy wyrażona w groszach (int) (może być ujemna) oraz komentarz do zmiany (str)

    zakup: program pobiera trzy linie:
            identyfikator produktu (str),
            cena jednostkowa (int)
            i liczba sztuk (int).
        Program odejmuje z salda cenę jednostkową pomnożoną przez liczbę sztuk.
        Jeśli saldo po zmianie jest ujemne, cena jest ujemna bądź liczba sztuk jest mniejsza od zero program zwraca błąd.
        Program podnosi stan magazynowy zakupionego towaru

    sprzedaż: program pobiera trzy linie: identyfikator produktu (str), cena jednostkowa (int), liczba sztuk (int).
        Program dodaje do salda cenę jednostkową pomnożoną razy liczbę sztuk.
        Jeśli na magazynie nie ma wystarczającej liczby sztuk, cena jest ujemna bądź liczba sztuk sprzedanych jest mniejsza od zero program zwraca błąd.
        Program obniża stan magazynowy zakupionego towaru.

    stop: program przechodzi do kroku IV

II. Program zapamiętuje każdą wprowadzoną linię
III. Program wraca do kroku I
IV. W zależności od wywołania:
    a) b) c) program dodaje do historii podane argumenty tak, jakby miały być wprowadzone przez standardowe wejście, przechodzi do kroku V
    d) program wypisuje na standardowe wyjście stan konta po wszystkich akcjach, kończy działanie
    e) program wypisuje stany magazynowe dla podanych produktów, w formacie: <id produktu>: <stan> w nowych liniach i kończy działanie:
    f) Program wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie)
V. Program wypisuje wszystkie podane parametry w formie identycznej, w jakiej je pobrał.
'''

import sys

historia_operacji = []
wejscie = sys.argv[1]
saldo = 0
magazyn = {}


# poniższa pętla wczytuje dane z zewnętrznego pliku z historią operacji i zapisuje je do historii operacji wewnątrz programu
while True:
    plik_in_txt = input()
    if plik_in_txt == "saldo":
        zmiana_na_koncie = input()
        nazwa_operacji = input()
        obecna_lista = (plik_in_txt, zmiana_na_koncie, nazwa_operacji)
        historia_operacji.append(obecna_lista)
    elif plik_in_txt == "zakup":
        nazwa_zakup = input()
        cena_szt_zakup = input()
        ilosc_zakup = input()
        obecna_lista = (plik_in_txt, nazwa_zakup, cena_szt_zakup, ilosc_zakup)
        historia_operacji.append(obecna_lista)
    elif plik_in_txt == "sprzedaz":
        nazwa_sprzedaz = input()
        cena_szt_sprzedaz = int(input())
        ilosc_sprzedaz = int(input())
        obecna_lista = (plik_in_txt, nazwa_sprzedaz, cena_szt_sprzedaz, ilosc_sprzedaz)
        historia_operacji.append(obecna_lista)
    elif plik_in_txt == "stop":
        break
    else:
        print("Błąd")
        break


# wczytanie danych wejsciowych uruchamiających program i zapisanie ich w historii operacji
if wejscie == "saldo":
    zmiana_na_koncie = sys.argv[2]
    nazwa_operacji = sys.argv[3]
    obecna_lista = (wejscie, zmiana_na_koncie, nazwa_operacji)
    historia_operacji.append(obecna_lista)
    historia_operacji.append(("stop",))
elif wejscie == "zakup" or wejscie == "sprzedaz":
    nazwa_zakup = sys.argv[2]
    cena_jednostkowa = sys.argv[3]
    liczba_sztuk = sys.argv[4]
    obecna_lista = (wejscie, nazwa_zakup, cena_jednostkowa, liczba_sztuk)
    historia_operacji.append(obecna_lista)
    historia_operacji.append(("stop",))


# przerobienie historii operacji na działania
for polecenie in historia_operacji:
    if polecenie[0] == "saldo":
        kwota = polecenie[1]
        saldo += int(kwota)
        if saldo < 0:
            print("Brak wystarczających środków na koncie do przeprowadzenia operacji")
            # saldo -= kwota      # to jest niepotrzebne, ale nie lubię zostawiać błędów
            break
    elif polecenie[0] == "zakup":
        kwota = int(polecenie[2]) * int(polecenie[3])
        saldo -= kwota
        if saldo < 0 or int(polecenie[2]) < 0 or int(polecenie[3]) < 0:
            # saldo += kwota      # to jest niepotrzebne, ale nie lubię zostawiać błędów
            print("Błąd")
            break
        przedmiot = polecenie[1]
        if not magazyn.get(przedmiot):
            magazyn[przedmiot] = 0
        magazyn[przedmiot] += int(polecenie[3])
    elif polecenie[0] == "sprzedaz":
        kwota = int(polecenie[2]) * int(polecenie[3])
        saldo += kwota
        liczba_sztuk_w_magazynie = int(magazyn[polecenie[1]])
        if liczba_sztuk_w_magazynie < int(polecenie[3]) or int(polecenie[2]) < 0 or int(polecenie[3]) < 0:
            # saldo -= kwota      # to jest niepotrzebne, ale nie lubię zostawiać błędów
            print("Błąd")
            break
        magazyn[polecenie[1]] -= int(polecenie[3])
    else:
        break


# wyniki ostateczne
if wejscie == "saldo" and saldo >= 0:
    for element in historia_operacji:
        for element2 in element:
            print(element2)
elif wejscie == "sprzedaz" and int(magazyn[sys.argv[2]]) >= 0 and int(sys.argv[3]) >= 0 and int(sys.argv[4]) >= 0:
    #TODO tu wchodzi błąd z ilością w magazynie - jest to związane z pętlą for w "sprzedaz", po niej wychodzi różny stan magazynu i tu wczytuje się tylko jedna opcja z dwóch
    for element in historia_operacji:
        for element2 in element:
            print(element2)
elif wejscie == "zakup" and saldo >= 0 and int(sys.argv[3]) >= 0 and int(sys.argv[4]) >= 0:
    for element in historia_operacji:
        for element2 in element:
            print(element2)
elif wejscie == "konto":
    print(saldo)
elif wejscie == "magazyn":
    for idx in sys.argv[2:]:
        if magazyn.get(idx):
            print(idx, ":", magazyn[idx])
        else:
            print(idx, ": brak w magazynie")
elif wejscie == "przeglad":
    for element in historia_operacji[int(sys.argv[2]):int(sys.argv[3])+1]:
        for element2 in element:
            print(element2)
    print("stop")
else:
    print("Błąd")


