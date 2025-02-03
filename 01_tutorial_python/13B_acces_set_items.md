# Python - Mengakses Item Set
## Akses Item
Anda tidak dapat mengakses item dalam satu set dengan merujuk pada indeks atau kunci.

Namun anda dapat melakuka pengulangan melaui item-item yang ada dalam set menggunakan `for` loop, atau menanyakan apakah suatu nilai tertentu ada dalam satu set, dengan menggunakan kata knci `in`.

Contoh, ulangi rangkaian tersebut, dan cetak nilainya:

```py
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

Contoh, periksa apakah "banana" ada di set:

```py
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

Contoh, periksa apakah "banana" TIDAK ada di set:

```py
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
```
## Ubah item
Setelah satu set dibuat, Anda tidak dapat mengubah itemnya, tetapi Anda dapat menambahkan item baru.