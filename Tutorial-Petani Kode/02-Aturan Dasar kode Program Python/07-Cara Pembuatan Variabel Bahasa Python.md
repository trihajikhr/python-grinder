---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Cara Pembuatan Variabel Bahasa Python
sumber:
  - duniailkom
date_learned: 2025-10-03T16:53:00
tags:
  - python
---
Link Sumber: [Cara Pembuatan Variabel Bahasa Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-cara-pembuatan-variabel-bahasa-python/)

---
# Cara Pembuatan Variabel Bahasa Python

Dalam tutorial belajar bahasa pemrograman python sebelumnya telah dibahas [Aturan Dasar Penulisan Kode Program Python](https://www.duniailkom.com/tutorial-belajar-python-aturan-dasar-penulisan-kode-program-python/). Pada tutorial kali ini kita akan mempelajari [Cara Pembuatan Variabel di dalam Bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-cara-pembuatan-variabel-bahasa-python/).

## 1 | Pengertian Variabel

Di dalam dunia pemrograman, **variabel** adalah 'penanda' identitas yang digunakan untuk menampung suatu nilai. Nilai tersebut dapat diubah sepanjang kode program. Bisa diibaratkan bahwa variabel ini seperti lemari penyimpanan yang bisa diisi dengan berbagai data, dan isi lemari bisa ditukar jika diperlukan.

Secara teknis, variabel merujuk kepada suatu alamat di memory komputer. Setiap variabel memiliki nama yang dipakai sebagai identitas untuk variabel tersebut.

---
## 2 | Cara Pembuatan Variabel dalam Bahasa Python

Kesederhanaan kembali terlihat di dalam bahasa Python, dimana kita tidak perlu mendeklarasikan variabel untuk bisa menggunakannya.

Dalam bahasa Python, variabel bisa langsung ditulis pada saat akan digunakan. Untuk memberi nilai ke dalam sebuah variabel, gunakan tanda sama dengan ( = ), seperti contoh berikut:

```py
website = "Duniailkom"
harga = 20000
sukses = True
```

Di baris pertama, saya membuat variabel dengan nama **website** dan memberinya nilai **"Duniailkom"**. Di baris kedua saya membuat variabel **nilai** dan mengisinya dengan angka **20000**. Di baris ketiga saya membuat variabel **sukses** dan menginput nilai **True**.

Operasi pemberian nilai ke dalam sebuah variabel ini disebut juga sebagai **operasi assignment**, dan berlangsung dari kanan ke kiri. Maksudnya, kode **website = "Duniailkom"** adalah proses pemberian nilai **"Duniailkom"** ke dalam variabel **website**.

---
## 3 | Cara Menampilkan Variabel dalam Bahasa Python

Untuk menampilkan variabel dalam bahasa Python, kita bisa menggunakan perintah **print**, lalu menulis nama variabel di dalam tanda kurung seperti contoh berikut:

```py
ebsite = "Duniailkom"
print(website)
harga = 20000
print(harga)
sukses = True
print(sukses)
```

![[07-Cara Pembuatan Variabel Bahasa Python-1.png]]


Dalam kode ini saya membuat 3 buah variabel, mengisinya dengan sebuah nilai, dan menampilkannya menggunakan perintah **print**.

---

## 4 | Mengubah Nilai Variabel dalam Bahasa Python

Sepanjang penulisan program, nilai dari sebuah variabel bisa ditimpa dengan nilai lain. Berikut contohnya:

```py
website = "Duniailkom"
print(website)
website = "Python"
print(website)
website = "Google"
print(website)
```
![[07-Cara Pembuatan Variabel Bahasa Python-2.png]]


Disini saya membuat variabel **website** yang nilai awalnya berupa teks **"Duniailkom"**, lalu ditimpa menjadi **"Python"** di baris ketiga, dan kembali ditimpa menjadi **"Google"** di baris kelima.

Variabel di dalam Python tidak terbatas untuk dalam satu tipe saja. Sebuah variabel bisa diisi dengan berbagai tipe data, mulai dari teks (_string_), angka (_number_), dan berbagai tipe data lain. Berikut percobaannya:

```py
foo = "Belajar Python di Duniailkom"
print(foo)
foo = 350.25
print(foo)
foo = False
print(foo)
```

![[07-Cara Pembuatan Variabel Bahasa Python-3.png]]


Kali ini saya membuat sebuah variabel **foo** yang diisi teks **"Belajar Python di Duniailkom"** (baris 1). Kemudian nilai variabel **foo** ditimpa dengan angka **350.25** (baris 3). Terakhir nilai variabel **foo** kembali ditimpa menjadi **False** (baris 5).

Sepanjang kode program di atas, isi variabel **foo** sudah berubah dari tipe data **string** (teks), **number** (angka) dan **boolean** (True / False). Semua ini bisa dilakukan pada bahasa pemrograman Python.

Dalam bahasa pemrograman dasar lain seperti **Pascal**, **C** dan **C++**, setiap variabel harus di deklarasikan akan bertipe apa dan hanya bisa diisi dengan tipe data tersebut sepanjang kode program (tidak bisa ditimpa antar tipe data). Dalam ketiga bahasa ini, jika variabel **foo** didefinisikan sebagai variabel angka (_integer_), maka hanya bisa diisi angka saja, tidak bisa diisi dengan teks (string) atau tipe data lain.


---

## 5 | Aturan Penamaan Variabel dalam Bahasa Python

Dalam bahasa pemrograman, terdapat beberapa aturan pembuatan nama variabel, dan ini juga berlaku di dalam bahasa pemrograman Python:

- Variabel bisa terdiri dari huruf, angka dan karakter underscore / garis bawah ( _ ).
- Karakter pertama dari variabel hanya boleh berupa huruf dan underscore ( _ ), tidak bisa berupa angka. Namun variabel yang diawali dengan karakter underscore bisa bermakna khusus di dalam Python.
- Variabel harus selain dari _keyword_. Sebagai contoh, kita tidak bisa memakai kata **continue** sebagai nama variabel, karena **continue** merupakan keyword atau perintah khusus dalam bahasa Python.

Secara teknis, aturan penamaan variabel merujuk ke aturan penamaan _identifier_. **Identifier** adalah sebutan untuk "nama sesuatu" yang ditulis oleh programmer. Dan aturan di atas tidak hanya berlaku untuk nama variabel saja, tapi juga untuk nama function, nama class, nama object yang semuanya termasuk identifier.

---
## 6 | Konstanta Dalam Bahasa Python?

Yang cukup unik, bahasa Python tidak mengenal adanya **konstanta**, yakni variabel yang nilainya tidak bisa diubah sepanjang kode program.

Untuk mengatasi hal ini, kesepakatan programmer Python adalah dengan membuat nama variabel dalam huruf besar untuk menandakan sebuah konstanta, seperti kode program berikut:

```py
PI = 3.14
BULAN_1 = "Januari"
NAMA_WEBSITE = "Duniailkom"
```

Sebenarnya ini tidak lain membuat 3 buah variabel. Hanya saja karena nama variabel ini ditulis dalam huruf besar semua, sebagian besar programmer Python akan menganggapnya sebagai konstanta.

---

Dalam lanjutan tutorial belajar bahasa pemrograman Python di Duniailkom kali ini kita telah membahas cara pembuatan variabel. Berikutnya akan dibahas tentang [jenis-jenis tipe data dalam bahasa pemrograman Python](https://www.duniailkom.com/tutorial-belajar-python-jenis-jenis-tipe-data-dalam-bahasa-python/).
