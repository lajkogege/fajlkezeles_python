"""Készits metodust amely kiszámolja a személyek átlag életkorát"""

def atlageletkor(lista:[]):
    osszeg:int=0
    for i in range(0,len(lista),1):
        osszeg+= lista[i].kor

    return osszeg/len(lista)


"""készíts metodust mely megmondja a nők számét a listában"""

def nok_szama(lista_no:[]):
    osszeg:int=0
    for i in range(0,len(lista_no),1):
        if lista_no[i].nem ==" nő":
            osszeg+=1
    return osszeg
