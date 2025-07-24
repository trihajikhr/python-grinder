# Class dan Objct dalam Python
## CLass/Objek dalam Python
Python adalah bahasa pemrograman berorientasi objek.

Hampir semua hal di Python adalah objek, dengan properti dan metodenya. Class seperti konstruktor objek, atau "cetak biru" untuk membuat objek.

## Buat Class
Untuk membuat class, gunakan kata kunci `class`.

Contoh:
Buat class bernama `MyClass`, dengan properti bernama x

```py
class MyClass:
  x = 5
```
## Buat Objek
Sekarang kita dapat menggunakan class bernama `MyClass` untuk membuat objek.

Contoh:
Buat objek bernama p1, dan cetak nilai x

```py
p1 = MyClass()
print(p1.x)
```
## Fungsi `__init__()`
Contoh diatas adalah class dan objek dalam bentuk yang paling sederhana, dan tidak benar-benar berguna dalam aplikasi kehidupan nyata.

Untuk memahami arti class, kita harus memahami fungsi bawaan `__init__()`.

Semua class memiliki fungsi yang disebut `__init__()`, yang selalu dieksekusi saat class dimulai.

Gunakan `__init__()` fungsi ini untuk menetapkan nilai ke properti objek, atau operasi lain yang perlu dilakukan saat objek sedang dibuat.

Contoh:
Buat class bernama Person, gunakan fungsi `__init__()` tersebut untuk menetapkan nilai untuk nama dan usia

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```

> Note : Fungsi `__init__()` dipanggil secara otomatis setiap kali class digunakan untuk membuat objek baru.

## Fungsi `__str__()`
Fungsi `__str__()`, mengontrol apa yang harus dikembalikan ketika objek kelas direpresentasikan sebagai string.

Jika fungsi `__str__()` tidak diatur, representasi string objek dikembalikan.

Contoh:
Representasi string suatu objek TANPA fungsi `__str__`

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
```

Contoh:
Representasi string dari sebuah objek DENGAN fungsi `__str__()`

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
```
## Method Objek
Objek juga dapat berisi method. Method dalam objek adalah fungsi yang dimiliki oleh objek tersebut.

Mari kita membuat method di class Person.

Contoh:
Masukan fungsi yang mencetak ucapan salam, dan jalankan pada objek p1:

```py
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```

> Note : Parameter `self`merupakan referensi ke instansi class saat ini, dan digunakan untuk mengakses variabel yang termasuk dalam class tersebut.

## Self Parameter
Parameter `self` merupakan referensi ke instansi class saat ini, dan digunakan untuk mengakses variabel yang termasuk dalam class tersebut.

Tidak harus diberi nama `self`, Anda dapat menyebutnya apa pun yang Anda suka, tetapi harus menjadi parameter pertama dri fungsi apa pun di class.

Contoh:
Gunakan kata *mysillyobject* dan *abc* sebagai ganti *self*:

```py
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```
## Ubah Properti Objek
Anda dapat mengubah properti pada objek seperti ini.

Contoh:
Tetapkan usia p1 menjadi 40

```py
p1.age = 40
```
## Hapus Properti Objek
Anda dapat menghapus properrti pada objek dengan menggunakan kata kunci `del`.

Contoh:
Hapus properti usia dari objek p1

```py
del p1.age
```
## Hapus Objek
Anda dapat menghapus objek dengan menggunakan kata kunci `del`.

Contoh:
Hapus objek p1:

```py
del p1
```
## Pernyataan Pass
Definisi `class` tidak boleh kosong, tetapi jika karena alasan tertentu Anda memiliki definisi `class` tanpa konten, masukan pernyataan `class` untuk menghindari kesalahan.

Contoh:
```py
class Person:
	pass
```