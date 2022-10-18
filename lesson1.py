import math as m
import random
import time
import pyautogui as pag
import os
#открытие.закрытие файла
#f = open("name of file", "parameter")
#    ...
#f.close()


#with open("name of file", "parameter") as f:
#    ...
#parameters:
#r - open for reading
#w - open for write
#x - create file
#a - open for rewrite file (in end)
#b - open in double mode
#t - open in txt mode
#+ - open for reading and write
#file.readlines - read all strings
#file.read(size) - read fix size

#example:
#with open('test.txt', 'x') as f:
#   f.write('ghghhg')




def read(seqv):
    with open('Ensembl.txt', 'r') as f:
        for line in seqv:
            if '>' in string:
                title = string


        rna = dna.replace('U', 'T')
        list0fOrf = []
        orf1 = [rna[i:i + 3]
        for i in range(0, len(rna), 3)]
        orf2 = [rna[i:i + 3]
        for i in range(1, len(rna), 3)]
        orf3 = [rna[i:i + 3]
        for i in range(2, len(rna), 3)]
        list0fOrf.append(orf1)
        list0fOrf.append(orf2)
        list0fOrf.append(orf3)
        for i in orf:
            if 'AUG' in orf:
                if 'UAG' | 'UGA' | 'UAA':
                    print("True")
                else:
                    print("False")
            else:
                print("False")

# AUG - старт-кодон
# UAG, UGA, UAA - стоп-кодоны

with open('Ensembl.txt', 'r') as f:
    mylist = []
    rna = dna
