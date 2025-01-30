# Sintaksis Python
## Menjalankan sintaks Python
Seperti yang kita pelajari di halaman sebelumnya, sintaks Python dapat dieksekusi dengan menulis langsung di Command Line:

```shell
>>> print("Hello, World!")
Hello, World!
```

Atau dengan membuat file python di server, menggunakan ekstensi file.py, dan menjalankanya di command line:

```shell
C:\Users\_Your Name_>python myfile.py
```
## Indentasi Python
Indentasi mengacu pada spasi di awal baris kode.

Sementara dalam bahasa pemrograman lain, indentasi dalam kode hanya untuk keterbacaan, indentasi dalam Python sangatlah penting.

Python menggunakan indentasi untuk menunjukan blok kode.
Contoh:
```py
if 5 > 2:
	print("Five is greater than two!")
```

Python akan memberi Anda pesan kesalahan jika anda melewatkan indentasi:
Contoh kesalahan sintaksis:
```py
if 5 > 2:
print("Five is greater than two!")
```

Jumlah spasi terserah Anda sebagai programmer, penggunaan yang paling umum adalah empat, tetapi minimal harus satu.
Contoh:
```py
if 5 > 2:
	print("Five is greater than two!")
if 5 > 2:
		print("Five is greater than two!")
```

Anda harus menggunakan jumlah spasi yang sama di blok kode yang sama, jika tidak maka Python akan memberi Anda kesalahan:
Contoh kesalahan sintaksis:
```py
if 5 > 2:  
 print("Five is greater than two!")  
        print("Five is greater than two!")
```
## Variabel Python
Dalam Python, variabel dibuat saat Anda menetapkan nilai padanya:
Contoh variabel dalam python:

```py
x = 5
y = "Hello World"
```

Python tidak memiliki perintah untuk mendeklarasikan variabel. Anda bisa mempelajari tentang variaebel dari python di bab terpisah.
## Komentar
Python memiliki kemampuan memberi komentar untuk tujuan dokumentasi dalam kode. Komentar dimulai dengan #, dan Python akan menampilkan sisa baris sebagai komentar.
Contoh komentar:

```py
#Ini adalah komentar
print("Hello, World!")
```