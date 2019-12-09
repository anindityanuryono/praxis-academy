from name_function import get_formatted_name
print("tekan'q' untuk keluar.")
while True:
    first = input("\nMasukkan nama depan: ")
    if first == 'q':
        break
    last = input("Masukka nama belakang: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNama Lengkap: {formatted_name}.")