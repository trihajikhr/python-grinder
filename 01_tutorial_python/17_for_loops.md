# Python For Loops
## Perulangan Python for
Perulangan `for` digunakan untuk mengulang suatu rangkaian (bisa berupa list, tuple, dictionary, set, atau string).

Ini tidak seperti kata kunci `for` dalam bahasa pemrograman lain, dan bekerja lebih seperti metode iterator seperti yang ditemukan dalam bahasa pemrograman berorientasi objek lainya.

Dengan `for` loop kita dapat mengeksekusi serangkaian pernyataan, sekali untuk setiap item di dalam suatu list, tuple, set, dan seterusnya.

Contoh, cetak setiap buah dalam daftar buah:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

Perulangan `for` tidak memerlukan variabel pengindeksan untuk ditetapkan sebelumnya.
## Melakukan Perulangan Melalui String
Bahkan string adalah objek yang dapat diulang, mereka berisi serangkain karakter. Contoh, ulangi huruf-huruf dalam kata "banana":

```py
for x in "banana":
  print(x)
```

## Pernyataan Break
Dengan pernyataan `break` kita dapat menghentikan loop sebelum loop tersebut melewati semua item.

Contoh, keluar dari loop saat `x` "banana":

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

Contoh, keluar dari loop saat `x` "banana", tapi kali ini break terjadi sebelum print:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```

## Pernyataan continue
Dengan pernyataan `continue`, kita dapat menghentikan iterasi loop saat ini, dan melanjutkan dengan yang berikutnya:

Contoh, jangan cetak banana:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```

## Fungsi range()
Untuk mengulang serangkaian kode sejumlah kali tertentu, kita dapat menggunakan fungsi `range()`.

Fungsi `range()` mengembalikan serangkaian angka, dimulai dari 0 secara default, dan bertambah 1 (secara default), dan berakhir pada angka yang dittentukan.

Contoh, menggunakan fungsi range():

```py
for x in range(6):
  print(x)
```

> Perhatikan bahwa range(6) bukanlah nilai 0 sampai 6, tetapi nilai 0 sampai 5.

Fungsi `range()` secara default bernilai 0 sebagai nilai awal, namun ada kemungkinan untuk menentukan nilai awal dengan menambahkan parameter: `range(2, 6)`, yang berarti nilai dari 2 hingga 6 (tetapi tidak termasuk 6).

Contoh, menggunakan parameter awal:

```py
for x in range(2, 6):
	print(x)
```

Fungsi `range()` secara default akan menambah urutan sebesar 1, namun ada kemungkinan untuk menentukan nilai penambahan dengan menambahkan parameter ketiga: `range(2, 30, 3)`.

Contoh, tambahkan urutan dengan 3 (nilai default adalah 1):

```py
for x in range(2, 30, 3):
  print(x)
```

## Else in For Loop
Kata kunci `else` dalam `for` loop menentukan blok kode yang akan dieksekusi ketika loop selesai.

Contoh, cetak semua angka dari 0 hingga 5, dan cetak pesan ketika loop telah berakhir:

```py
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

> Note : Blok `else`TIDAK akan dieksekusi jika loop dihentikan oleh suatu pernyataan `break`.

Contoh, putuskan loop ketika `x` nilainya 3, dan lihat apa yang terjadi dengan blok `else`:

```py
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
```

## Nested Loop
Perulangan bersarang merupakan perlangan yang ada didalam perulangan.

"Loo dalam" akan dieksekusi satu kali untuk setiap iterasi "loop luar".

Contoh, cetak setiap kata sifat untuk setiap buah:

```py
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```

## Pernyataan Pass
Perulangan `for` loop tidak boleh kosong, tetapi jika karena asalah tertentu Anda memiliki `for` loop tanpa konten, masukan pernyataan `pass` untuk menghindari kesalahan.

Contoh:

```py
for x in [0, 1, 2]:
  pass
```