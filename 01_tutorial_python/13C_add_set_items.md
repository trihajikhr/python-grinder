# Python - Menambahkan item Set
## Tambahkan Item
Setelah satu set dibuat, Anda tidak dapat mengubah itemnya, tetapi anda dapat menambahkan item baru.

Untuk menambahkan satu item ke satu set, gunakan fungsi `add()`.

Contoh, tambahkan item kedalam set, menggunakan fungsi `add()` berikut:

```py
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```
## Tambahkan Set
Untuk menambahkan item dari set lain ke set saat ini, gunakan  fungsi `update()`.
Contoh, tambahkan elemen dari `tropical` ke dalam `thisset`:

```py
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
```
## Tambahkan iterabel apa pun
Objek dalam fungsi atau method `update()` tidak harus berupa suatu himpunan, dapat berupa objek apapun yang dapat diulang (tuple, list, dictionary, dan lainya).

Contoh, tambahkan elemen list ke set:

```py
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
```