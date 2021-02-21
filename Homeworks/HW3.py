def prime_first():
    for i in range(500):
        k = True
        if i<=1:
            k=False
        for j in range(2, i):
            if i%j == 0:
                k = False
        if k:
           print(i)



def prime_second():
    for i in range(500,1000):
        k = True
        for j in range(2, i):
            if i%j == 0:
                k = False
        if k:
           print(i)

prime_first()
prime_second()
