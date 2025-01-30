# String Python
## String
String dalam python diapit oleh tanda kutip tunggal, atau tanda kutip ganda. Artinya 'halo' sama dengan "halo".

Anda dapat menampilkan literal dengan fungsi `print()`.
Contoh:

```py
print("Hello")
print('Hello')
```
## Kutipan didalam Kutipan
Anda dapat menggunakan tanda kutip didalam string, selama tanda kutip tersebut tidak cocok dengan tanda kutip yang ada di sekitar string tersebut:

```py
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

## Menetapkan String ke Variabel
Menetapkan string ke variabel dilakukan dengan nama variabel diikuti tanda sama dengan dan string:

```py
a = "Hello World!"
print(a)
```
## String multiline
Anda dapat menetapkan string multiline ke suatu variabel dengan menggunakan tida tanda kutip.
Contoh:

```py
a = """Apapun yang datang dengan cepat,
akan pergi dengan cepat. 
Jangan tertarik pada hasil yang instan,
tetapi pada sesuatu yang mampu bertahan lama, 
dan dapat dibanggakan."""
print(a)
```

Atau tiga tanda kutip tunggal:

```py
a = """Kecuali kita memiliki kekuatan,
untuk bertahan di gelapnya malam,
kita tidak akan,
melihat indahnya fajar!"""
print(a)
```

> Note : Pada saat di run, jeda baris disisipkan pada posisi yang sama seperti dalam kode.

## String adalah Array
Seperti banyak bahasa pemrograman populer lainya, string dalam Python adalah array byte yang mewakili karakter unicode.

Akan tetapi, python tidak memiliki tipe data karakter, karakter tunggal hanyalah string dengan panjang 1.

Tanda kurung siku dapat digunakan untuk mengakses elemen string.

Contoh, dapatkan karakter pada posisi 1 (ingat bahwa karakter pertama dimulai dari indek 0):

```py
a = "Hello World!"
print(a[1])
```
## Melakukan Perulangan melalui String
Karena string adalah array, kita dapat melakukan pengulangan melalui karakter-karakter dalam string, dengan sebuah for pengulangan.

Contoh, ulangi huruf-huruf dalam kata "banana":

```py
for x in "banana":
print(x)
```
## Panjang String
Untuk mendapatkan panjang string, gunakan fungsi `len()`.
Contoh, fungsi `len()` mengembalikan panjang string:

```py
a = "Hello World!"
print(len(a))
```
## Periksa String
Untuk memeriksa apakah frasa atau karakter tertentu hadir dalam suatu string, kita dapat menggunakan kata kunci `in`.

Contoh, periksa apakah kata `free` ada dalam teks:

```py
txt = "The best thngs in life are free!"
print("free" in txt)
```

Gunakan dalam sebuah pernyataan `if`.
Contoh, cetak hanya jika ada `free`:

```py
txt = "The best things in life are free!"
if "free" in txt:
	print("Yes, 'free' is present.")
```

Untuk materi if, atau percabangan, akan dipelajari di materi terpisah.
## Periksa not in
Untuk memeriksa apakah frasa atau karakter tertentu TIDAK ada dalam suatu string, kita dapat menggunakan kata kunci `not in`.

Contoh, periksa apakah "expensive" TIDAK ada dalam teks:

```py
txt = "The best things in life are free!"
print("expensive" not in txt)
```

Penggunaan dalam percabangan if:
Contoh, jika kata "expensive" tidak ada:

```py
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
```