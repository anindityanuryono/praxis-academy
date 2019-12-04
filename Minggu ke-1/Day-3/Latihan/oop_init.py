class Orang:
    def __init__(self, nama):
        self.nama = nama
    def say_hi(self):
        print("hi, nama saya adalah", self.nama)

p = Orang('Aan')
p.say_hi()