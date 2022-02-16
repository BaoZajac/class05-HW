'''
Prosty system księgowy/magazyn

Napisz program (accountant.py), który będzie rejestrował operacje na koncie firmy i stan magazynu.
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
??  Jeśli użytkownik wprowadzi inną akcję, program powinien zwrócić błąd i zakończyć działanie.

    saldo: program pobiera dwie linie: zmiana na koncie firmy wyrażona w groszach (int) (może być ujemna) oraz komentarz do zmiany (str)

    zakup: program pobiera trzy linie:
            identyfikator produktu (str),
            cena jednostkowa (int)
            i liczba sztuk (int).
        Program odejmuje z salda cenę jednostkową pomnożoną przez liczbę sztuk.
        Jeśli saldo po zmianie jest ujemne, cena jest ujemna bądź liczba sztuk jest mniejsza od zero program zwraca błąd.
        Program podnosi stan magazynowy zakupionego towaru

    sprzedaż: program pobiera trzy linie: identyfikator produktu (str), cena jednostkowa (int), liczba sztuk (int). Program dodaje do salda cenę jednostkową pomnożoną razy liczbę sztuk. Jeśli na magazynie nie ma wystarczającej liczby sztuk, cena jest ujemna bądź liczba sztuk sprzedanych jest mniejsza od zero program zwraca błąd. Program obniża stan magazynowy zakupionego towaru.

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

wejscie = sys.argv[1]
saldo = 0

# WCZYTYWANIE Z PLIKU in.txt
# pytanie: czy wprowadzane dane są w groszach czy w złotych? poniższa pętla przelicza z groszy na złote
while True:
    plik_in_txt = input()
    if plik_in_txt == "saldo":
        saldo += int(input()) / 100
        nazwa_saldo = input()
        print(f"Obecne saldo to: {saldo}zł ze względu na: {nazwa_saldo}")
    elif plik_in_txt == "zakup":
        nazwa_zakup = input()
        cena_szt_zakup = int(input()) / 100
        ilosc_zakup = int(input())
        saldo -= cena_szt_zakup * ilosc_zakup
        print(f"Obecne saldo to: {saldo}zł, bo kupiono {nazwa_zakup}, w ilości: {ilosc_zakup}, po {cena_szt_zakup} za sztuke")
    elif plik_in_txt == "sprzedaz":
        nazwa_sprzedaz = input()
        cena_szt_sprzedaz = int(input()) / 100
        ilosc_sprzedaz = int(input())
        saldo += cena_szt_sprzedaz * ilosc_sprzedaz
        print(f"Obecne saldo to: {saldo}zł, bo sprzedano {nazwa_sprzedaz} w ilosci: {ilosc_sprzedaz}, po {cena_szt_sprzedaz} za sztuke")
    elif plik_in_txt == "stop":
        break

print(f"Saldo po wczytaniu danych poczatkowych z in.txt to: {saldo}zł")
print()


if wejscie == "saldo":
    zmiana_na_koncie = int(sys.argv[2]) / 100  # wyrażone w groszach!
    komentarz = sys.argv[3]
    saldo += zmiana_na_koncie
    print(f"Obecne saldo to: {saldo}zł, bo {komentarz}")
elif wejscie == "zakup":
    identyfikator_produktu = sys.argv[2]
    cena_jednostkowa = int(sys.argv[3]) / 100
    liczba_sztuk = int(sys.argv[4])
    if (saldo < 0) or (cena_jednostkowa < 0) or (liczba_sztuk < 0):
        print("Błąd w: cena jednostka lub liczba sztuk")
    # TODO: Poprawić błąd z tym, że saldo nie może być ujemne
    else:
        saldo -= cena_jednostkowa * liczba_sztuk
        print(f"Obecne saldo to: {saldo}, bo kupiono {identyfikator_produktu} w liczbie {liczba_sztuk} sztuk, po {cena_jednostkowa}zł za sztukę")
    #TODO: Program podnosi stan magazynowy zakupionego towaru
# elif wejscie == "sprzedaz":
#     print("sprzedaz")
# # else:
# #     print("Błąd")
# else:


