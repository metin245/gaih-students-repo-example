class Tarifler:
    def __init__(self,ad):
        self.ad=ad
    def add_ing(self,ing):
        if ing not in self.malzemeler:
            self.malzemeler.append(ing)
    def cook(self):
        print("Pişmesi için yeteri kadar süre ocağa koy.")
    def tuz(self):
        print("kararınca tuz konulur.")
    def baharat(self):
        print("İstediğiniz baharatları koyun")
    def malzemeler(self):
        print ("tüm malzemeleri tencereye/tavaya koy.")
    def sukoy(self):
        print("tencereye su koy ")

class makarna(Tarifler):
    def __init__(self,ad,malzemeler=None):
        super().__init__(ad)
        if malzemeler is None:
            self.malzemeler=[]
        else:
            self.malzemeler=malzemeler

class pilav(Tarifler):
    def __init__(self,ad,malzemeler):
        super().__init__(ad)
        if malzemeler is None:
            self.malzemeler=[]
        else:
            self.malzemeler=malzemeler

class corba(Tarifler):
    def __init__(self,ad,malzemeler):
        super().__init__(ad)
        if malzemeler is None:
            self.malzemeler=[]
        else:
            self.malzemeler=malzemeler

def menu():
    print("Tarifini istediğiniz yemeği saçiniz")
    print("1.Makarna 2.Pilav 3.Mercimek Çorbası 4.Çıkış", sep="***")
    choice = input("Seçiminizi Giriniz:")
    if choice == "1":
        mk=makarna('italiano')
        mk.add_ing('makarna')
    elif choice == "2":
        pl=pilav('pirinç')
        pl.add_ing()
    elif choice == "3":
        cb=corba('mercimek')
        cb.add_ing
    elif choice=='4':
        exit()
    else:
        print("doğru bir değer girmediniz.")
        menu()

menu()
