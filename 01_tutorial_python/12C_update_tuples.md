# Python - Memperbarui Tuple
Tuple tidak dapat diubah, artinya anda tidak dapat mengubah, menambah, atau menghapus item setelah tuple dibua.

Namun ada beberapa solusi.
## Mengubah Nilai Tuple
Setelah sebuah  tuple dibua, anda tidak dapat mengubah nilainya. Tuple **tidak dapat diubah**, atau disebut juga **immutable**.

Namun, ad solusinya. Anda dapat mengubah tuple menjadi list, mengubah list, dan mengubah list lagi menjadi tuple.

Contoh, ubah tuple menjadi list, agar kita dapat mengubahnya:

```py
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

## Tambahkan Item
Karena tuple tidak dapat diubah, tuple tidak memiliki fungsi bawaan `append()`, tetapi ada cara lain untuk menamahkan item ke tuple.

1. **Ubah menjadi list**: Sama seperti solusi sebelumnya, kita dapat mengubah tuple menjadi list, menambahkan item, dan mengubahnya kembali menjadi tuple. Contoh, ubah tuple menjadi list, tambahkan item "orange", dan ubah kembali menjadi tuple:

```py
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
```

2. **Tambahkan tuple ke tuple**: Anda diperbolehkan menambahkan tuple ke tuple, jadi jika anda ingin menambahkan satu item (atau banyak), buat tuple baru dengan itemtersebut, dan tambahkan ke tuple yang sudah ada. Contoh, buat tuple baru dengan nilai "orange", dan tambahkan ke tuple tersebut:
```py
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
```

> Note : Saat membuat tuple dengan hanya satu item, ingatlah untuk menyertakan tanda koma setelah item, jika tidak, item tersebut tidak aakn diidentifikasi sebagai tuple.

## Hapus item
> Note : Anda tidak dapat menghapus item dalam tuple

Tuple **tidak dapat diubah**, jadi anda tidak dapat menghapus item darinya, tetapi anda dapat menggunakan solusi yang sama seperti yang kami gunakan untuk mengubah dan menambahkan item tuple.

Contoh, ubah tuplee menjadi list, hapus "apple", dan ubah kembali menjadi tuple:

```py
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
```

Atau anda dapat menghapus tuple sepenuhnya. Contoh, kata kunci `del` dapat menghapus tuple sepenuhnya:

```py
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
```