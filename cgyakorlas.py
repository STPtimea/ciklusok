def harom():

    for i in range(0,21,1): #vagy >> for i in range(21): vagy >> for i in range(0,21):
        print(i)
'''
Ugyanez while-al
i = 0
while i<21:
    print(i)
    i +=1
'''
def negy():
    for i in range(20,57,2):
        print(i)

def ot():
    for i in range(77,-77,-4):
        print(i)


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot: "))
    return szam
def hat ():

    szam1 = beolvas()
    szam2 = beolvas()

    if szam2 < szam1:
        #csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")

#7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
def het ():

    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2
    if szorzat <0:
        for i in range(0, szorzat-1,-1):
            print(i, end=" ")

    else:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
'''
Kérem adjon meg egy egész számot: 3
Kérem adjon meg egy egész számot: 2
0 1 2 3 4 5 6 
'''

# 8.	Írd meg a fenti feladatot while és for ciklussal is!
def nyolc():

if szorzat < 0:
    i = 0





def kilen():
    pass