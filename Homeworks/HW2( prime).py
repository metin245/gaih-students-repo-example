""" Kodu Biraz Daha Geliştirerek Random Olarak Verilen Aralıkta Sadece Asal ve tekrar Etmeyen (Uniq)
 Değerin 3x3 Matris Şeklinde Gösterimi:
"""
import random

asal = []
# Random İnteger Sayı Üretiyoruz.
num=random.randint(1,1000)
# Asal Olup Olmadığını Kontrol Ediyoruz Ve Asal Değilse Yeniden Sayı Üretiyoruz.
for i in range(2, num):
    k = True
    for j in range(2,i):
        if i%j == 0:
            k=False
    if k:
# Tekrar etmeyen Değerleri Listeye Ekliyoruz.
        while i in asal:
            continue
        asal.append(i)
print (asal)