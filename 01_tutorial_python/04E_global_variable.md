# Python - Variable Global
## Variabel Global
Variabel yang dibuat di luar suatu fungsi (seperti dalam semua contoh di tutorial sebelumnya) dikenal sebagai variabel global.

Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar.
Contoh:

```py
x = "keren"

def myfunc():
	print("Python itu "+x)

myfunc()
```

Jika anda membuat variabel dengan nama yang sama dialam suatu fungsi, variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti sebelumnya, global dan dengan nilai aslinya.
Contoh:

```py
x = "keren"

def myfunc():
	x = "Fantastis"
	print("Python itu " + x)

myfunc()

print("Python pasti sangat " + x)
```
## Kata Kunci Global
Biasanya, ketika Anda membuat suatu variabel di dalam suatu fungsi, variabel tersebut bersifat lokal, dan hanya dapat digunakan didalam fungsi tersebut.

Untuk membuat variabel lokal yang ada didalam fungsi tersebut menjadi global, anda dapat menggunakan kata kunci `global`.
Contoh:

```py
def myfunc():
	global x
	x = "fantastic"

myfunc()

print("Python is " + x)
```

Gunakan juga kata kunci `global` jika anda ingin mengubah variabel global didalam suatu fungsi.
Contoh, untuk mengubah nilai variabel global didalam suatu fungsi, rujuk variabel tersebut dengan menggunakan kata kunci `global`:

```py
x = "Keren"

def myfunc():
	global x
	x = "Fantastis"

myfunc()

print("Python sangat " + x)
```
