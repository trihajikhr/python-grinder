# Python - Tuple Perulangan
## Melakukan Loop Melalui Tuple
Anda dapat melakukan pengulangan melalui item tuple dengan menggunakan perulangan `for`.

Contoh, ulangi item-item dan cetak nilainya:

```py
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
	print(x)
```

Pelajari lebih lanjut tentang perulangan for di bab terpisah.
## Loop melalui nomor indeks
Anda juga dapat melakukan pengulangan melalaui item tuple dengan merujuk pada nomor indeksnya.

Gunakan fungsi `range()` dan `len()` untuk membuat iterable yang sesuai.

Contoh, cetak semua item dengan merujuk pada nomor indeksnya:

```py
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
```
## Menggunakan While Loop
Anda juga dapat melakukan pengulangan melalui item tuple dengan menggunakan pengulangan `while`.

Gunakan fungsi `len()` tersebut untuk menentukan panjang tuple, lalu mulai dari 0 dan lakukan pengulangan melalui item tuple dengan merujuk ke indeksnya.

Ingatlah untuk menambah indeks sebesar  setelah setiap iterasi.

Contoh, cetak semua item, gunakan `while` loop untuk menelusuri semua nomor indeks:

```py
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
```

