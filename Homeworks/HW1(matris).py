
# Manuel Olarak Girdiğimiz Asal Sayıların 3x3 Matris Şeklinde Gösterimi:
row = [[3, 5, 7], [9, 1, 13], [15, 17, 19]]
for i in range(3):
    row_new = []
    for j in range(3):
        row_new.append(row[i][j])
        if j == 2:
            print(row_new)


print("**********************************************************************************************")
print("  ****************************************************************************************   ")
print("Kodun Geliştirilmiş Hali")
""" Kodu Biraz Daha Geliştirerek Random Olarak Verilen Aralıkta Sadece Asal ve Tekrar Etmeyen (Uniq)
 Değerin 3x3 Matris Şeklinde Gösterimi:
"""
import random

asal = []
asal1=[]
# Random İnteger Sayı Üretiyoruz.
num=random.randint(1,1000)
print(num)
# Asal Olup Olmadığını Kontrol Ediyoruz.
for i in range(2, num   ):
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

# Asal Sayı Listemizdeki Değerlerden İlk Dokuzunu  i,j İndexine Uygun Hale Getiriyoruz.
asal_1=[]
for i in range(9):

    asal_1.append(asal[i])
print(asal_1)
first_row=[]
second_row=[]
third_row=[]
for i in range(3):
    first_row.append(asal_1[i])
for i in range(3,6):
    second_row.append(asal_1[i])
for i in range(6,9):
    third_row.append(asal_1[i])
print(first_row,second_row,third_row, sep="\n")
