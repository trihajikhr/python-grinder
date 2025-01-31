# Mengakses item list
## Akses item
Item dalam list diindeks, dan anda dapat mengaksesnya dengan merujuk ke nomor indeks:

Contoh, cetak item kedua dari list:

```py
thislist = ["apel", "pisang", "cherry"]
print(thislist(1))
```

## Pengindeksan negatif
Pengindeksan negatif berarti mulai dari akhir. `-1` merujuk pada item terakhir, `-2` merujuk pada item kedua terakhir, dan seterusnya.

Contoh, cetak item terakhir dari list:

```py
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
## Rentang Indeks
Anda dapat menetukan rentang indeks dengan menentukan dimana memulai dan dimana mengakhiri rentang tersebut.

Saat menentukan rentang, nilai yang dikembalikan akan berupa list baru dengan item yang ditentukan.

Contoh, kembalikan item ketiga, keempat, dan kelima:

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```

> Note : Pencarian akan dimulai pada indeks 2 (termasuk) dan berakhir pada indeks 5 (tidak termasuk). Ingat bahwa item pertama memiliki indeks 0.

Dengan menghilangkan nilai awal, rentang akan dimulai pada item pertama.

Contoh, ini mengembalikan item dari awal ke, tetapi TIDAK termasuk "kiwi":

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```

Dengan menghilangkan nilai akhir, rentang akan berlanjut hingga ke akhir list.
Contoh, ini mengambalikan tem dari "cherry" hingga akhir:

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```
## Rentang indeks negatif
Tentukan indeks negatif jika Anda ingin memulai pencarian dari akhir list.
Contoh, ini akan mengembalikan item dari "orange" (-4) hingga, tetapi tidak termasuk "mango" (-1):

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```
## Periksa apakah item ada
Untuk menentukan apakah suatu item tertentu ada dalam suatu daftar, gunakan kata kunci `in`.

Contoh, periksa apakah "apple" ada dalam daftar:

```py
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```