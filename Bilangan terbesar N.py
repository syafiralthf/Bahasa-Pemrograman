#inisialisasi variabel untuk menyimpan bilangan terbesar
bilangan_terbesar = float('-inf') # inisialisasi dengan nilai terkecil

while True:
    bilangan = float(input("Masukan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break # keluar dari loop jika input 0
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

# memeriksa apakah ada bilangan yang dimasukkan
if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar)