# Python - Lambda
Fungsi lambda adalah fungsi anonim kecil.

Fungsi lambda dapat mengambil sejumlah argumen, tetapi hanya dapat memiliki satu ekspresi.

## Sintaksis
```
lambda arguments : expression
```

Ekspresi dieksekusi dan hasilnya dikembalikan.

Contoh:
tambahkan 10 ke argumen `a`, dan kembalikan hasilnya:

```py
x = lambda a : a + 10
print(x(5))
```

Fungsi lambda dapat mengambil sejumlah argumen.

Contoh:
kalikan argumen `a` dengan argumen `b` dan kembalikan hasilnya:
```py
x = lambda a, b : a * b
print(x(5, 6))
```

Contoh:
Ringkas argumen `a`, `b`, dan `c` dan kembalikan hasilnya:
```py
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
```
## Mengapa menggunakan fungsi Lambda?
kekuatan lambda ditunjukan lebih baik saat Anda menggunakanya sebagai fungsi anonim di dalam fungsi lain.

Misalkan Anda memiliki definisi fungsi yang mengambil satu argumen, dan argumen tersebut akan dikalikan dengan angka yang tidak diketahui:

```py
def myfunc(n):
  return lambda a : a * n
```
Gunakan definisi fungsi tersebut untuk membuat fungsi yang selalu menggandakan angka yang Anda kirim.

Contoh:
```py
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```

Atau, gunakan definisi fungsi yang sama untuk membuat fungsi yang selalu *melipatgandakan* angka yang Anda kirim.

Contoh:
```py
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
```

Atau, gunakan definisi fungsi yang sama untuk membuat kedua fungsi, dalam program yang sama.

Contoh:
```py
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```

> Gunakan fungsi lambda ketika fungsi anonim diperlukan untuk jangka waktu yang singkat.