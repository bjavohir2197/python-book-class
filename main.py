class Book:
    def __init__(self, sarlavha, muallif, sahifalar_soni):
        self.sarlavha = sarlavha
        self.muallif = muallif
        self.sahifalar_soni = sahifalar_soni

    def read(self):
        return f" Kitob nomi {self.sarlavha}, Yozuvchining ismi {self.muallif}, sahifalar soni {self.sahifalar_soni}"

b1 = Book("God father", "Mario Puso", 1000)
print(b1.read())
