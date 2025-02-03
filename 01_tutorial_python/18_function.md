# Python Function
Fungsi adalah blok kode yang hanya berjalan saat dipanggil. 

Anda dapat meneruskan data, yang dikenal sebagai parameter, ke dalam suatu fungsi.

Suatu fungsi dapat mengembalikan data sebagai hasil.
## Membuat Fungsi
Dalam Python, suatu fungsi didefinisikan menggunakan kata kunci `def`:

Contoh:

```py
def my_function():
	print("Hello form a funcction")
```

## Memanggil Fungsi
Untuk memanggil suatu fungsi, gunakan nama fungsi diikuti tanda kurung:

```py
def my_function():
	print("Hello from a function")

my_function()
```
## Argumen
Informasi dapat diterukan ke fungsi sebagai argumen.

Argumen ditentukan setelah nama fungsi, didalam tanda kurung. Anda dapat menambahkan argumen sebanyak yang ada inginkan, cukup pisahkan dengan koma.

Contoh berikut memiliki fungsi dengan satu argumen. Saat fungsi dipanggil, kami meneruskan nama depan, yang digunakan didalam fungsi untuk mencetak nama lengkap:

```py
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

> _Argumen_ sering disingkat menjadi _args_ dalam dokumentasi Python.

## Parameter atau Argumen?
Istilah *parameter* dan *argumen* dapat digunakan untuk hal yang sama:
Informasi yang diteruskan ke suatu fungsi.

Dari perspektif fungsi:

Parameter adalah variabel yang tercantum di dalam tanda kurung dalam definisi fungsi. Argumen adalah nilai yang dikirim ke fungsi saat dipanggil.
## Jumlah argumen
Secara default, suatu fungsi harus dipanggil dengan jumlah argumen yang benar. Artinya, jika fungsi Anda mengharapkan 2 argumen, Anda harus memanggil fungsi tersebut ddengan 2 argumen juga, tidak lebih, dan tidak kurang.

Contoh, fungsi ini mengharapkan 2 argumen, dan mendapatkan 2 argumen:

```py
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
```

Jika anda mencoba memanggil fungsi dengan 1 atau 3 argumen, maka Anda akan mendapatkan pesan kesalahan.

Contoh, fungsi ini mengharapkan 2 argumen, tetapi hanya mendapat 1:

```py
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
```
## Arbitrary Arguments, \*args
Jika Anda tidak tahu berapa banyak argumen yang akan dimasukan ke dalam fungsi Anda, tambahkan `*` sebelum nama parameter dalam definisi fungsi.

Dengan cara ini, fungsi akan menerima sejumlah argumen, dan dapat mengakses item yang sesuai.

Contoh, jika jumlah argumen tidak diketahui, tambahkan `*` sebelum nama parameter:

```py
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

> _Argumen Sembarangan_ sering disingkat menjadi _\*args_ dalam dokumentasi Python.

## Kata kunci Argumen
Anda juga dapat mengirim argumen dengan sintaksis *kunci = nilai*.

Dengan cara ini urutan argumen tidak menjadi masalah.

Contoh:

```py
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

> Frasa _Argumen Kata Kunci_ sering disingkat menjadi _kwargs_ dalam dokumentasi Python.

## Arbitrary Keyword Arguments, \*\*kwargs
Jika anda tidak tahu berapa banyak argumen kata kunci yang akan dimasukan kedalam fungsi Anda, tambahkan dua tanda bintang: `**` sebelum nama parameter dalam definisi fungsi.

Dengan cara ini fungsi akan menerika *dictionary* argumen, dan dapat mengakses item yang sesuai.

Contoh, jika jumlah argumen kata kunci tidak diketahui, tambahkan tanda bintang ganda `**` sebelum nama parameter:

```py
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

> _Argumen Kword Sembarangan_ sering disingkat menjadi _\*\*kwargs_ dalam dokumentasi Python.

## Nilai Parameter Default
Contoh berikut menunjukan cara menggunakan nilai parameter default.

