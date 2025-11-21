---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Tipe Data Boolean dalam Bahasa Python
sumber:
  - duniailkom
date_learned: 2025-10-03T17:17:00
tags:
  - python
---
Link Sumber: [Tutorial Belajar Python Part 11: Tipe Data Boolean dalam Bahasa Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-boolean-dalam-bahasa-python/)

---
# Tipe Data Boolean dalam Bahasa Python

Dari seluruh tipe data yang ada di dalam bahasa pemrograman Python, mungkin inilah tipe data yang paling sederhana, namun **Boolean** sangat penting dan selalu ada di setiap bahasa pemrograman komputer. Untuk lebih lanjut, kita akan bahas [Tipe Data Boolean dalam Bahasa Pemrograman Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-boolean-dalam-bahasa-python/).

---
## 1 | Pengertian Tipe Data Boolean Python

**Tipe data** **boolean** sebenarnya sangat _simple_. Tipe data ini hanya bisa diisi dengan salah satu dari 2 nilai: **True** atau **False**. Tipe data **boolean** banyak dipakai untuk percabangan kode program atau untuk memutuskan apa yang mesti dijalankan ketika sebuah kondisi terjadi.

Sebagai contoh, kita bisa membuat kode program untuk menentukan apakah sebuah angka genap atau ganjil berdasarkan input dari pengguna. Untuk keperluan ini kita harus mengecek terlebih dahulu apakah angka tersebut bisa dibagi 2 (untuk angka genap), atau tidak bisa dibagi 2 (untuk angka ganjil). Tipe data boolean bisa dipakai untuk menampung kondisi seperti ini, yakni benar atau salah (_True_ atau _False_).

Penggunaan tipe data boolean ini akan lebih jelas saat kita masuk ke kondisi percabangan program seperti IF (yang akan dibahas pada tutorial terpisah).

---
## 2 | Cara Penggunaan Tipe Data Boolean Python

Sebagaimana yang sudah dijelaskan sebelumnya, tipe data boolean hanya bisa diisi dengan 2 nilai, yakni salah satu dari **True** atau **False**. Berikut contoh penulisannya:

```py
foo = True
bar = False
  
print(foo)
print(bar)
```

Hasil kode program python:

```
True
False
```

Dalam kode program diatas, saya menginput nilai boolean **True** ke dalam variabel **foo** dan nilai boolean **False** ke dalam variabel **bar**.

Yang juga harus diperhatikan adalah penulisan huruf besar atau kecil. Dalam bahasa Python, penulisannya harus persis seperti itu, jika diinput sebagai **true** atau **TRUE**, akan menghasilkan error:

```py
foo = true
print(foo)
```

Hasil kode program python:

```
Traceback (most recent call last):
File "D:\belajar_python\latihan.py", line 1, in <module>
foo = true
NameError: name 'true' is not defined
```

Selain diinput manual, tipe data boolean lebih sering di dapat sebagai hasil dari operasi perbandingan, seperti apakah suatu angka lebih besar dari angka lainnya, apakah lebih kecil, atau sama dengan. Berikut contoh penggunaan operasi perbandingan ini:

```py
foo = 12 < 10
print(foo)
foo = 12 > 10
print(foo)
foo = "A" == "a"
print(foo)
```

Hasil kode program python:

```
False
True
False
```


Di baris pertama, saya menyimpan hasil operasi perbandingan 12 < 10 ke dalam variabel foo. Apakah 12 < 10? **Salah**. Sehingga nilai variabel **foo** akan berisi boolean **False**.

Di baris ketiga, operasi perbandingannya di balik, yakni apakah 12 > 10? **Benar**. Sehingga nilai variabel **foo** akan berisi boolean **True**.

Terakhir di baris kelima operasi perbandingannya adalah apakah **"A"** sama dengan **"a"**. Disini saya membandingkan antara dua buah string, namun karena **"A"** tidak sama dengan **"a"**, maka variabel **foo** akan berisi boolean **False**.


Hasil boolean dari operasi perbandingan ini juga bisa didapat tanpa harus menyimpannya ke dalam variabel, seperti contoh berikut:


```py
print(12 < 10)
print(12 > 10)
print("A" == "a")
```

Hasil kode program python:

```
False
True
False
```

Operasi perbandingan yang dipakai masih sama seperti sebelumnya, hanya saja kali ini langsung saya input ke dalam perintah print.

Lebih jauh lagi, metode perbandingan seperti ini sangat sering dipakai dalam struktur logika IF seperti contoh berikut:

```py
a = 12
b = 10
if (a < b):
  print("Isi variabel a lebih kecil daripada variabel b")
elif (a > b):
  print("Isi variabel a lebih besar daripada variabel b")
else:
  print("Isi variabel a sama dengan variabel b")
```

Hasil kode program python:

```
Isi variabel a lebih besar daripada variabel b
```

Pembahasan lebih lanjut tentang struktur IF ini akan kita bahas dalam tutorial tersendiri. Tapi bisa anda lihat bahwa operasi perbandingan yang menghasilkan nilai Boolean dipakai untuk menentukan perintah apa yang harus dijalankan. Dalam contoh diatas, operasi yang menghasilkan nilai **True** adalah **a > b**, sehingga hasil yang tampil adalah "**Isi variabel a lebih besar daripada variabel b**".

---

Dalam lanjutan tutorial belajar bahasa pemrograman Python kali ini kita telah membahas tentang pengertian tipe data **Boolean** beserta contoh penggunaannya. Berikutnya kita akan membahas [tipe data List dalam bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-list-dalam-bahasa-python/).






