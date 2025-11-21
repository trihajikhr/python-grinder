---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: 5 Aturan Penulisan Sintaks Python yang Harus dipatuhi
sumber:
  - Petani Kode
date_learned: 2025-07-24T18:15:00
tags:
  - python-tutorial
---
Link Sumber: 


```cardlink
url: https://www.petanikode.com/python-sintaks/
title: "5 Aturan Penulisan Sintaks Python yang Harus dipatuhi"
description: "Ada beberapa aturan dasar penulisan sintaks Python yang harus dipatuhi agar tidak terjadi error dan kode tersusun rapi"
host: www.petanikode.com
favicon: https://www.petanikode.com/images/icon_hu5404421105932717208.png
image: https://www.petanikode.com/img/python/python.png
```


---
# 5 Aturan Penulisan Sintaks Python yang Harus dipatuhi
Setelah mempersiapkan segala [perlengkapan untuk _coding_ python](https://www.petanikode.com/python-linux) dan mengetahui cara membuat program python, selanjutnya mari kita pelajari tentang aturan-aturan penulisan sintaks Python yang harus dipatuhi.

“Bagaimana kalau tidak dipatuhi?”

Resikonya bisa terjadi error 😄.

Pada artikel ini, saya akan membahas beberapa aturan dasar penulisan sintaks Python yang harus diketahui.

Agar nanti mudah dalam menulis program.

Apa saja aturan-aturannya?

Silakan di simak..

## 1. Penulisan Statement Python

Statement adalah sebuah instruksi atau kalimat perintah yang akan dieksekusi oleh komputer.

Contoh:

```python
print("Hello World!")
print("Belajar Python dari Nol")
nama = "petani kode"
```

Penulisan satu statement tidak diakhiri dengan tanda titik-koma.

Sedangkan, bila kita ingin menulis lebih dari satu statement dalam satu baris, maka kita harus memisahnya dengan titik-koma.

Contoh:

```python
print("Hello"); print("World"); print("Tutorial Python untuk Pemula")
nama_depan = "petani"; nama_belakang = "kode"
```

Tapi…

Menurut beberapa _style guide_ python, tidak dianjurkan menulis lebih dari satu statement dalam satu baris. Karena akan sulit dibaca.

## 2. Penulisan String pada Python

String adalah teks atau kumpulan dari karakter.

String dalam pemrograman biasanya ditulis dengan dibungkus menggunakan tanda petik.

Bisa menggunakan tanda petik tunggal maupun ganda.

Contoh:

```python
judul = "Belajar Pemrograman Python sampai Bisa"
penulis = 'Petani Kode'
```

Atau kita juga bisa menggunakan triple tanda petik.

Contoh:

```python
judul = """Belajar Python dengan Cepat"""
penulis = '''Petani Kode'''
```

## 3. Penuilsan Case pada Python

Sintak Python bersifat _case sensitive_, artinya `teksini` dengan `TeksIni` dibedakan.

Contoh:

```python
judul = "Belajar Dasa-dasar Python"
Judul = "Belajar Membuat Program Python"
```

Antara variabel `judul` dengan `Judul` itu dibedakan…

### Case Style

Menurut rekomendasi [_style guide_ Google](https://google.github.io/styleguide/pyguide.html), berikut ini contoh penulisan _case_ yang disarankan:

```python
## Snake Case digunakan pada:
module_name, package_name, method_name, function_name, , global_var_name, instance_var_name, function_parameter_name, local_var_name.

## CamelCase digunakan Pada:
ClassName, ExceptionName

## ALL CAPS digunakan Pada:
GLOBAL_CONSTANT_NAME
```

Baca juga: [4 Macam Gaya Penulisan Case dalam Pemrograman](https://www.petanikode.com/gaya-penulisan-case-dalam-pemrograman/)

## 4. Penulisan Blok Program Python

Blok program adalah kumpulan dari beberapa statement yang digabungkan dalam satu blok.

Penulisan blok program harus ditambahkan indentasi (tab atau spasi 2x/4x).

![[03-5 Aturan Penulisan Sintaks Python yang Harus dipatuhi-1.png]]

✔️ Contoh yang benar:

```python
# blok percabangan if
if username == 'petanikode':
    print("Selamat Datang Admin")
    print("Silakan ambil tempat duduk")

# blok percabangan for
for i in range(10):
    print i
```

❌ Contoh yang salah:

```python
# blok percabangan if
if username == 'petanikode':
print("Selamat Datang Admin")
print("Silakan ambil tempat duduk")

# blok percabangan for
for i in range(10):
print i
```

Ada beberapa macam blok program:

- [Blok Percabangan](https://www.petanikode.com/python-percabangan)
- [Blok Perulangan](https://www.petanikode.com/python-perulangan)
- [Blok Fungsi](https://www.petanikode.com/python-fungsi/)
- Blok Class
- Blok Exception
- Blok With

## 5. Cara Penulisan Komentar pada Python

Komentar merupakan baris kode yang tidak akan dieksekusi.

Komentar digunakan untuk memberikan informasi tambahan dan untuk menonaktifkan kode.

Ada beberapa cara menulis komentar pada pemrograman Python.

### Menggunakan Tanda Pagar (`#`)

Cara pertama menggunakan tanda pagar (`#`).

Cara ini paling sering digunakan.

Contohnya:

```python
# ini adalah komentar
# Ini juga komentar
```

### Menggunakan Tanda Petik

Selain untuk mengapit teks (_string_), tanda petik juga dapat digunakan untuk membuat komentar.

Contoh:

```python
"Ini adalah komentar dengan tanda petik ganda"
'Ini juga komentar, tapi dengan tanda petik tunggal'
```

Penulisan komentar dengan tanda petik jarang digunakan, kebanyakan orang lebih memilih untuk menggunakan tanda pagar. Jadi…tidak direkomendasikan.

### Menggunakan Triple Tanda Petik

Sedangkan triple tanda petik, sering digunakan untuk menuliskan dokumentasi.

Contohnya:

```python
class Pagar:
    """kelas pagar untuk membuat objek pagar. Dibuat oleh Petani Kode sebagai contoh saja."""
    def __init__(self, warna, tinggi, bahan):
        self.warna = warna
        self.tinggi = tinggi
        self.bahan = bahan

# Mengakses dokumentasi kelas
print Pagar.__doc__
input('\ntekan [enter] untuk melihat bantuan (dokumentasi) kelas: ')
help(Pagar) # untuk melihat dokumentasi kelas
```

Hasilnya:

```bash
$ python kelas_pagar.py
kelas pagar untuk membuat objek pagar.
dibuat oleh Petani Kode
sebagai contoh saja.

tekan [enter] untuk melihat bantuan (dokumentasi) kelas:
```

Setelah _Enter_ ditekan

```bash
Help on class Pagar in module main:
class Pagar
| kelas pagar untuk membuat objek pagar.
| dibuat oleh Petani Kode
| sebagai contoh saja.
|
| Methods defined here:
|
| __init__(self, warna, tinggi, bahan)
(END)
```

## Apa Selanjutnya?

Itulah beberapa aturan dasar penulisan sintaks Python.

Selebihnya mungkin nanti kita akan pelajari atau bisa membaca beberapa _style guide_ seperti:

- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Python Style Guide Google](https://google.github.io/styleguide/pyguide.html)
- [Stanford Style Guide](https://nifty.stanford.edu/2010/zingaro-song-generator/rules.shtml)

Selanjutnya silakan pelajari tentang:

- [Variabel dan Tipe data pada Python](https://www.petanikode.com/python-variabel-dan-tipe-data)
- [Cara Mengambil Input dan Menampilkan Output di Python](https://www.petanikode.com/python-input-output/)
- [Operator pada Python](https://www.petanikode.com/python-operator)