# Angka Python
## Angka Python
Ada tiga tipe numberik dalam Python:
- `int`
- `float`
- `complex`

Variabel bertipe numerik dibuat saat Anda menetapkan nilai padanya.
Contoh:

```py
x = 1 #int
y = 2.8 #float
z = 1j #complex
```

Untuk memverifikasi jenis objek apapun di Python, gunakan fungsi `type()`.
Contoh:

```py
print(type(x))
print(type(y))
print(type(z))
```

## Int
Int, atau integer, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tidak terbatas. 
Contoh bilangan bulat:

```py
x = 1;
y = 87656789876543
z = -98765456

print(type(x))
print(type(y))
print(type(z))
```

## Float
Float, atau "floating point number" adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal.
Contoh:

```py
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Float juga bisa berpa angka ilmiah dengan "e" untuk menunjukan pangkat 10.
Contoh:

```py
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)
```

## Complex
Angka complex dilutis dengan "j" sebagai bagian imajiner.
Contoh:

```py
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

## Konversi Tipe
Anda  dapat mengonversi dari satu tipe ke tipe lain dengan metode `int()`, `float()`, dan `complex()`.
Contoh konversi dari satu tipe ke tipe lainya:

```py
x = 1    #int
y = 2.8  #float
z = 1j   #complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> Note : Anda tidak dapat mengubah bilangan kompleks menjadi jenis bilangan lainya.
## Angka Acak
Python tidak memiliki fungsi `random()` untuk membuat angka acak, tetapi python memiliki modul bawaan yang disebut `random` yang dapat digunakan untuk membuat angka acak.
Contoh, impor modul acak, dan tampilkan angka acak antara 1 dan 9:

```py
import random

print(random.randrange(1, 10))
```

Dalam tutorial terpisah, akan kita pelajari penggunaan fungsi modul ini.
