# Python - Mengakses Item Tuple
## Akses item Tupple
Anda dapat mengakses item tuple dengan merujuk ke nomor indeks, di dalam tanda kurung siku. 
Contoh, cetak item kedua dalam tuple:

```py
thistuple = ("apple","banana","cherry")
print(thistuple[1])
```
## Pengindeksan Negatif
Pengindeksan negatif berarti mulai dari akhir. `-1` merujuk pada item terakhir, -2 merujuk pada item kedua terakhir, dan seterusnya.

Contoh, cetak item terakhir dari tupple:

```py
thistuple = ("apple","banana","cherry")
print(thistuple[-1])
```
## Rentang Indeks
Anda dapat menentukan rentang indeks dengan menentukan di mana meulai dan dimana mengakhiri rentang tersebut.

Saat menentukan rentang, nilai yang dikembalikan akan berupa tuple baru dengan item yang ditentukan.

Contoh, kembalikan item ketiga, keempat, dan kelima:

```py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```

> Pencarian akan dimulai pada indeks 2 (termasuk), dan berakhir pada indeks 5 (tidak termasuk)

Dengan menghilangkan nilai awal, rentang akan dimulai pada item pertama.

Contoh, ini akan mengembalikan item dari awal ke, tetapi tidak termasuk "kiwi":

```py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
```

Dengan menghilangkan nilai akhir, rentang akan berlanjut hingga akhir tuple.

Contoh, ini mengembalikan item dari "cherry" dan ke akhir:

```py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
```
## Rentang Indeks Negatif
Tentukan indeks negatif jika Anda ingin memulai penelusuran dari akhir tuple. Contoh, ini akan mengembalikan item dari indeks -4 (termasuk) ke indeks -1 (dikecualikan):

```py
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
```
## Periksa apakah item ada
Untuk menentukan apakah item tertentu ada dalam suatu tuple, gunakan kata kunci `in`.

Contoh, periksa apakah "apple" ada di tuple:

```py
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
```
