# Python - Remove List Items
## Hapus Item Tertentu
Fungsi `remove()` menghapus item yang ditentukan.

Contoh, hapus "banana":

```py
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

Jika ada lebih dari satu item dengan nilai yang telah ditentukan, maka fungsi `remove()` akan menghapus kemunculan pertama.

Contoh, hapus kemunculan pertama "banana":

```py
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
```
## Hapus indeks tertentu
Fungsi `pop()` menghapus indeks yang ditentukan.

Contoh, hapus item kedua:

```py
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```

Jika Anda tidak menentukan indeks, fungsi `pop()` akan menghapus item terakhir.

Contoh, hapus item terakhir:

```py
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
```

Kata kunci `del` juga menghapus indeks yang ditentukan.

Contoh, hapus item pertama:

```py
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
```

Kata kunci `del` juga dapat menghapus daftar sepenuhnya.

Contohnya, hapus seluruh daftar:

```py
thislist = ["apple", "banana", "cherry"]
del thislist
```
## Hapus list
Fungsi `clear()` akan mengosongkan list. Listnya masih ada, tetapi isinya dihapus, atau tidak ada.

Contoh, hapus isi list:

```py
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
```