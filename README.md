# Biodata

Nama = Syafira Luthfi Azzahra

NIM = 321410353

Kelas = TI.24.A.4

# LATIHAN 1

<img width="712" alt="image" src="https://github.com/user-attachments/assets/1447f1ff-cdc7-42cd-a86c-90956cac26f5">

## PENGGUNAAN END
<img width="286" alt="image" src="https://github.com/user-attachments/assets/6d7f5c02-fa7a-46bf-97b4-1bf8f3a45e90">

```python
print('A', end='')
print('b', end='')
print('c', end='')
print()
print('x')
print('y')
print('z')
```

Parameter end dalam fungsi Print () di python di gunakan untuk menambahkan string(" ")apapun diakhir dan mengeluarkan pertanyaan print

```python
print()
```

Secara default,fungsi print() akan mengakhiri dengan baris baru,dan akan secara otomatis karakter baris baru di akhir outputnya

inilah hasil program tersebut:

![Screenshot 2024-10-19 105401](https://github.com/user-attachments/assets/e4be0ae6-0c1e-46ab-a947-1470668b5387)

dan ini hasil tanpa menggunakan fungsi print() di tengah pada kode program di atas:

![Screenshot 2024-10-19 105727](https://github.com/user-attachments/assets/ce8c4426-642e-4460-b59e-31b88d4bd59b)

# PENGGUNAAN SEREPATOR

![Screenshot 2024-10-19 105946](https://github.com/user-attachments/assets/f883e3f9-751b-4be6-973a-a1720cf8d062)

```python
w, x, y, z, =10, 15, 20, 25
print(w, x, y, z,)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
```
pada python penggunaan serepator dapat menggunakan fungsi split() atau sep yang seperti dalam kode program di atas

serepator ini menentukan pembatasan yang digunakan untuk memisahkan sting,serepator dapat berupa karakter tunggal atau beberapa karakter.jika tidak ditentukan,maka python akan menggunakan spasi sebagai pemisah.

Berikut Hasil Kode Program Diatas:

![Screenshot 2024-10-19 111502](https://github.com/user-attachments/assets/9afa0286-fcd8-437e-8319-0da6019ef34e)

```python
w, x, y, z, =10, 15, 20, 25
```
Variable yang seperti ini menentukan parameter,jadi variable ini tidak bisa memasukan variable angka yang sudah ditentukan w = 10,x=15,y=20,z=25

```python
print(w, x, y, z,)
```

Fungsi ini hanya mencetak saja yang menggunakan fungsi print(), tetapi di karenakan mencetak parameter,koma tersebut di hilangkan

```python
print(w, x, y, z, sep=',')
```
karena pemisahnya dihilangkan,kita menggunakan fungsi `sep`atau`split()`dan kita memasukkan pemisahnya didalam string akan memunculkan cetakan yang sesuai keinginan anda dalam memisahkan sesuatu parameter

# LATIHAN 2

![Cuplikan layar 2024-10-21 191320](https://github.com/user-attachments/assets/544b1fa9-2860-4cd2-a27a-90c8bf6386c5)

```python
a=int(input("masukan nilai a:"))
b=int(input("masukan nilai b:"))
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil pejumlah {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
```

Jika kita run file maka akan muncul tampilan seperti ini:

![Cuplikan layar 2024-10-21 193438](https://github.com/user-attachments/assets/b16d50ae-30e1-440d-a24b-cfee32d30e85)


# STRING FORMAT

![Screenshot 2024-10-19 112724](https://github.com/user-attachments/assets/d5f2d127-76c0-4653-996c-aa5e6d201274)

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**6)
print(7, 10**7)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```
String Format adalah proses memasukan variable atau string kustom ke dalam teks yang sudah ditentukan,dan dapat digunakan untuk berbagai keperluan,seperti memasukan judul dalam grafik,menampilkan pesan atau kesalahan, atau meneruskan kesalahan ke suatu fungsi 

```python
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)
```

Nilai pertama dalam setiap pasangan adalah angka dari 0 hingga 10, kode program ini dihitung dengan menggunakan operasi pangkat atau fungsinya (**) untuk menaikkan 10 ke pangkat yang sesuai dengan angka pertama, yang bisa di bahasa manusiakan variable 0 = 10 pangkat 0, variable 1 10 pangkat 1 dan seterusnya hingga variable 10 yaitu 10 pangkat 10, dan di cetak dengan fungsi print()

```python
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```

Kode ini mencetak 11 baris dengan format {0:3} {1:16} yang di gunakan untuk mengatur format string

Pada string pertama, angka 0 di format untuk memeliki lebar 3 karakter atau yang bisa disebut 3 kali spasi dengan perataan kanan.

angka 1 diformat untuk memiliki lebar 16 Karakter atau 16 kali spasi dengan perataan kanan, dan masing-masing mencetak nilai seperti format di atas dengan fungsi print()

# PRAKTIKUM 3

![Screenshot 2024-10-19 095852](https://github.com/user-attachments/assets/18c4eb26-8df1-45df-afb3-dee64f83a5f9)

# Flowchart Bilangan Terbesar dari 3 Bilangan

![Flowchart github](https://github.com/user-attachments/assets/c669c033-cc03-4132-822e-6070a5fb905a)

# Berikut screenshoot program nya

![Cuplikan layar 2024-10-21 114535](https://github.com/user-attachments/assets/dfcc21c3-581d-430b-9604-775989517c37)

```python
bilangan_terbesar = float('-inf')

while True:
    bilangan = float(input("Masukan bilangan (tekan 0 untuk berhenti): "))
    if bilangan == 0:
        break 
    if bilangan > bilangan_terbesar:
        bilangan_terbesar = bilangan

# memeriksa apakah ada bilangan yang dimasukkan
if bilangan_terbesar == float('-inf'):
    print("Tidak ada bilangan yang dimasukan.")
else:
    print("Bilangan terbesar adalah:", bilangan_terbesar)
```

Setiap angka di input akan membandingkan dengan angka yang telah di input lainnya untuk menentukan angka yang terbesar sesuai dengan perintah

# Flowchart Bilangan terbesar

![github](https://github.com/user-attachments/assets/ecbc09ba-0ef2-40ec-a09e-9cfade73216f)

```python
a = int(input('Masukan bilangan petama: '))
b = int(input('Masukan bilangan kedua: '))
c = int(input('Masukan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}')
```

Program ini digunakan untuk menemukan bilangan yang terbesar dari tiga bilangan yang telah di input oleh pengguna. Program meminta tiga bilangan untuk dibandingkan dan kemudian mencetak bilangan terbesar

# Berikut screenshoot program nya

![Cuplikan layar 2024-10-21 115637](https://github.com/user-attachments/assets/c33c4ebf-bd87-45c3-b34d-7c4ad6685a32)
