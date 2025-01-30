# Variabel Python
## Variabel
Variabel adalah wadah untuk menyimpan nilai data.
## Membuat variabel
Python tidak memiliki perintah untuk mendeklarasikan variabel. Suatu variabel tercipta pada saat pertama kali Anda menetapkan suatu nilai padanya.
Contoh:

```py
x = 5
y = "John"
print(x)
print(y)
```

Variabel tidak perlu dideklarasikan dengan tipe tertentu, dan bahkan dapat mengubah tipe setelah ditetapkan.
Contoh:

```py
x = 4 #tipe data angka
x = "Sally" #tipe data string
print(x)
```
## Casting
Jika anda ingin menentukan tipe data suatu variabel, ini dapat dilakukan dengan casting.
Contoh:

```py
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```
## Dapatkan tipenya
Anda bisa mendapatkan tipe data suatu variabel dengan fungsi `type()`
Contoh:

```py
x = 5
y = "John"
print(type(x))
print(type(y))
```

> Kita akan mempelajari tipe data dan casting dalam tutorial terpisah

## Tanda kutip tunggal dan ganda
Variabel string dapat dideklarasikan dengan menggunakan tanda kutip tunggal aatau ganda.
Contoh:

```py
x = "John"
# adalah sama dengan
x = 'John'
```
## Case sensitive
Nama variabel juga peka terhadap perbedaann huruf besar dan kecil.
Contoh, ini akan membuat dua variabel:

```py
a = 4
A = "Sally"
# A tidak akan menimpa a
```

