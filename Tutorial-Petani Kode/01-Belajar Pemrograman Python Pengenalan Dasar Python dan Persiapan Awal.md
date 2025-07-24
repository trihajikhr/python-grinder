---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: "Belajar Pemrograman Python: Pengenalan Dasar Python dan Persiapan Awal"
sumber:
  - Petani Kode
date_learned: 2025-07-24T17:42:00
tags:
  - python-tutorial
---
Link Sumber: 


```cardlink
url: https://www.petanikode.com/python-linux/
title: "Belajar Pemrograman Python: Pengenalan Dasar Python dan Persiapan Awal"
description: "Mau belajar bahasa pemrograman python, tapi masih bingung mulainya dari mana? Artikel ini akan membahasnya, dari pengenalan Python dan persiapan awalnya sampai tuntas."
host: www.petanikode.com
favicon: https://www.petanikode.com/images/icon_hu5404421105932717208.png
image: https://www.petanikode.com/img/python/python.png
```


---
# Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal

Mau belajar bahasa pemrograman python, tapi masih bingung mulainya dari mana?

Tenang…

Karena pada artikel ini, kita akan membahas persiapan awalnya sampai tuntas:

- Apa itu Python dan kenapa belajar Python?
- Apa saja alat-alat yang diperlukan untuk belajar python?
- Bagaimana cara membuat program python?
- Apa yang harus dipelajari selanjutnya?

Mari kita bahas semuanya…

## Apa itu Python?

Python merupakan bahasa pemrograman tingkat tinggi yang diracik oleh [Guido van Rossum](https://id.wikipedia.org/wiki/Guido_van_Rossum).

Python banyak digunakan untuk membuat berbagai macam program, seperti: program CLI, [Program GUI (desktop)](https://www.petanikode.com/kategori/desktop/), [Aplikasi Mobile](https://www.petanikode.com/kategori/mobile/), [Web](https://www.petanikode.com/kategori/web/), IoT, [Game](https://www.petanikode.com/kategori/game/), Program untuk Hacking, dsb.

Python juga dikenal dengan bahasa pemrograman yang mudah dipelajari, karena struktur sintaknya rapi dan mudah dipahami.

(Python bagus untuk pemula yang belum pernah _coding_)

### Kenapa belajar Python?

Pernah melihat meme ini?

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-1.png|500]]

Python memang sangat sederhana dibandingkan bahasa yang lainnya. Tidak perlu ini dan itu untuk membuat program [Hello World!](https://www.petanikode.com/sejarah-dan-asal-usul-hello-world/).

Bahkan tagline di websitenya menjelaskan, kalau python akan membuatmu bekerja lebih cepat dan efektif.

> _Python is a programming language that lets you work quickly and integrate systems more effectively_.

Jadi kenapa belajar Python?

1. Cepat dan efektif;
2. Mudah dipelajari;
3. Banyak digunakan di perusahaan besar;
4. Sekedar ingin tahu saja.
5. …(tambahkan sendiri)

## Persiapan Alat untuk Belajar Pemrograman Python

Apa saja alat-alat yang harus dipersiapkan untuk belajar pemrograman python?

1. **Python**: Interpreter yang menerjemahkan bahasa python ke bahasa mesin, sehingga program bisa dijalankan.
2. **Teks Editor/IDE**: Program yang digunakan untuk menulis kode.

### Bagaimana cara install Python?

Bagi pengguna Linux, Python tidak perlu diinstal. Karena Sebagian besar distro Linux sudah menyediakannya secara default.

Untuk mengeceknya, silakan ketik perintah `python --version` di terminal.

```bash
$ python --version
Python 2.7.12
```

Bagi pengguna Windows, silakan baca [Cara Install Python di Windows](https://www.petanikode.com/pemrograman-python-di-windows/).

### Python Versi 2 vs Python Versi 3

Ada dua versi Python yang beredar saat ini, yaitu versi 2 dan 3.

Apa perbedaannya?

Python versi 2 merupakan versi yang banyak digunakan saat ini, baik dilingkungan produksi dan pengembangan.

Sementara Python versi 3 adalah pengembangan lanjutan dari versi 2. Python 3 memiliki lebih banyak fitur dibandingkan Python 2.

Untuk membuka Python 2 kita hanya menggunakan perintah `python` saja, sedangkan Python 3 menggunakan perintah `python3`.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-2.png]]

Manakah yang harus saya pilih?

Untuk yang baru belajar saya sarankan menggunakan versi 2. Sementara untuk yang sudah mahir, bisa mencoba yang versi 3.

### Siapkan Teks Editor/IDE untuk Menulis Kode

