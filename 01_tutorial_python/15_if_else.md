# Python - If Else
## Kondisi Python dan Pernyataan If
Python mendukung kondisi logika umum dari matematikan:
- Sama dengan : `a==b`
- Tidak sama dengan : `a != b`
- Kurang dari : `a < b`
- Kurang dari atau sama dengan : `a <= b`
- Lebih besar dari : `a > b`
- Lebih besar atau sama dengan : `a >= b`

Kondisi ini dapat digunakan dalam beberapa cara, yang paling umum adalah dalam pernyataan `if` dan perulangan.

"Pernyataan if" ditulis dengan menggunakan kata kunci `if`.

Contoh, pernyataan if:

```py
a = 33
b = 200
if b > a:
	print("b is greater than a")
```

Dalam contoh ini, kami menggunakan dua variabel, `a` dan `b`, yang digunakan sebagai bagian dari pernyataan if untuk menguji apakah `b` lebih besar dari `a`. Karena `a` adalah `33`, dan `b` adalah `200`, kami tahu bahwa 200 lebih besar dari 33, jadi kami mencetak ke layar bahwa "b is greater tha a".
## Indentasi
Python mengandalkan indentasi (spasi di awal baris) untuk menentukan cakupan kode. Bahasa pemrograman lain sering menggunakan tanda kurung kurawal untuk tujuan ini.

Contoh, pernyataan if, tanpa indentasi (akan menimbulkan kesalahan):

```py
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
```

## Elif
Kata kunci `elif` adalah cara Python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka kondisi ini".

Contoh:

```py
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

Dalam contoh ini `a` sama dengan `b`, jadi kondisi pertama tidak benar, namun kondisi `elif` benar, sehingga kita mencetak ke layar bahwa "a and b are equal".
## else
Kata kunci `else` menangkap apapun yang tidak ditangkap oleh kondisi sebelumnya. Contoh:

```py
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

Dalam contoh ini `a` lebih besar dari `b`, jadi kondisi pertama tidak benar, kondisi `elif` juga tidak benar, jadi kita masuk ke kondisi `else` dan mencetak ke layar bahwa "a lebih besar dari b".

Anda juga dapat memiliki `else` tanpa `elif`:

```py
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
```

## Shortcut If
Jika Anda hanya memiliki satu pernyataan untuk dieksekusi, Anda dapat meletaknya pada baris yang sama dengan pernyataan if:

```py
if a > b: print("a is greater than b")
```
## Shortcut If else
Jika Anda hanya memiliki satu pernyataan untuk dijalankan, satu untuk if, dan satu untuk else, Anda dapat meletakan semuanya pada baris yang sama:

Contoh, pernyataan if else satu baris:

```py
a = 2
b = 330
print("A") if a > b else print("B")
```

> Teknik ini dikenal sebagai **Operator Terner** , atau **Ekspresi Kondisional** .

Anda juga dapat memiliki beberapa pernyataan else pada baris yang sama.

Contoh, pernyataan if else satu baris, dengan 3 kondisi:

```py
a = 330
b = 330
print("A") if a > b else print ("=") if a == b else print("B")
```
## and
Kata kunci `and` adalah operator logika, dan digunakan untuk menggabungkan pernyataan kondisional:

Contoh, uji jika `a` lebih besar dari `b`, DAN jika `c` lebih besar dari `a`:

```py
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```

## or
Kata kunci `or` adalah operator logika, dan digunakan untuk menggabungkan pernyataan kondisional. 

Contoh, uji apakah `a` lebiih besar dari `b`, ATAU apakah `a` lebih besar dari `c`:

```py
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```
## not
Kata kunci `not` adalah operator logika, dan digunakan untuk membalikan hasil pernyataan kondisional.

Contoh, uji apakah `a` TIDAK lebih besar dari `b`:

```py
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```
## Nested if
Anda dapat memiliki pernyataan `if` di dalam pernyataan `if`, ini disebut nestedd if, atau pernyataan bersarang. Contoh:

```py
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```
## Pass
Pernyataan `if` tidak boleh kosong, tetapi jika karena alasan tertentu anda memiliki pernyataan `if` tanpa konten, masukan pernyataan `pass` tersebut untuk menghindari kesalahan. Contoh:

```py
a = 33
b = 200

if b > a:
  pass
```