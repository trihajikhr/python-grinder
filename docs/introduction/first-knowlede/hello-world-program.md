# Hello World Program

Tutorial ini akan mengajarkan cara menulis program **Hello World** sederhana menggunakan bahasa pemrograman Python. Program ini menggunakan fungsi bawaan Python, yaitu `print()`, untuk menampilkan sebuah string.

## Program Hello World dalam Python
Mencetak "Hello World" adalah program pertama dalam Python. Program ini tidak menerima input apa pun dari pengguna; program hanya menampilkan teks pada layar output. Program ini biasanya digunakan untuk memastikan bahwa perangkat lunak yang dibutuhkan untuk menjalankan program telah terpasang dengan benar.

## Langkah-Langkah

Berikut adalah langkah-langkah untuk menulis program Python yang mencetak **Hello World**:

- **Langkah 1:** Instal Python. Pastikan Python sudah terpasang di sistemmu. Jika belum, instal dari: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Langkah 2:** Pilih text editor atau IDE untuk menulis kode.
- **Langkah 3:** Buka text editor atau IDE, buat file baru, dan tulis kode untuk mencetak *Hello World*.
- **Langkah 4:** Simpan file dengan nama dan ekstensi **“.py”**.
- **Langkah 5:** Kompilasi/Jalankan program.

## Program Python untuk Mencetak Hello World

```python
# Python code to print "Hello World"
print("Hello World")
```

Dalam kode di atas, ada dua baris. Baris pertama adalah komentar Python yang akan diabaikan oleh interpreter. Baris kedua adalah pernyataan `print()` yang akan menampilkan pesan (“Hello World”) ke layar output.

Outputnya nanti adalah sebagai berikut:

```
Hello World
```

## Berbagai Cara Menulis dan Menjalankan Program Hello World

### 1. Menggunakan Mode Command Prompt Interpreter Python

Menampilkan pesan Hello World sangat mudah menggunakan interpreter Python. Jalankan interpreter dari terminal di Windows lalu ketik perintah berikut:

**Contoh (Windows):**

```
PS C:\> python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb 7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello World")
Hello World
```

Contoh serupa di Linux:

**Contoh (Linux):**

```
$ python3
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> print("Hello World")
Hello World
```

### 2. Menggunakan Mode Script Python

Interpreter Python juga bisa menjalankan kode dalam bentuk file. Tulis kode berikut di editor dan simpan sebagai **Hello.py**:

```python
print("Hello World")
```

#### Menjalankan di Windows

Buka CMD dan jalankan:

```
C:\>python hello.py
```

Output:

```
Hello World
```

#### Menjalankan di Linux

```
$ python3 hello.py
```

Output:

```
Hello World
```

### 3. Menggunakan Shebang `#!` dalam Script Linux

Di Linux, kamu bisa membuat program Python menjadi script yang bisa dieksekusi langsung. Baris pertama file harus diawali *shebang* `#!` yang berisi path menuju interpreter Python. Biasanya Python ada di `/usr/bin/python3`.

Tambahkan ini di baris pertama `hello.py`:

```
#!/usr/bin/python3

print("Hello World")
```

Beri izin eksekusi pada file tersebut dengan:

```
$ chmod +x hello.py
```

Lalu jalankan:

```
$ ./hello.py
```

Output:

```
Hello World
```

## FAQ

**1. Kenapa program pertama disebut Hello World?**

Itu hanyalah program sederhana untuk menguji sintaks dasar dan memastikan konfigurasi compiler/interpreter Python berjalan dengan benar.

**2. Apakah instalasi Python diperlukan untuk menjalankan program Hello World?**

Ya. Kamu harus menginstal Python untuk menjalankan program Hello World.

**3. Bagaimana cara menjalankan program Python tanpa menginstalnya?**

Ada banyak web yang menyediakan python compiler, jadi kamu bisa mencoba secara langsung salah satu web.

**4. Apa perbedaan antara First Program dan Hello World Program dalam Python?**

Tidak ada perbedaan. Program pertama dalam Python biasanya memang disebut program Hello World.

**5. Metode apa saja yang bisa digunakan untuk mencetak Hello World atau pesan lainnya?**

Kamu bisa menggunakan:

* Metode `print()`
* `sys.stdout.write()` (setelah mengimpor modul `sys`)
* Menggunakan *f-string* Python
