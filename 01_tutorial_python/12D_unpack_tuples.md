# Python - Membongkar Tuple
## Membongkar tuple
Saat kita membuat tuple, kita biasanya menetapkan nilai padanya. Ini disebut "packing/mengemas" tuple. 

Contoh, packing tuple:

```py
fruits = ("apple", "banana", "cherry")
```

Namun, dalam python, kita juga dapat mengekstrak nilai-nilai tersebut kembali ke dalam variabel. Ini disebut "unpacking".

Contoh, unpacking tuple:

```py
fruits = ("apple", "banana", "cherry")

(green,yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

> Note : Jumlah variabel harus sesuai dengan jumlah nilai dalam tuple, jika tidak, anda harus menggunakan tanda bintang untuk mengumpulkan nilai yang tersisa sebagai daftar.

## Menggunakan Asterisk `*`
Jika jumlah variabel lebih kecil dari jumlah nilai, anda dapat menambhakan tanda `*` pada nama variabel dan nilai akan ditetapkan ke variabel sebagai list.

Contoh, tetapkan sisa nilai sebagai list, yang disebut "red":

```py
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
```

Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir, Python akan menetapkan nilai ke variabel tersebut hingga jumlah nilai yang tersisa cocok dengan jumlah variabel yang tersisa.

Contoh, tambahkan list ke variabel "tropic":

```py
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```