---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Tipe Data Number dalam Bahasa Python
sumber:
  - duniailkom
date_learned: 2025-10-03T17:11:00
tags:
  - python
---
Link Sumber: [Tutorial Belajar Python Part 10: Tipe Data Number dalam Bahasa Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-number-dalam-bahasa-python/)

---
# Tipe Data Number dalam Bahasa Python

Dalam tutorial sebelumnya kita telah membahas tentang T[ipe Data String](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-string-dalam-bahasa-python/) di dalam bahasa pemrograman **Python**. Kali ini akan dilanjutkan dengan [Tipe Data Number dalam Bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-number-dalam-bahasa-python/).

## 1 | Pengertian Tipe Data Number Python

Dalam bahasa **Python**, tipe data number terdiri dari 3 jenis:

- **Integer (int)**: Tipe data bilangan bulat, seperti 1, 300, 59000000
- **Float**: Tipe data bilangan desimal / pecahan, seperti 0.43, 0.0002, 999.99
- **Complex Number**: Tipe data bilangan kompleks atau bilangan imajiner, seperti 5j, 54j, 1j

Dari ketiga tipe data ini, tipe data **Complex Number** adalah tipe data yang cukup unik dan jarang tersedia di bahasa pemrograman lain.

Dalam teori matematika, _complex number_ atau _bilangan kompleks_ atau _bilangan imajiner_ adalah sebutan untuk angka yang mengandung nilai akar kuadrat dari -1. Angka akar kuadrat dari -1 ini ditulis dalam Python dengan huruf j. Bilangan 5j sama artinya dengan $5 \sqrt{-1}$.

---
## 2 | Cara Penggunaan Tipe Data Number Python

Sama seperti tipe data lain di dalam Python, kita bisa langsung menginput angka-angka ini ke dalam sebuah variabel. Berikut contohnya:

```py
foo = 100
bar = 30.23
baz = 4j
 
print(foo)
print(bar)
print(baz)
```

Hasil kode program python:

```
100
30.23
4j
```
Untuk memeriksa tipe data dari sebuah variabel, terdapat function **type()** bawaan Python. Berikut contoh penggunaannya:

```py
foo = 100
bar = 30.23
baz = 4j
  
print(type(foo))
print(type(bar))
print(type(baz))
```

Hasil kode program python:

```py
<class 'int'>
<class 'float'>
<class 'complex'>
```

Dari hasil ini bisa terlihat bahwa variabel **foo** yang berisi angka **100** merupakan tipe data **int**. Variabel **bar** yang berisi angka **30.23** merupakan tipe data **float**, dan variabel **baz** yang diisi dengan angka **4j** merupakan tipe data **complex**.

---
## 3 | Nilai Maksimum untuk Tipe Data Number

Yang juga cukup unik di dalam bahasa Python, nilai maksimum **integer** (angka bulat) hanya dibatasi dengan jumlah memory. Berikut percobaannya:


```py
foo = 999
bar = -99999
baz = 99999999999999999999
 
print(foo)
print(bar)
print(baz)
```


Hasil kode program python:

```py
999
-99999
99999999999999999999
```
Sebagai tambahan, di Python versi 2, terdapat tipe data **long** untuk menampung angka integer yang besar, tapi di dalam Python versi 3, tipe data **long** sudah tidak ada lagi dan digabung dengan tipe data **int** biasa.

Untuk tipe data **float**, nilai maksimumnya sama seperti tipe data **double** dalam bahasa **C** dan **C++**, yakni **1.7976931348623157e+308**.


---
## 4 | Penulisan Notasi Ilmiah (Scientific Notation)

Untuk tipe data **float**, kita bisa menulisnya menggunakan **notasi ilmiah** atau dalam bahasa inggris disebut sebagai **scientific notation**.

Dalam matematika, notasi ilmiah harus dinyatakan dalam 1 angka di depan koma. Angka **125** jika kita tulis dalam bentuk notasi ilmiah menjadi $1,25 \times 10^2$.

Di dalam bahasa Python (dan sebagian besar bahasa pemrograman lain), pangkat 10 ini diganti dengan huruf **e** atau **E**. Sebagai contoh $1,2 \times 10^2$ bisa ditulis sebagai **1.2e2** atau **1.2E2**. Berikut contoh penggunaannya:

```py
foo = 3e2
bar = 3e-2
baz = 1.34E5
  
print(foo)
print(bar)
print(baz)
```

Hasil kode program python:

```
300.0
0.03
134000.0
```

Perhatikan isi variabel **foo**. Disana saya menginput angka **3e2** yang berarti $3 \times 10^2$ atau angka **300**. Meskipun **300** ini terlihat seperti **integer**, namun karena ditulis menggunakan notasi ilmiah, maka akan dianggap sebagai tipe data **float**, yakni **300.0**.

---

Dalam tutorial kali ini kita telah membahas 3 jenis tipe data number dalam bahasa Python, yakni **integer**, **float** dan **complex number**. Berikutnya akan dilanjutkan dengan [Tipe Data Boolean dalam Bahasa Pemrograman Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-boolean-dalam-bahasa-python/).