# Python - Memodifikasi String
Python memiliki seperangkat metode bawaan yang dapat Anda gunakan pada string.
## Huruf besar
Contoh, metode `upper()` ini mengembalikan string dalam huruf besar:

```py
a = "Hello, World!"
print(a.upper())
```

## Huruf kecil
Contoh, metode `lower()` mengembalikan string dalam huruf kecil:

```py
a = "Hello, World!"
print(a.lower())
```
## Huruf Spasi
Whitespace adalah spasi sebelum dan/atau sesudah teks sebenarnya, dan sering kali Anda ingin menghapus spasi ini.
Contoh, menggunakan fungsi `strip()` menghapus spasi apapun dari awal atau akhir:

```py
a = "Hello, World!"
print(a.strip()) #mengembalikan "Hello, World!"
```
## Replace String
Contoh, metode ini mengganti string dengan string lain, dengan fungsi `replace()`:

```py
a = "Hello, World!"
print(a.replace("H","J"))
```
## Split String
Metode `split()` mengembalikan daftar dimana teks diantara pemisah yang ditentukan menjadi item daftar, atau list.

Contoh, metode ini membagi string menjadi sub-string jika menemukan contoh pemisah:

```py
a = "Hello, World!"
print(a.split(",")) # mengembalikan ['Hello','World!']
```

Untuk materi list, akan kita pelajari di tutorial terpisah.
