# Python - Pemahaman List
## Pemahaman List
Pemahaman list menawarkan sintaksis yang lebih pendek saat Anda ingin membuat list baru berdasarkan nilai list yang ada.

Contoh:

Berdasarkan list buah-buahan, Anda menginginkan list baru (newlist) yang hanya berisi buah-buahan dengan huruf "a" dalam namanya.

Tanpa pemahaman list, Anda harus menulis pertanyaan `for` dengan pengujian kondisional di dalamnya:

```py
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
	if "a" in x:
		newlist.append(x)

print(newlist)
```

Dengan pemahaman list, Anda dapat melakukan semua itu hanya dengan satu baris kode:

```py
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for in fruits if "a" in x]

print(newlist)
```

## Sintaksis

```py
newlist = [_expression_ for _item_ in _iterable_ if _condition_ == True]
```

Nilai yang dikembalikan adalah list baru, yang tidak mengubah list lama
## Kondisi
Kondisi ini seperti filter yang hanya menerima item yang bernilai `True`

Contoh, hanya terima barang yang bukan "apple":

```py
newlist = [x for x in fruits if x != "apple"]
```

Kondisi `if x != "apple"` akan kembali `True` untuk semua elemen selain "apel", membuat list baru berisi semua buah kecuali "apple".

Kondisi ini bersifat opsional dan dapat dihilangkan. 

Contoh, tanpa `if` pernyataan:

```py
newlist = [x for x in fruits]
```
## Iterable
Iterable atau dapat diulang, dapat berpa objek apa saja yang dapat diulang, seperti list, tupel, set, dll.

Contoh, anda dapat menggunakan fungsi `range()` untuk membuat sesuatu yang dapat diulang:

```py
newlist = [x for x in range(10)]
```

Contoh yang sama, tetapi dengan suatu kondisi:
Contoh, terima hanya angka yang lebih rendah dari 5:

```py
newlist = [x for x in range(10) if x < 5]
```

## Expression
Ekspresi adalah item saat ini dalam iterasi, tetapi juga merupakan hasil yang dapat anda manipulasi sebelum berakhir sepreti item list dalam newlist.

Contoh, tetapkan nilai dalam newliist ke huruf besar:

```py
newlist = [x.upper() for x in fruits]
```

Anda dapat mengatur hasil sesuai keinginan Anda:
Contoh, tetapkan semua nilai dalam newliist ke 'hello':

```py
newlist = ['hello' for x in fruits]
```

Ekspresi tersebut juga dapat berisi kondisi, bukan seperti filter, tetapi sebagai cara untuk memanipulasi hasilnya.

Contoh, mengembalikan "orange", bukanya "banana":

```py
newlist = [x if x != "banana" else "orange" for x in fruits]
```

Ungkapan dalam contoh di atas mengatakan:

*"Kembalikan barangnya kalau bukan banana, kalau banana kembalikan orange"*

