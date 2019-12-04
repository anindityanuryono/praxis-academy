'''
- Warung bakso - Mie ayam

Penjual
Responsibilities -	Collaborators
Menanyakan mau makan apa? - Makanan, pembeli
Menanyakan mau minum apa? - Minuman pembeli
Menghitung jumlah yang harus dibayar - penjual - minuman - makanan

Pembeli
Pesan makanan - Penjual, Makanan
Pesan minuman - Penjual, Minuman
Membayar total tagihan - Penjual, minuman , makanan

'''

class Penjual:
    def __init__(self, Makan, Minum, total_harga):
        self.makanan = Makan
        self.minuman = Minum
        self.harga = total_harga

    def fungsi_Makan(mk):
        print("Saya Pesan " + mk.makanan)

    def fungsi_Minum(mn):
        print("Saya Pesan " + mn.minuman)

    def tagihan_harga(hg):

        bakso = 8000
        mie_ayam = 6000
        es_jeruk = 3000
        es_teh = 2000

        harga1 = bakso + es_jeruk
        harga2 = bakso + es_teh
        harga3 = mie_ayam + es_jeruk
        harga4 = mie_ayam + es_teh

        if tanya_mk == "bakso" and tanya_mn == "es jeruk":
            print("total tagihan: ", hg.harga, harga1)
        elif tanya_mk == "bakso" and tanya_mn == "es teh":
            print("total tagihan: ", hg.harga, harga2)
        elif tanya_mk == "mie ayam" and tanya_mn == "es jeruk":
            print("total tagihan: ", hg.harga, harga3)
        elif tanya_mk == "mie ayam" and tanya_mn == "es teh":
            print("total tagihan: " , hg.harga, harga4 )

tanya_mk = input("Mau pesan makan apa bakso atau mie ayam? ")
tanya_mn = input("Mau pesan minum apa ?")
total_harga = ("Rp.")

mk_mn = Penjual(tanya_mk, tanya_mn, total_harga)
mk_mn.fungsi_Makan()
mk_mn.fungsi_Minum()
mk_mn.tagihan_harga()


