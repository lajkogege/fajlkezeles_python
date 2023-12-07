from Szemely import Szemely

szemelyek_lista=[] #itt tárolom a létrehozott osztálypéldányokat
fajlom= open("teszt.txt", "r", encoding='utf-8')
fajlom.readline()
string_lista=fajlom.readlines()
fajlom.close()
for i in range(0,len(string_lista),1):
    """minden sort szét kell bontani"""
    aktsor:str=string_lista[i].strip()
    """Eltávolitsuk a sorok végéről a sor törést """
    print(aktsor)
    """Jenő, férfi, 16\n"""
    sor_lista=aktsor.split(",")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])
    szemely=Szemely(sor_lista[0],sor_lista[1], int(sor_lista[2]))
    szemelyek_lista.append(szemely)


for i in range(0,len(szemelyek_lista),1):
    print(f"{szemelyek_lista[i].nev}, {szemelyek_lista[1]}, {szemelyek_lista[i].nem}")


import feladatok_szemelyek_listaval
atlageletkor=feladatok_szemelyek_listaval.atlageletkor(szemelyek_lista)
print(f"{atlageletkor}")

osszeg=feladatok_szemelyek_listaval.nok_szama(szemelyek_lista)
print(osszeg)
