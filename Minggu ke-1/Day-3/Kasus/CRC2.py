# Peminjaman buku di perpustakaan

'''
Admin
Responsibilities -	Collaborators
Melakukan register user baru - Student
Memasukkan data buku baru - Book
Memodifikasi data buku - Book
Memodifikasi data user - Student
Memberikan pinjaman buku - Student, Book
Memberikan info denda -	Student, Book

Book
Responsibilities -	Collaborators
Memberikan informasi buku - Admin, Student
Dapat dipinjam oleh user - Admin, Student

Student
Responsibilities -	Collaborators
Melakukan registrasi sebagai pinjaman - Admin
Melihat daftar buku yang ada - Book, Admin
Meminjam dan mengembalikan - Book, Admin
'''

class Student:
    def __init__(self, nama):
        self.name = nama

    def register_as_pinjaman(self, registras_dipinjam):
        print("Melakukan registrasi sebagai pinjaman")
    def daftar_buku_yang_ada(self, avalaible_book):
        print("Melihat daftar buku yang ada")
    def borrow_return(self, pinjam_kembalikan):
        print("Meminjam dan mengembalikan")

class Admin:

    def to_register_user(self, nama_user):
        users.append(Student(nama_user))
    def show_users(self, users):
        for user in users:
            print(user.name)
    def input_data_buku_baru(self, data_buku):
        print("Memasukkan data buku baru")
    def modif_data_buku(self, mod_data_buku):
        print("Memodifikasi data buku")
    def modif_data_user(self, mod_data_user):
        print("Memodifikasi data user")
    def kasih_pinjam_buku(self, pinjam_buku):
        print("Memberikan pinjaman buku")
    def info_denda(self, info_denda_buku):
        print("Memberikan info denda")

class Book:
    def info_buku(self, info_buku):
        print("Memberikan informasi buku")
    def dapat_dipinjam_user(self, dapat_dipinjam):
        print("Dapat dipinjam oleh user")

users = []
#borrows = []
a = Admin()
a.to_register_user("aan")
a.to_register_user("bayu")
a.show_users(users)
