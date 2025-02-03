# Python - Join Set
## Join Set
Ada beberapa cara untuk menggabungkan dua atau lebih set dalam Python.

Metode `union()` dan `update()` menggabungkan semua item dari kedua set. 

Method `intersection()` HANYA menyimpan duplikat.

Method `difference()` menyimpan item dari set pertama yang tidak ada di set lainya.

Method `symmetric_difference()` menyimpan semua item KECUALI duplikat.
## Union
Methode atau fungsi `union()` mengembalikan set baru dengan semua item dari kedua set. Contoh, gabungkan set1 dan set2 menjadi set baru:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
```

Anda dapat menggunakan operator pipe `|` sebagai ganti method `union()`, dan Anda akan mendapatkan hasil yang sama. Contoh, `|` digunakan untuk menggabungkan set:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
```

## Gabungkan Beberapa Set
Semua method dan operator penggabungan dapat digunakan untuk menggabungkan beberapa set.

Saat menggunakan suatu method, cukup tambahkan lebihi banyak set dalam tanda kurung, pisahkan dengan koma. Contoh, gabungkan beberapa set dengan method `union()`:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
```

Saat menggunakan operator `|`, pisahkan set dengan lebih banyak operator `|`. Contoh, gunakan operator `|` untuk menggabungkan dua set:

```py
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
```

## Gabungkan Set dan Tuple
Metode `union()` memungkinkan anda menggabungkan satu set dengan tipe data lain, seperti list atau tuple.

Hasilnya akan menjadi satu set. Contoh, gabungkan satu set dengan tuple:

```py
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
```

> Note : Operator `|` hanya memungkinkan Anda untuk menggabungkan set dengan set, dan tidak dengan tipe data lain, seperti yang dapat anda lakukan dengan method `union()`.

## Update
Method `update()` memasukan semua item dari satu set ke set lainya. Mengubah `update()` set asli, dan tidak mengembalikan set baru.

Contoh, method `update()` memasukan item dalam set2 ke dalam set1:

```py
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
```

> Note : Keduanya `union()` dan `update()` akan mengembalikan item duplikat.

## Intersection
Simpan HANYA duplikatnya.

Method `intersection()` akan mengembalikan satu set baru, yang hanya berisi item yang ada di kedua set.

Contoh, gabungkan set1 dan set2, tetapi simpan hanya duplikatnya:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
```

Anda dapat menggunakan operator `&` sebagai ganti `intersection()`, dan akan mendapatkan hasil yang sama. Contoh:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
```

> Note : Operator `&` hanya memungkinkan Anda untuk menggabungkan set dengan set, dan tidak dengan tipe data lain seperti yang dapat Anda lakukan dengan `intersection()`metode ini.

Metode ini `intersection_update()`juga HANYA akan menyimpan duplikat, tetapi akan mengubah set asli alih-alih mengembalikan set baru.

Contoh, simpan item yang ada di `set1`, dan `set2`:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
```

Nilai `True`dan `1` dianggap sebagai nilai yang sama. Hal yang sama berlaku untuk `False`dan `0`.

Contoh, gabungkan set yang berisi nilai `True`, `Falsae`, `1`, dan `0`, dan lihat apa yang dianggap duplikat:

```py
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
```
## difference
Method `difference()` akan mengembalikan set baru yang hanya berisi item dari set pertama yang tidak ada di set lainya.

Contoh, simpan semua item dari set1 yang tidak ada di set2:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
```

Anda dapat menggunakan operator `-` sebagai ganti method `difference()`, dan Anda akan mendapatkan hasil yang sama. Contoh:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
```

> Note : Operator `-` hanya memungkinkan Anda untuk menggabungkan set dengan set, dan tidak dengan tipe data lain seperti yang dapat Anda lakukan dengan `difference()`metode ini.

Metode ini `difference_update()`juga akan menyimpan item dari set pertama yang tidak ada di set lainnya, tetapi akan mengubah set asli alih-alih mengembalikan set baru.

Contoh, gunakan `difference_update()`, method ini untuk menyimpan item yang tidak ada di kedua set:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
```

## symmetric_difference
Method atau fungsi `symmetric_difference()` hanya akan menyimpan elemen yang TIDAK ada dalam kedua set.

Contoh, simpan item yang tidak ada di kedua set:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
```

Anda dapat menggunakan operator `^` sebagai ganti `symmetric_difference()`, dan Anda akan tetap mendapatkan hasil yang sama:


```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
```

> Note : Operator `^` hanya memungkinkan Anda untuk menggabungkan set dengan set, dan tidak dengan tipe data lain seperti yang dapat Anda lakukan dengan `symmetric_difference()`metode ini.

Metode ini `symmetric_difference_update()`juga akan menyimpan semuanya kecuali yang duplikat, tetapi akan mengubah set asli alih-alih mengembalikan set baru.

Contoh, gunakan `symmetric_difference_update()`, method ini untuk menyimpan item yang tidak ada di kedua set:

```py
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
```

