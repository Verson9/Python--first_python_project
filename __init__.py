# coding=utf-8
import sys


class produkt(object):
    def __init__(self, nazwa, cena, wykonanie):
        self.nazwa = nazwa
        self.cena = cena
        self.wykonanie = wykonanie

    def opisz(self):
        print ("Ten produkt to " + self.nazwa + " kosztuje :" + self.cena + '\n' + self.wykonanie)

    def wypiszdane(self):
        print ("Nazwa produktu: " + self.nazwa + ", \nCena produktu: " + self.cena)


def addchlep():
    typo = "Chleb"
    price = ""
    print("mamy na stanie chlep pszenny oraz zytni")
    print("jesli chcesz pszenny za 2zl (1) \njesli zytni za 2,50zl (2)")
    w = int(input())
    if w == 1:
        print("chlep przenny ")
        typo += " pszenny"
        price += "2zl"
    if w == 2:
        print("chleb zytni")
        typo = " żytni"
        price = "2,50zl"
    print("chcesz kupić daną rzecz?")
    print("Tak(1) Nie(2)")
    b = int(input())
    if b == 1:
        database.baze += [produkt(typo, price, "zrobiono ten chleb z jak najwiekszymi staraniami daci calych siebie "
                                               "wrecz musisz sprobowac")]
        print("Dziękuje za zakupy")
        print("chcesz kupic cos jeszcze?")
        print("tak(1),nie(2)")
        c = int(input())
        if c == 1:
            print("")
        if c == 2:
            display()
            print("Dowidzenia")
            sys.exit(0)
    if b == 2:
        display()
        print("Dowidzenia")
        sys.exit(0)


def addwoda():
    typo = "Woda"
    price = ""
    print("mamy wode gazowana oraz niegazowana")
    print("gazowana kosztuje 2zl (1) '\n' niegazowana kosztuje 1,60zl (2)")
    e = int(input())
    if e == 1:
        print("woda gazowana")
        typo += " gazowana"
        price += "2zl"
    if e == 2:
        print("woda niegazowana")
        typo += "niegazowana"
        price += "1,60zl"
    print("chcesz kupić daną rzecz?")
    print("Tak(1) Nie(2)")
    b = int(input())
    if b == 1:
        database.baze += [produkt(typo, price, "zrobiono ta wode z najkrystaliczniejszych lodowcow sam lord kruszwil "
                                               "ja pije")]
        print("Dziękuje za zakupy")
        print("chcesz kupic cos jeszcze?")
        print("tak(1),nie(2)")
        c = int(input())
        if c == 1:
            print("")
        if c == 2:
            display()
            print("Dowidzenia")
            sys.exit(0)
    if b == 2:
        display()
        print("Dowidzenia")
        sys.exit(0)


def addmleko():
    precent = "Mleko"
    price = ""

    print("Mamy mleko 2% oraz 4%")
    print("jesli chcesz mleko 2% za 2,50zl (1) '\n' jesli chcesz kupić mleko 4% za 3 zl (2)")
    q = int(input())
    if q == 1:
        print("mleko 2% kosztuje 2,50zl")
        precent += " 2%"
        price = "2,50zl"
    if q == 2:
        print("mleko 4% kosztuje 3zl")
        precent += " 4%"
        price = "3zl"
    print("chcesz kupić daną rzecz?")
    print("Tak(1) Nie(2)")
    b = int(input())
    if b == 1:
        print("Dziękuje za zakupy")
        database.baze += [produkt(precent, price, "zrobiono to mleko na polance dlatego jest takie pyszne")]
        print("chcesz kupic cos jeszcze?")
        print("tak(1),nie(2)")
        c = int(input())
        if c == 1:
            print("")
        if c == 2:
            display()
            print("Dowidzenia")
            sys.exit(0)
    if b == 2:
        display()
        print("Dowidzenia")
        sys.exit(0)


def addkrowa():
    typo = "Mięso "
    price = ""
    print("mamy schabowe oraz krowie mieso")
    print("schabowe za 7zl od kg (1) '\n'krowie mieso za 8zl od kg(2)")
    r = int(input())
    if r == 1:
        print("schabowe")
        typo += "schabowe"
        price = "7zl"
    if r == 2:
        print("krowie mieso")
        typo += "krowie"
        price = "8zl"
    print("chcesz kupić daną rzecz?")
    print("Tak(1) Nie(2)")
    b = int(input())
    if b == 1:
        database.baze += [produkt(typo, price, "zrobiono to mieso z nabardziej otylej krowy a zarazem "
                                               "najsmaczniejszej")]
        print("Dziękuje za zakupy")
        print("chcesz kupic cos jeszcze?")
        print("tak(1),nie(2)")
        c = int(input())
        if c == 1:
            print("")
        if c == 2:
            display()
            print("Dowidzenia")
            sys.exit(0)
    if b == 2:
        display()
        print("Dowidzenia")
        sys.exit(0)


def display():
    print("Produkty, które wybrałeś:")
    for produkt in database.baze:
        produkt.wypiszdane()
    print ('\n')


def displaypossibleproducts():
    possiblebutfrancheese = [produkt("schabowe oraz krowie mieso", "7 lub 8 zł za kg", "zrobiono to mieso z nabardziej "
                                                                                       "otylej krowy a zarazem najsmaczniejszej"),
                             produkt("mleko 2% oraz 4%", "2,50 lub 3 zł",
                                     "zrobiono to mleko na polance dlatego jest takie pyszne"),
                             produkt("wode gazowana oraz "
                                     "niegazowana", "2 lub 1,60 zł",
                                     "zrobiono ta wode z najkrystaliczniejszych lodowcow sam "
                                     "lord kruszwil ja pije"), produkt("chlep pszenny oraz zytni", "2 lub 2,50zł",
                                                                       "zrobiono to mleko na polance dlatego jest takie pyszne")]
    for el in possiblebutfrancheese:
        el.opisz()


def propose_a_product():
    nazwa = input("\nPodaj nazwę proponowanego produktu")
    cena = input("\nPodaj cenę proponowanego produktu")
    opis = input("\nOpisz proponowany produkt")
    database.propo += [nazwa, cena, opis]


def chooseoption():
    print("Na stanie mamy: ")
    print("mleko(1),")
    print("chleb(2),")
    print("woda(3),")
    print("mieso(4),")
    print("informacje odnoście produktów(5),")
    print ("wyświetl produkty w koszyku(6)")
    x = int(input("Wprowadź liczbę: "))
    if x == 1:
        addmleko()
    if x == 2:
        addchlep()
    if x == 3:
        addwoda()
    if x == 4:
        addkrowa()
    if x == 5:
        # displaypossibleproducts()
        print("chcesz kupic cos?")
        print("tak(1),nie(2)")
        c = int(input())
        if c == 1:
            chooseoption()
        if c == 2:
            print("Dowidzenia")
            display()
            sys.exit(0)
    if x == 6:
        display()
    if x == 7:
        print "zaproponuj produkt"
        propose_a_product()


class database():
    baze = []
    propo = []


def start():
    b = ''
    while b != 2:
        print("Dzień dobry,wypisz produkty które chcesz kupić")
        chooseoption()


start()
