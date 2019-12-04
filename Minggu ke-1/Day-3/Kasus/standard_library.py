# menghitung sisi miring segitiga
import math
def main():
    a = float(input("Masukkan panjang sisi A: "))
    b = float(input("Masukkan panjang sisi B: "))
    # menghitung sisi miring segitia
    c = math.hypot(a,b)
    # display pangjang sisi miring segitiga
    print("panjang sisi miring segitiga adalah ", c)
main()

