a = int(input('Masukan bilangan petama: '))
b = int(input('Masukan bilangan kedua: '))
c = int(input('Masukan bilangan ketiga: '))

if a > b and a > c:
    print(f'Bilangan terbesar adalah {a}')
elif b > a and b > c:
    print(f'Bilangan terbesar adalah {b}')
else:
    print(f'Bilangan terbesar adalah {c}')