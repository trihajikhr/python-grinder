# Nama Variabel
Suatu variabel dapat memiliki nama yang pendek, seperti (x dan y), atau nama yang lebih deskriptif (usia, total, jumlah, panjang, lebar, volume, etc). Aturan untuk penulisan nama variabel python:

- Nama variabel harus dimulai dengan huruf atau karakter garis bawah
- Nama variabel tidak dapat dimulai dengan angka
- Nama variabel hanya dapat berisi karakter alfanumetrik dan garis bawah (Az, 0-9, dan_)
- Nama variabel peka terhadap huruf besar kecil (age, Age, dan AGE adalah tiga variabel yang berbeda)
- Nama variabel tidak dapat berupa salah satu satu syntax python.

Contoh, nama variabel yang legal:

```py
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

Contoh, nama variabel yang ilegal atau salah:

```py
2myvar = "John" #karena diawali angka
my-var = "John" #menggunakan karakter -
my var = "John" #terdapat spasi 
```

> Ingat! Penamaan variabel peka terhadap huruf besar/kecil

## Nama variabel Multi Kata
Nama variabel dengan lebih dari satu kata dapat sulit dibaca. Ada beberapa teknik yang dapat Anda gunakan untuk membuatnya lebih mudah dibaca:
### camel case
Setiap kata, kecuali kata pertama, dimulai dengan huruf kapital:

```py
myVariableName = "John"
```
### pascal case
Setiap kata dimulai dengan huruf kapital:

```py
MyVariableName = "John"
```
### snake case
Setiap kata dipisahkan oleh karakter garis bawah:

```py
my_variable_name = "John"
```

