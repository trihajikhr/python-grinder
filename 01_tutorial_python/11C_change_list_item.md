# Mengubah Item List
## Ubah nilai item
Untuk mengubah nilai item tertentu, lihat nomor indeks:
Contoh, ubah item kedua:

```py
thislist = ["Apel","Pisang","Nanas"]
thislist[1] = "Blackberry"
print(thislist)
```
## Mengubah Rentang nilai Item
Untuk mengubah nilai tem dalam rentang tertentu, tentukan daftar dengan nilai baru, dan rujuk rentang nomor indeks tempat Anda ingin memasukan nilai baru.

Contoh, ubah nilai "banana" dan "cherry" dengan "blackcurrat" dan "watermelon":

```py
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```

Jika Anda memasukkan _lebih banyak_ item daripada yang Anda ganti, item baru akan dimasukkan di tempat yang Anda tentukan, dan item yang tersisa akan dipindahkan sesuai dengan urutannya.
Contoh, ubah nilai kedua dengan menggantikany dengan dua nilai baru:

```py
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```

> **Catatan:** Panjang daftar akan berubah jika jumlah item yang dimasukkan tidak sesuai dengan jumlah item yang diganti.

Jika Anda memasukkan item _yang lebih sedikit_ daripada yang Anda ganti, item baru akan dimasukkan di tempat yang Anda tentukan, dan item yang tersisa akan dipindahkan sesuai dengan urutannya.
Contoh, ubah nilai kedua dan ketiga dengan menggantinya dengan satu nilai:

```py
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```

## Masukkan Item
Untuk menyisipkan item list baru, tanpa mengganti nilai apapun yang ada, kita dapat menggunakan fungsi `insert()`. Fungsi `insert()` memasukan item pada indeks yang ditentukan.

Contoh, masukan "watermelon" sebagai item ketiga:

```py
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

> **Catatan:** Sebagai hasil dari contoh di atas, list sekarang akan berisi 4 item.