Teks editor yang digunakan untuk menulis program python bisa apa saja. Bahkan Notepad pun bisa.

Pada Linux, banyak sekali pilihan teks editor yang bisa digunakan.

Silakan baca-baca di sini:

- [6 Teks Editor Berbasis Teks (CLI) di Linux untuk Menulis Kode](https://www.petanikode.com/teks-editor-cli-linux/)
- [[Review] Text Editor Visual Studio Code di Linux](https://www.petanikode.com/text-editor-vscode)

Selain teks editor, kita juga bisa menggunakan IDE _(Integrated Development Environment)_. Namun, nanti kita akan bahas belakangan.

Untuk saat ini kita pakai teks editor saja dulu, biar lebih paham konsep pemrograman.

## Mengenal Mode Interaktif Python

Mode interaktif merupakan fasilitas/fitur yang disediakan oleh Python sebagai tempat menulis kode secara interaktif.

Fitur ini dikenal juga dengan Shell, Console, REPL _(Read–Eval–Print Loop)_, interpreter, dsb.

Cara membuka mode interaktif adalah dengan mengetik perintah `python` pada terminal.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-3.png]]


> untuk keluar dari mode interaktif tekan `Ctrl`+`d` atau ketik perintah `exit()`.

Tanda `>>>`, artinya python siap menerima perintah.

Terdapat juga tanda `...` yang berarti _secondary prompt_ atau _sub prompt_, biasanya muncul saat membuat blok kode dan menulis perintah tunggal dalam beberapa baris.

Mari kita coba memberikan perintah `print`, perintah ini berfungsi untuk mencetak teks ke layar.

Cobalah tulis `print "Hello World"` kemudian tekan `Enter`.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-4.png]]

Perintah yang kita tulis langsung dieksekusi dan ditampilkan hasilnya.

Inilah mode interaktif, setiap kode atau perintah yang diketik akan direspon langsung oleh python.

Kita bisa memanfaatkan mode interaktif ini untuk:

- Uji coba suatu fungsi;
- Eksperimen modul tertentu;
- Kalkulator;
- Mencari bantuan tentang fungsi tertentu;
- dll.

Hal yang perlu kita coba adalah mencari bantuan tentang fungsi tertentu, karena akan membantu sekali dalam mempelajari python.

Ada dua fungsi yang digunakan untuk mencari bantuan:

1. fungsi `dir()` untuk melihat fungsi apa saja yang tersedia pada sebuah modul;
2. fungsi `help()` untuk membuka dokumentasi suatu fungsi.

Sebagai contoh, kita akan coba mencari tahu tentang penggunaan modul `math`.

Pertama kita impor dulu modulnya ke mode interaktif:

```python
>>> import math
```

Setelah itu kita bisa melihat-lihat, fungsi apa saja yang tersedia di modul tersebut.

```python
>>> dir(math)
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
```

Lalu, kita bisa cari tahu cara penggunaan fungsi-fungsi tersebut dengan `help()`.

Misalkan kita ingin cari tahu cara penggunaan fungsi `pow()`, maka kita harus memberikan perintah `help(math.pow)`.

```python
Help on built-in function pow in module math:

pow(...)
    pow(x, y)

    Return x**y (x to the power of y).
(END)
```

*untuk keluar dari dokumentasi tekan `q`

Setelah itu, baru kita bisa pakai dan coba fungsinya.

## Menulis Skrip Python

Program yang kita tulis dalam mode interaktif tidak akan disimpan. Setelah mode interaktif ditutup, program akan hilang.

Karena itu, kita harus membuat skrip.

Silakan gunakan teks editor untuk menulis skrip seperti di bawah ini.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-5.png]]

Setelah itu simpan dengan nama `hello_world.py`

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-6.png]]

Kemudian untuk menjalankan skripnya, gunakan perintah berikut:

```bash
python nama_skrip.py
```

Pastikan mengetik perintah tersebut pada direktori tempat menyimpan skripnya.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-7.png]]

## Alur Kerja Pembuatan Program Python

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-8.png]]

1. Membuat skrip python dengan teks _editor_.
2. Skrip python diterjemahkan ke dalam kode biner oleh (_interpreter_) python, sehingga komputer dapat mengerti arti perintah tersebut.
3. Komputer mengerjakan perintah tersebut.

Paham…?

Sampai tahap ini, kita sudah tahu cara membuat program Python.

Selanjutnya, kita akan belajar cara membuat program Python menggunakan IDE PyCharm.

## Pemrograman Python Menggunakan PyCharm

PyCharm merupakan IDE terbaik untuk pemrograman python. PyCharm dibuat oleh JetBrains.

