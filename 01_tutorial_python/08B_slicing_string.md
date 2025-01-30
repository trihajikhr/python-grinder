# Python - Memotong String
## Slicing / mengiris
Anda dapat mengembalikan serangkaian karakter dengan menggunakan sintaksis irisan. tentukan indeks awal dan indeks akhir, dipisahkan dengan titik dua, untuk mengembalikan bagian string.

Contoh, dapatkan karakter dari posisi 2 ke posisi 5 (tidak termasuk):

```py
b = "Hello, World!"
print(b[2:5])
```

> Note : Karakter pertama memiliki indeks 0

Dengan menghilangkan indeks awal, rentang akan dimulai pada karakter pertama.
Contoh, dapatkan karakter dari awal hingga posisi 5 (tidak termasuk):

```py
b = "Hello, World!"
print(b[:5])
```

## Slicing / potong sampai akhir
Dengan menghilangkan indeks terakhir, rentangnya akan sampai ke akhir.
Contoh: Dapatkan karakter dari posisi 2, dan sampai akhir:

```py
b = "Hello, World!"
print(b[2:])
```
## Pengindeksan Negatif
Gunakan indeks negatif untuk memulai irisan dari akhir string.
Contoh: Dapatkan karakternya:
Dari "o" di "World" (posisi -5)
Dengan, tetapi tidak termasuk: "d" di "World" (posisi -2)

```py
b = "Hello, World!"
print(b[-5:-2])
```

Maka outpunya:

```shell
orl
```

 