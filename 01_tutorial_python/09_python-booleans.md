# Boolean pada Python
Boolean mewakili satu dari dua nilai: `True` atau `False`
## Nilai Boolean
Dalam pemrograman Anda sering kali perlu mengetahui apakah suatu ekspresi adalah `True` atau `False`.

Anda dapat mengevaluasi ekspresi apa pun dalam Python, dan mendapatkan salah satu dari dua jawaban, `True`atau `False`.

Saat Anda membandingkan dua nilai, ekspresi dievaluasi dan Python mengembalikan jawaban Boolean:

```py
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

Ketika Anda menjalankan suatu kondisi dalam pernyataan if, Python mengembalikan `True`atau `False`.
Contoh, cetak pesan berdasarkan apakah kondisinya `True` atau `False`:

```py
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```
## Mengevaluasi Nilai dan Variabel
Fungsi `bool()` memungkinkan Anda untuk mengevaluasi nilai apapun, dan memberi Anda `True` atau `False` sebagai gantinya.
Contoh, mengevaluasi string dan angka:

```py
print(bool("Hello"))
print(bool(15))
```

Contoh, mengevaluasi dua variabel:

```py
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```

## Sebagian besar nilai adalah Benar
Hampir semua nilai dievaluasi menjadi `True` jika memiliki beberapa jenis konten.

String apa pun bernilai `True`, kecuali string kosong.

Angka apa pun bernilai `True`, kecuali 0.

Semua daftar, tupel, set, dan kamus adalah `True`, kecuali yang kosong.

Contoh, berikut ini akan mengembalikan `True`:

```py
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
```
## Beberapa nilai Salah
Faktanya, tidak banyak nilai yang bernilai `False`, kecuali nilai kosong, seperti `()`, `[]`, `{}`, angka `0`, dan nilai `None`. Dan tentu saja nilainya `False` bernilai `False`.

Contoh:
Berikut ini akan mengembalikan `False`:

```py
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```

Satu nilai lagi, atau objek dalam kasus ini, dievaluasi menjadi `False`, dan itu jika Anda memiliki objek yang dibuat dari kelas dengan `__len__` fungsi yang mengembalikan `0` atau `False`:

```py
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
```
## Fungsi dapat mengembalikan Boolean
Anda dapat membuat fungsi yang mengembalikan Nilai Boolean.
Contoh, cetak jawaban suatu fungsi:

```py
def myFunction() :
  return True

print(myFunction())
```

Anda dapat mengeksekusi kode berdasarkan jawaban Boolean suatu fungsi.
Contoh, cetak "YES!" jika fungsi mengembalikan True, jika tidak maka cetak "NO!":

```py
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
```

Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean, seperti `isinstance()` fungsi, yang dapat digunakan untuk menentukan apakah suatu objek memiliki tipe data tertentu.
Contoh, periksa apakah suatu objek merpakan bilangan bulat atau integer atau bukan:

```py
x = 200
print(isinstance(x, int))
```