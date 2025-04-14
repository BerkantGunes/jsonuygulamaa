class User:
    pass

class UserRepository:
    def register(self): #register fonksiyonu
        pass
    def login(self):
        pass
    def savetoFile(self):
        pass

while True:
    print('Menu'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseciminiz: ')
    if secim == '5':
        break

    else:
        if secim == '1':
            pass #register
        elif secim == '2':
            pass #login
        elif secim == '3':
            pass #logout
        elif secim == '4':
            pass # display username
        else:
            print('yanlis secim')
        