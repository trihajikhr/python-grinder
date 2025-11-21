---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Tipe Data String dalam Bahasa Python
sumber:
  - duniailkom
date_learned: 2025-10-03T17:06:00
tags:
  - python
---
Link Sumber: [Tutorial Belajar Python Part 9: Tipe Data String dalam Bahasa Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-string-dalam-bahasa-python/)

---
# Tipe Data String dalam Bahasa Python

Pada lanjutan tutorial belajar bahasa pemrograman Python di Duniailkom kali ini kita akan membahas [Tipe Data String dalam Bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-string-dalam-bahasa-python/).

## 1 | Pengertian Tipe Data String

Tipe data string adalah tipe data untuk menampung data teks, seperti **"Duniailkom"**, **"Indonesia"**, atau **"Saya sedang belajar bahasa Python"**.

Bahasa Python tidak membatasi jumlah karakter yang ada di dalam string, tapi lebih ke batasan maksimum memory. Jika kita menggunakan interpreter **Python 32-bit** maksimum karakter adalah sekitar 2 atau 3 milyar karakter (2 – 3GB). Jika menggunakan interpreter **Python 64-bit**, maka maksimum jumlah karakter menjadi sekitar 63 milyar (63GB). Batasan ini sudah lebih dari cukup.

---
## 2 | Cara Pembuatan Tipe Data String Python

Di dalam bahasa Python, terdapat 3 cara untuk membuat tipe data string:

- Menggunakan tanda kutip satu ( ' )
- Menggunakan tanda kutip dua ( " )
- Menggunakan tanda kutip satu atau dua sebanyak 3 kali ( ' ' ' ) atau (" " ")

Cara pertama dan kedua tidak ada perbedaan mendasar dan kita bisa memilih ingin menggunakan yang mana saja.

```py
foo = "Duniailkom"
print(foo)
bar = 'Duniailkom'
print(bar)
```

Untuk menulis karakter khusus seperti tab atau pindah baris, bisa menggunakan **escape character**, yakni karakter _backslash_ ( \ ) dan diikuti dengan satu karakter khusus. Sebagai contoh, untuk menulis karakter 'tab' bisa dipakai **\t**, dan untuk membuat karakter _new line_ (pindah baris) bisa menggunakan tanda **\n**:

```py
foo = "Teks ini akan dipecah\nke dalam 2 baris"
print(foo)
foo = 'Teks ini\nakan dipecah\nke dalam 3 baris'
print(foo)
```

![[09-Tipe Data String dalam Bahasa Python-1.png]]

Cara pembuatan string menggunakan 3 kali tanda kutip dipakai untuk membuat **multiline string**, dimana teks yang diinput bisa tersambung ke beberapa baris


```py
foo = '''Teks ini
akan dipecah
ke dalam 3 baris'''
print(foo)
```

Hasil kode program python:

```
Teks ini
akan dipecah
ke dalam 3 baris
```

---
## 3 | Operasi Penyambungan String (string concatenation)


Salah satu operasi yang sering dipakai ke dalam tipe data string adalah proses penyambungan (string concatenation). Di dalam bahasa Python, operasi ini menggunakan karakter tambah ( + ). Berikut contohnya:

```py
foo = 'Belajar '
bar = "Bahasa Pemrograman Python "
baz = "di Duniailkom"
hasil = foo + bar + baz
print(hasil)
```

![[09-Tipe Data String dalam Bahasa Python-2.png]]

---
## 4 |  String Python sebagai Array

Mirip seperti kebanyakan bahasa pemrograman modern, tipe data string Python bisa diproses sebagai array dari karakter.

Secara sederhana, array adalah kumpulan tipe data yang saling terhubung. Dengan kata lain, sebuah string adalah huruf yang saling terhubung satu sama lain yang membentuk kata atau kalimat.

Misalkan variabel **foo** berisi string **'Duniailkom'**. Untuk merujuk ke huruf pertama dari variabel **foo**, kita bisa mengaksesnya dengan cara **foo[0]**. Angka 0 adalah nomor _index_ dari array. Untuk karakter kedua bisa diakses dari **foo[1]**, dst.

Berikut contoh pengaksesan huruf dari sebuah string:

```py
foo = 'Duniailkom'
print(foo[0])
print(foo[4])
print(foo[5:10])
```

Hasil kode program python:

```
D
a
ilkom
```
Khusus untuk perintah di baris terakhir, **foo[5:10]** bisa diartikan sebagai: "Ambil karakter dari string **foo** mulai dari index 5 sampai 10, tapi tidak termasuk karakter ke 10".

---

Dalam tutorial Python kali ini kita telah membahas tipe data **String**. Berikutnya akan dilanjutkan dengan [Tipe Data Number](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-number-dalam-bahasa-python/).