Jika kita memanggil fungsi tanpa argumen, ia menggunakan nilai default. Contoh:

```py
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```

## Menggunakan list sebagai argumen
Anda dapat mengirim tipe data argumen apa pun ke suatu fungsi (string, int, list, dictionary, dll), dan itu akan diperlakukan sebagai tipe data yang sama didalam fungsi tersebut.

Misalnya jika Anda mengirim llist sebagai argumen, itu akan tetap menjadi list saat mencapai fungsi.

Contoh:

```py
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```
## return value
Untuk membiarkan suatu fungsi mengembalikan suatu nilai, gunakan pernyataan `return`:

Contoh:

```py
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```
## Pernyataan Pass
Definisi fungsi tidak boleeh kosong, tetapi jika karena alasan tertentu anda memiliki `function` tanpa konten, masukan didalamnya pernyataan `pass` untuk menghindari kesalahan.

Contoh:

```py
def myfunction():
  pass
```

## Positional-Only Arguments
Anda dapat menentukan bahwa suatu fungsi HANYA dapat memiliki argumen posisi, atau HANYA argumen kata kunci.

Untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen posisional, tambahkan `,/` setelah argumen:

```py
def my_function(x, /):
  print(x)

my_function(3)
```

Tanpa `,/` Anda sebenarnya diizinkan untuk menggunakan argumen kata kuci bahka jika fungsi tersebut mengharapkan argumen posisi:

```py
def my_function(x):
  print(x)

my_function(x = 3)
```

Namun, saat menambahkan `,/` Anda akan mendapatkan kesalahan jjika Anda mencoba mengirim argumen  kata kunci:

Contoh, fungsi seperti ini akan menghasilkan kesalahan:

```py
def my_function(x, /):
  print(x)

my_function(x = 3)
```

## Keyword-Only Arguments

Untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen kata kunci, tambahkan `*,` sebelum argumen:

```py
def my_function(*, x):
  print(x)

my_function(x = 3)
```

Tanpa `*,` Anda diperbolehkan menggunakan argumen posisional bahkan jika fungsi mengharapkan argumen kata kunci:

```py
def my_function(x):
  print(x)

my_function(3)
```

Namun, dengan `*,` Anda akan mendapatkan kesalahan jika Anda mencoba mengirim argumen posisi:

```py
def my_function(*, x):
  print(x)

my_function(3)
```
## Gabungkan Positional-Only and Keyword-Only
Anda dapat menggabungkan dua tipe argumen dalam fungsi yang sama.

Argumen apapun *sebelum* bersifat `/,` posisional saja, dan argumen apapun *setelahnya* bersifat `*,` kata kunci saja.

Contoh:

```py
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
```
## Rekursi
Python juga menerima rekursi fungsi, yang berarti suatu fungsi yang ditentukan dapat memanggil dirinya sendiri.

Rekursi adalah konsep matematika dan pemrograman yang umum. Artinya, suatu fungsi memanggil dirinya sendiri. Manfaatnya adalah Anda dapat mengulang data untuk mencapai suatu hasil.

Pengembang harus sangat berhati-hati dengan rekursi karena sangat mudah untuk tergelincir ke dalam penulisan fungsi yang tidak pernah berakhir, atau fungsi yang menggunakan memori atau daya prosesor yang berlebihan. Namun, jika ditulis dengan benar, rekursi dapat menjadi pendekatan pemrograman yang sangat efisien dan elegan secara matematis.

Dalam contoh ini, tri_recursion() adalah fungsi yang telah kita definisikan untuk memanggil dirinya sendiri ("recurse"). Kita menggunakan variabel k sebagai data, yang berkurang ( -1 ) setiap kali kita melakukan rekursi. Rekursi berakhir saat kondisinya tidak lebih besar dari 0 (yaitu saat nilainya 0).

Bagi pengembang baru, mungkin perlu waktu untuk mengetahui cara kerjanya secara tepat, cara terbaik untuk mengetahuinya adalah dengan menguji dan memodifikasinya.

Contoh:

```py
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
```