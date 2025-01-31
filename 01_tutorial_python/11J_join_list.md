# Join List - Python
## Gabungkan 2 list
Ada beberapa cara untuk menggabungkan, atau menyatukan, dua atau lebih list dalam python.

Salah satu cara termudah adalah dengan menggunakan operator `+`.

Contoh:

```py
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
```

Cara lain untuk menggabungkan dua list adalah dengan menambahkan semua item dari list2 ke list1, satu per satu:

Contoh, tambahkan list2 ke list1:

```py
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
```

Atau Anda dapat menggunakan `extend()`, yang tujuanya adalah untuk menambahkan elemen dari satu list ke list lainya:

Contoh, gunakan `extend()` untuk menambahkan list2 di akhir list1:

```py
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
```