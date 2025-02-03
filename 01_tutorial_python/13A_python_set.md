# Python Sets
```py
myset = {"apple", "banana", "cherry"}
```
## Set
Set digunakan untuk menyimpan beberapa item dalam satu variabel.

Set adaah salah stu 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan kumpulan data, 3 lainya adalah list, tuple, dan dictionary, semuanya dengan kualitas dan penggunaan yang berbeda.

Suatu set adalah suatu koleksi yang *tidak berurutan, tidak dapat diubah\*, dan tidak memiliki indeks*.

> \*Note : Item yang ditetapkan tidak dapat diubah, tetapi Anda dapat menghapus ittem dan menambahkan item baru.

Set ditulis dengan tanda kurung kurawal.

Contoh, satu set:

```py
thisset = {"apple", "banana","cherry"}
print(thisset)
```

> Note:  Set tidak diurutkan, jadi anda tidak bisa memastikan urutan item yang akan muncul.

## Mengatur Barang
Item yang ditetapkan tidak berurutan, tidak dapat diubah, dan tidak memperbolehkan nilai duplikat.
## Tidak Berurut
Tidak berurutan artinya item-item dalam satu set tidak mempunyai urutan yang pasti. Item yang ditetapkan dapat munccul dalam urutan berbeda setiap kali anda menggunakanya, dan tidak dapat dirujuk berdasarkan indeks atau kunci.
## Tidak dapat diubah
Item yang ditetapkan dapat diubah, artinya kita tidak dapat mengubah item setelah set dibuat.

> Setelah satu set dibuat, Anda tidak dapat mengubah itemnya, tetapi anda dapat menghapus item dan menambahkan item baru.
## Duplikat Tidak Diizinkan
Set tidak dapat memiliki dua item dengan nilai yang sama. Contoh, nilai duplikat akan diabaikan:

```py
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
```

> Note : Nilai `True` dan `1` dianggap sebagai nilai yang sama dalam Set, dan diperlakukan sebagai duplikat

Contoh ,`True` dan `1` dianggap memiliiki nilai yang sama:

```py
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
```

> Note : Nilai `False` dan `0` dianggap sebagai nilai yang sama dalam set, dan diperlakukan sebagai duplikat

Contoh, `False` dan `0` dianggap memiliki nilai yang sama:

```py
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
```
## Dapatkan panjang Set
Untuk menentukan berapa banyak item yang dimiliki suatu set, gunakan fungsi `len()`.

Contoh, dapatkan jumlah item dalam satu set:

```py
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
```
## Set item - Tipe Data
Item yang ditetapkan dapat berupa tipe data apa pun.

Contoh, tipe data string, int, dan boolean:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
```

Satu set dapat berisi berbagai tipe data. 

Contoh, satu set dengan string, integer, dan nilai boolean:

```py
set1 = {"abc", 34, True, 40, "male"}
```
## type()
Dari perspektif Python, himpunan didefinisikan sebagai objek dengan tipe data `set`:

```bash
<class 'set'>
```

Contoh, apa tipe data suatu set?

```py
myset = {"apple", "banana", "cherry"}
print(type(myset))
```
## Konstruktor set()
Dimungkinkan juga untuk menggunakan konstruktor `set()` untuk membuat suatu set.

Contoh, menggunakan konstruktor set() untuk membuat satu set:

```py
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```