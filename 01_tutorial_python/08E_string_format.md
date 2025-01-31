# Python Format String
## Format String
Seperti yang telah kita pelajari di bab Variabel Python, kita tidak dapat menggabungkan string dan angka seperti ini:

```py
age = 36
txt = "My name is John, I am " + age
print(txt)
```

Namun kita dapat menggabungkan string dan angka dengan menggunakan *f-string* atau fungsi `format()`
## F-String
F-String diperkenalkan dalam Python 3.6, dan sekarang menjadi cara yang disukai untuk memformat string.

Untuk menentukan suatu string sebagai f-string, cukup letakan sebuah `f` didepan literal string, dan tambahkan tanda kurung kurawal `{}` sebagai tempat penampung untuk variabel dan operasi lainya.

Contoh, buat f string:

```py
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```
## Placeholder dan Modifier
Placeholder dapat berisi variabel, operasi, fungsi, dan pengubah untuk memformat nilai.

Contoh, tambahkan placeholder untuk variabel `price`:

```py
price = 59
txt = f"The price is {price} dollars"
print(txt)
```

Placeholder dapat menyertakan *modifier* untuk memformat nilai.

Modifier disertakan dengan menambahkan titik dua `:` diikuti oleh jenis format legal, seperti `.2f` yang berarti angka titik tetap dengan 2 desimal.

Contoh, menampilkan harga dengan 2 desimla:

```py
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```

Maka hasilnya menjadi:

```shell
The price is 59.00 dollars
```

Placeholder dapat berisi kode Python, seperti operasi matematika.
Contoh, lakukan operasi matematika di placeholder, dan kembalikan hasilnya:

```py
txt = f"The price is {20 * 59} dollars"
print(txt)
```
