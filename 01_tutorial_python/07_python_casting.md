# Python Casting
## Tentukan Jenis Variabel
Mungkin ada saatnya Anda ingin menentukan tipe pada variabel. Ini dapat dilakukan dengan casting. Python adalah bahasa berorientasi objek, dan karenanya menggunakan kelas untuk menentukan tipe data, termasuk tipe primitifnya.

Oleh karena itu, casting dalam python dilakukan dengan menggunakan fungsi kontruktor:

- `int()` - Membuat bilangan integer dari literal integer, literal float (dengan menghilangakan semua desimal), atau literal string (dengan syarat string tersebut mewakili bilangan bulat)
- `float()` - Membuat bilangan float dari literal integer, literal float, atau literal string (dengan syarat string tersebut mewakili float atau integer)
- `str()` - Membuat string dari berbagai macam tipe data, termasuk string, literal integer, dan literal float

Contoh int:

```py
x = int(1)
y = int(2.8)
z = int("3")
```

Contoh float:

```py
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2 
```

Contoh str:

```py
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```