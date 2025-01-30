# Python - Variable Keluaran
## Variabel Keluaran
Fungsi Python `print()` sering digunakan untuk mengeluarkan variabel.
Contoh: 

```py
x = "Python sangat keren"
print(x)
```

Dalam `print()` , Anda juga dapat mengeluarkan beberapa variabel, yang dipisahkan dengan koma.
Contoh:

```py
x = "Python"
y = "sangat"
z = "keren"
print(x, y, z)
```

Anda juga dapat menggunakan operator `+` untuk mengeluarkan beberapa variabel:
Contoh:

```py
x = "Python "
y = "sangat "
z = "keren"
print(x + y + z)
```

> Note : Perhatikan penulisan "Python " dan "sangat ". Masing-masing memiliki spasi dibelakagnya untuk memberi spasi untuk membuat kalimat yang memiliki spasi

Untuk penggunaan angka, karakter `+` berfungsi sebagai operator matematika.
Contoh:

```py
x = 5
y = 10
print(x+y)
```

Dalam fungsi `print()` tersebut, saat Anda mecoba menggabungkan string dan angka dengan operator `+`, Python akan memberi anda pesan kesalahan.
Contoh salah:

```py
x = 5
y = "John"
print(x + y)
```

Cara terbaik untuk menampilkan beberapa variabel dalam `print()` adalah dengan memisahkanya dengan koma, yang bahkan mendukung tipe data yang berbeda.
Contoh:

```py
x = 5
y = "John"
print(x, y)
```


