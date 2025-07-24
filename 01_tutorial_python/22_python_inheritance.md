# Pewarisan Python
## Pewarisan dalam Python
Pewarisan atau bahasa inggrisnya Inheritance memungkinkan kita mendefinisika class yang mewarisi semua method dan properti dari class lain.

Parent class, atau kelas induk adalah class yang diwarisi, disebut juga class dasar.

Child class, atau kelas anak adalah class yang mewarisi dari class lain, disebut juga class turunan.
## Buat Class Induk
Class apapun bisa menjadi class induk, jadi sintaksnya sama dengan membuat class lainya.

Contoh:
Buat class bernama `Person`,  dengan properti `firstname` dan method `lastname printname`

```py
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```
## Buat Class Anak
Untuk membuat class yang mewarisi fungsionalitas dari class lain, kirimkan class induk sebagai parameter saat membuat class anak.

Contoh:
Buat class bernama `student`, yang akan mewarisi properti dan method dari class `Person`

```py
class Student(Person):
  pass
```

> Note : Gunakan kata kunci `pass` ketika Anda tidak ingin menambah properti atau method lain ke class

Sekarang class Student memiliki properti dan method yang sama dengan class Person

Contoh:
GUnakan class `Student` untuk membuat objek, lalu jalankan method `printname`

```py
x = Student("Mike", "Olsen")
x.printname()
```

## Tambahkan Fungsi `__init__()`
Sejauh ini kita telah membuat class anak yang mewarisi properti dan method dari induknya. Kami ingin menamahkan fungsi `__init__()` ke class anak (bukan kata kunci `pass).

> Note : Fungsi `__init__()` dipanggil secara otomatis setiap kali class digunakan unntuk membuat objek baru

Contoh:
Tambahkan fungsi `__init__()` ke class `Student`

```py
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```

Ketika Anda menambahkan fungsi `__init__()` tersebut, class anak tidak akan lagi mewarisi fungsi `__init__()` induknya.

> Note : fungsi `__init__()` anak menggantikan pewarisan fungsi `__init__()` induknya.

Untuk mempertahankan pewarisan fungsi `__init__()` induk, tambahkan panggilan ke fungsi `__init__()` induk.

Contoh:
```py
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

Sekarang kit telah berhasil menambahkan fungsi `__init__()` tersebut, dan mempertahankan warisan class induk, dan kita siap untuk menambahkan fungsionalitas ke dalam fungsi `__init__()` tersebut.
## Gunakan Fungsi Super()
Python juga memiliki fungsi `super()` yang akan membuat class anak mewarisi semua method dan properti dari induknya.

Contoh:
```py
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```

Dengan menggunakan fungsi `super()` tersebut, Anda tidak perlu menggunakan nama elemen induk, maka secara otomatis akan mewarisi method dan properti dari induknya.
## Tambahkan Properti
Contoh:
Tambahkan properti yang disebut `graduationyear` ke class `Student`:

```py
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
```

Dalam contoh dibawah ini, tahun `2019` harus berupa variabel, dan dimasukan ke dalam class `Student` saat membuat object siswa. Untuk melakukanya, tambahkan parameter lain dalam fungsi `__init__()`.

Contoh:
Tambahkan parameter `year`, dan masukan tahun yang benar saat membuat objek:

```py
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
```
## Tambahkan Method
Contoh:
Tambakan method `welcomme` yang dipanggil ke class `Student`

```py
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```

Jika Anda menambahkan method di class anak dengan nama yang sama dengan  fungsi di class induk, pewarisan method induk akan ditimpa.