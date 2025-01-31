# Copy List
## Copy list
Anda tidak dapat menyalin list hanya dengan mengetik `list2 = list1`, karena: `list2` hanya akan menjadi *referensi* ke `list1`, dan perubahan yang dibuat dalam `list1` akan secara otomatis juga dibuat dalam `list2`
## Gunakan Metode copy()
Anda dapat menggunakan fungsi list bawaan yaitu `copy()` untuk menyalin list.

Contoh, buat salinan list dengan fungsi `copy()`:

```py
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
```

## Gunakan metode list()
Cara lain membuat salinan adalah dengan menggunakan fungsi bawaan list lain yaitu `list()`.
Contoh, buat salinan list dengan fungsi `list()`:

```py
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
```

## Gunakan operator irisan
Anda juga dapat membuat salinan list dengan menggunakan operator irisan `:`.
Contoh:

```py
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
```
