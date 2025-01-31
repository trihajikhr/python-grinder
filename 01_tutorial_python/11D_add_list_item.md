# Python - Menambahkan Item List
## Tambahkan Item
Untuk menambahkan item ke akhir list, gunakan fungsi `append()`.

Contoh, menggunakan fungsi `append()` untuk menambahkan item:

```py
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

## Masukkan Item
Untuk menyisipkan item list pada indeks tertentu, gunakan fungsi `insert()`. Fungsi `insert()` memasukan item pada indeks yang ditentukan.

Contoh, masukan item sebagai posisi kedua:

```py
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

> **Catatan:** Sebagai hasil dari contoh di atas, list sekarang akan berisi 4 item.
## Perpanjang List
Untuk menambahkan elemen dari *list lain* ke list saat ini, gunakan fungsi `extend()`.

Contoh, tambahkan elemen `tropical` ke `thislist`:

```py
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

> Elemen-elemen akan ditambahkan ke _akhir_ list
## Tambahkan Iterabel Apa pun
Metode atau fungsi `extend()` tidak harus menambahkan list, Anda dapat menambahkan objek apaun yang dapat diulang (tupel, set, dictionary, dll).

Contoh, tambahkan elemen tupel ke list:

```py
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```