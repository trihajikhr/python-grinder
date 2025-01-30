# Variabel Python - Menetapkan Beberapa Nilai
## Banyak Nilai ke Beberapa Variabel
Python memungkinkan Anda menetapkan nilai ke beberapa variabel dalam satu baris:

```py
x, y, z = "Jeruk", "Pisang", "Ceri"
print(x)
print(y)
print(z)
```

> Note : Pastikan jumlah variabel sesuai dengan jumlah nilai, atau Anda akan mendapatkan peringatan kesalahan!

## Satu Nilai ke Beberapa Variabel
Dan Anda dapat menetapkan nilai *yang sama* ke beberapa variabel dalam satu baris:

```py
x = y = z = "Jeruk"
print(x)
print(y)
print(z)
```
## Unpacking
Jika anda memiliki kumpulan nilai dalam daftar, tuple, dsb, python memungkinkan Anda untuk mengekstrak nilai ke dalam variabel. Ini disebut *unpacking*.
Contoh:

```py
fruits = ["apel","pisang","ceri"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

---
Untuk pemahaman lebih lanjut tentang unpacking, akan dipelajari di tutorial terpisah.