Ada dua versi PyCharm:

1. Versi Profesional (_Trial_ 30 hari) – Memiliki fitur lebih banyak untuk pemrograman python dan web.
2. Versi Komunitas (Gratis dan _opensource_) – Fiturnya standar untuk pemrograman python.

Pada panduan ini, kita akan menggunakan PyCharm versi Komunitas.

### Instalasi PyCharm di Linux

Pertama, pastikan komputermu sudah terinstal JDK (Java Development Kit) atau JRE. Karena PyCharm terbuat dari Java dan dia membutuhkan JRE untuk berjalan.

Silakan baca [Cara Instal JDK dan JRE di Linux](https://www.petanikode.com/java-linux/#2-jdk-java-development-kit).

Setelah itu…

Silakan download PyCharm di [website JetBrains](https://www.jetbrains.com/pycharm/download/).

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-9.png]]

Pastikan men-download yang versi komunitas.

Setelah itu, ikuti langkah-langkah berikut untuk menginstalnya:

1. Buka File manager sebagai `root`.
   ![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-10.png]]

2. Cari File PyCharm yang sudah di-download tadi, kemudian ekstrak ke direktori `/opt`.
   
   ![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-11.png]]
   Pada gambar di atas, Saya menggunakan `F3` untuk memecah tampilan (tergantung dari file manager yang kamu gunakan).

3. Buka kembali File Manager sebagai user biasa. Kemudian masuk ke `/opt/pycharm-community-2017.1.2/bin` dan klik ganda pada file `pycharm.sh`, lalu pilih **run**.
   
   ![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-12.png]]
4. Tunggulah sebentar, maka akan terbuka jendela baru. Pilih **Don not import settings**, kemudian klik **OK**.
   ![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-13.png]]
5. Jendela sambutan akan terbuka, silakan centang _**“Enable opening file…”**_ agar perintah `charm` dikenali di terminal. Setelah itu klik **Ok**.
   
   ![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-14.png]]
   Masukkan Password bila diminta, setelah itu klik **OK**. Selesai… Coba periksa di menu, apakah sudah ada PyCharm atau tidak?

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-15.png]]


### Membuat Proyek Python di PyCharm

Untuk membuat proyek baru, kita bisa klik _“Create new Project”_ pada jendela sambutan _(welcome)_ PyCharm.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-16.png]]
Atau bisa juga dilakukan melalui menu **File**->**New Project**.

Setelah itu, kita akan diminta untuk mengisi nama proyeknya dan memilih versi Python yang akan digunakan.

Isi saja nama proyeknya dengan `hello-world` dan gunakan Python versi 2 (`python2.7`).

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-17.png]]

Maka kita akan langsung di bawah ke area kerja PyCharm.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-18.png]]

Selanjutnya, silakan tambahkan file python dengan klik kanan pada direktori proyek, kemudian pilih **New**->**Python File**.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-19.png]]


Setelah itu, berikan nama filenya dengan `program-pertama` dan klik Ok.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-20.png]]

Selanjutnya, silakan tulis kode program-nya.

```python
print "Hello dunia"
print "Selamat datang di pemrograman Python"
print "Saya belajar Python dengan PyCharm"
print "Salam, Petani Kode"
```

Kemudian buka menu **Run**->**Run…** atau tekan tombol `Alt`+`Shift`+`F10`. Kalau muncul pilihan, pilih saja `program-pertama`.

![[01-Belajar Pemrograman Python Pengenalan Dasar Python dan Persiapan Awal-21.png]]

Selamat…

Program pertama kita di PyCharm sudah berhasil dieksekusi.

Begitulah cara membuat program python menggunakan IDE PyCharm, lebih mudah bukan?

Kita tidak perlu membuka terminal untuk mengeksekusi programnya.

Mana yang menurutmu lebih enak?

## Apa Selanjutnya yang Harus dipelajari?

Kita sudah mengetahui cara memprogram Python di Linux baik menggunakan teks editor dan IDE Pycharm.

Silakan melakukan eksperimen sendiri agar semakin paham.

Kalau ada pertanyaan, silakan sampaikan melalui komentar!

Selanjutnya silakan pelajari tentang:

- [Aturan Penulisan Sintaks Python](https://www.petanikode.com/python-sintaks/)
- [Variabel dan Tipe Data dalam Python](https://www.petanikode.com/python-variabel-dan-tipe-data/)
- [Mengambil Input dan Teknik Menampilkan Output](https://www.petanikode.com/python-input-output/)

> 📖 untuk daftar tutorial lengkap Python, cek di [List Tutorial Python](https://www.petanikode.com/tutorial/python/)