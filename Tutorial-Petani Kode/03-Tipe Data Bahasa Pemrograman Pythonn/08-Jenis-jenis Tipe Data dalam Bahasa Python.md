---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Jenis-jenis Tipe Data dalam Bahasa Python
sumber:
  - duniailkom
date_learned: 2025-10-03T17:03:00
tags:
  - python
---
Link Sumber: [Jenis-jenis Tipe Data dalam Bahasa Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-jenis-jenis-tipe-data-dalam-bahasa-python/)

---
# Jenis-jenis Tipe Data dalam Bahasa Python

**Data** bisa disebut sebagai inti dari setiap program. Program itu sendiri tidak lain memproses data input untuk menghasilkan data output. Dan untuk bisa memproses itu semua, bahasa pemrograman butuh **tipe data**.

Dalam tutorial belajar bahasa pemrograman Python kali ini kita akan membahas sekilas tentang [Jenis-jenis Tipe Data dalam Bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-jenis-jenis-tipe-data-dalam-bahasa-python/). Untuk penjelasan lebih rinci akan dibahas satu per satu mulai dari tutorial berikutnya.

## 1 | Pengertian Tipe Data

Sebelum sampai ke jenis-jenis tipe data di dalam bahasa **Python**, ada baiknya kita membahas sedikit pengertian dari tipe data itu sendiri. **Apa itu tipe data?**

Mengutip dari wikipedia ([Data type](https://en.wikipedia.org/wiki/Data_type)):

_"A data type or simply type is a classification of data which tells the compiler or interpreter how the programmer intends to use the data"._

Terjemahannya:

_"Tipe data atau kadang disingkat dengan 'tipe' saja adalah sebuah pengelompokan data untuk memberitahu compiler atau interpreter bagaimana programmer ingin mengolah data tersebut"_

Secara sederhana, **tipe data adalah cara kita memberitahu komputer untuk mengelompokkan data berdasarkan apa yang dipahami oleh komputer**.

Sebagai contoh, misalkan saya memiliki data berupa angka. Agar bisa dipahami oleh _interpreter_ bahasa Python, data ini disimpan ke dalam variabel. Nantinya variabel ini akan diproses sesuai dengan tipe data angka, misalnya bisa ditambah, dikurangi, dibagi, dst. Jika ternyata variabel tersebut berisi teks (_string_), maka operasi penambahan tidak bisa dilakukan. Setiap jenis tipe data akan memiliki sifat dan fitur masing-masing.

---
## 2 | Jenis-jenis Tipe Data dalam Bahasa Python


Dalam bahasa pemrograman Python, terdapat 9 tipe data dasar:

- **String**
- **Integer**
- **Float**
- **Complex Number**
- **Boolean**
- **List**
- **Tuple**
- **Set**
- **Dictionary**

Pembagian 9 jenis tipe data di atas tidak mutlak, karena banyak referensi yang menggabungkan tipe data **Integer**, **Float** dan **Complex Number** sebagai satu tipe data saja, yakni tipe data **Number**. Jika dibuat seperti ini maka jenis tipe data python menjadi 7 jenis tipe data.

Penjelasan lebih lanjut tentang masing-masing tipe data ini akan kita bahas satu persatu mulai dari tutorial berikutnya. Namun saya akan tampilkan kode program singkat dari penggunaan ke 9 jenis tipe data ini:

```py
#Tipe Data String
foo = "Belajar Python di Duniailkom"
print(foo)
 
#Tipe Data Integer
foo = 1500
print(foo)
 
#Tipe Data Float
foo = 99.123
print(foo)
 
#Tipe Data Complex Number
foo = 4j
print(foo)
 
#Tipe Data Boolean
foo = True
print(foo)
 
#Tipe Data List
foo = ["satu","dua","tiga","satu"]
print(foo)
 
#Tipe Data Tuple
foo = ("satu","dua","tiga","satu")
print(foo)
 
#Tipe Data Set
foo = {"satu","dua","tiga","empat"}
print(foo)
 
#Tipe Data Dictionary
foo = {"satu":1, "dua":2.13, "tiga":"a", "empat": True}
print(foo)
```

Hasil kode program:

![[08-Jenis-jenis Tipe Data dalam Bahasa Python-1.png]]

Kita akan bahas satu per satu tipe data dalam bahasa Python ini. Yang akan dimulai dari tipe data string terlebih dahulu: [Tipe Data String dalam Bahasa Python](https://www.duniailkom.com/tutorial-belajar-python-tipe-data-string-dalam-bahasa-python/).
