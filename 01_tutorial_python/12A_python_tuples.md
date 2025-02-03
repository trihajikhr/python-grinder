# Tuple Python
## Tuple
Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.

Tuple adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan kumpulan data, 3 lainya adalah `list`, `set`, dan `dictionary`. Semuanya dengan kualitas dan penggunaan yang berbeda.

Tuple adalah suatu koleksi yang teratur dan **tidak dapat diubah**.

Tuple ditulis dengan kurung bulat.

Contoh:

```py
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

## Item tuple
Item Tuple berssifat teratur, tidak dapat diubah, dan memperbolehkan nilai duplikat. Item Tuple diindeks, item pertama memiliki indeks `[0]`, item kedua memiliki indeks `[1]`, dan seterusnya.

## Ordered
Ketika kita katakan bahwa tuple tersusun secara berurutan, artinya item-itemnya mempunyai susunan yang pasti, dan susunan itu tidak akan berubah.
## Tidak dapat diubah
Tuple tidak dapat diubah, artinya kita tidak dapat mengubah, menambah, atau menghapus item setelah tuple dibuat.
## Izinkan duplikat
Karena tupel diindeks, tupel tersebut dapat memiliki item dengan nilai yang sama:

Contoh, tuple memperbolehkan nilai duplikat:

```py
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```
## Panjang Tuple
Untuk menentukan berapa banyak item yang dimiliki suatu tuple, gunakan fungsi `len()`.
Contoh, cetak jumlah item dalam tuple:

```py
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

## Buat Tuple Dengan Satu Item
Untuk membuat tupel dengan hanya satu item, Anda harus menambahkan koma setelah item, jika tidak, Python tidak akan mengenalinya sebagai tupel.

Contoh:

```py
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```
## Item Tuple - Tipe Data
Item tuple dapat berupa tipe data apa pun.
Contoh, tipe data string, int, dan boolean:

```py
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

Sebuah tuple dapat berisi tipe data yang berbeda. 
Contoh, tuple dengan nilai string, integer, dan boolean:

```py
tuple1 = ("abc", 34, True, 40, "male")
```
## type()
Dari perspektif python, tuple didefinisikan sebagai objek dengan tipe data 'tuple':

```bash
<class 'tuple'>
```

Contoh:

```py
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
```
## Konstruktor Tuple()
Dimungkinkan juga untuk menggunakan konstruktor `tuple()` untuk membuat tuple.

Contoh, menggunakan metode `tuple()` untuk membuat tuple:

```py
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

