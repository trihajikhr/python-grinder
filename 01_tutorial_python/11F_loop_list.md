# Perulangan List
## Melakukan Looping melalui list
Anda dapat melakukan pengulangan melalui item-item dalam list dengan menggunakan `for` loop.

Contoh, cetak semua item dalam list, satu per satu:

```py
thislist = ["apple", "banana", "cherry"]
for x in thislist:
	print(x)
```

Pelajari lebih lanjut tentang `for` loop di bab perulangan, yang akan kita pelajari nanti.
## Ulangi melalui Nomor Indeks
Anda juga dapat menelusuri item list dengan merujuk pada nomor indeksnya. Gunakan fungsi `range()` dan `len()` untuk membuat iterable yang sesuai.

Contoh, cetak semua item dengan merujuk pada nomor indeknya:

```py
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
```

Iterable yang dibuat dalam contoh di atas adalah `[0, 1, 2]`.
## Menggunakan While Loop
Anda dapat melakukan pengulangan pada item-item dalam list dengan menggunakan perulangan `while`.

Gunakan fungsi `len()` untuk menentukan panjang list, lalu mulai dari 0 dan lakukan pengulangan melalui item list dengan merujuk ke indeksnya.

Ingatlah untuk menambah indeks sebesar 1 setelah setiap iterasi.

Contoh, Cetak semua item, menggunakan `while`loop untuk menelusuri semua nomor indeks:

```py
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
	print(thislist[i])
i = i + 1
```

Pelajari lebih lanjut perulangan `while` di bagian terpisah
## Perulangan menggunakan pemahaman list
Pemahaman list menawarkan sintaksis terpendek untuk melakukan pengulangan melalui daftar.

Contoh, sebuah `for` loop menggunakan shorthand yang akan mencetak semua item dalam list:

```py
thislist = ["apple", "banana", "cherry"]
[print(x)] for x in thislist
```

Materi ini akan dipelajari di bab terpisah oke.

Syntax ini juga bisa digunakan untuk mencetak isi list dengan cara langsung:

```py
[print(x) for x in ['apple', 'banana', 'cherry']]
```