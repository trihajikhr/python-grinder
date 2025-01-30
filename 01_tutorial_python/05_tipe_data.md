# Tipe Data Python
## Tipe Data Bawaan
Dalam pemrograman, tipe data merupakan konsep penting. Variabel dapat menyimpan data dengan tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda.

Python memiliki tipe data bawaan berikut, dalam kategori berikut:
- Text type : `str`
- Numeric types : `int`, `float`, `complex`
- Sequence types : `list, 'tuple', 'range'
- Mapping type : `dict`
- Set types : `set`, `frozenset`
- Boolean type : `bool`
- Binary types : `bytes`, `bytearray`, `memoryview`
- None type : `NoneType`

## Mendapatkan Tipe Data
Anda bisa mendapatkan tipe data obejk apapun dengan menggunakan fungsi `type()`. 
Contoh, cetak tipe data variabel x :

```py
x = 5
print(type(x))
```

## Mengatur Tipe Data
Dalam python, tipe data ditetapkan saat Anda menetapkan nilai ke variabel:

| Contoh                                       | Tipe Data  |
| -------------------------------------------- | ---------- |
| x = "Hello World"                            | str        |
| x = 20                                       | int        |
| x = 20.5                                     | float      |
| x = 1j                                       | complex    |
| x =\["apple","banana","cherry"]              | list       |
| x =("apple","banana","cherry")               | tuple      |
| x = range(6)                                 | range      |
| x = {"name" : "John", "age" : 36}            | dict       |
| x = {"apple", "banana", "cherry"}            | set        |
| x = frozenset({"apple", "banana", "cherry"}) | frozenset  |
| x = True                                     | bool       |
| x = b"Hello"                                 | bytes      |
| x = bytearray(5)                             | bytearray  |
| x = memoryview(bytes(5))                     | memoryview |
| x = None                                     | NoneType   |
## Mengatur Tipe Data Tertentu
Jika anda ingin menentukan tipe data, anda dapat menggunakan fungsi konstruktor berikut:

| Example                                      | Data Type  |
|----------------------------------------------|------------|
| x = str("Hello World")                       | str        |
| x = int(20)                                  | int        |
| x = float(20.5)                              | float      |
| x = complex(1j)                              | complex    |
| x = list(("apple", "banana", "cherry"))      | list       |
| x = tuple(("apple", "banana", "cherry"))     | tuple      |
| x = range(6)                                 | range      |
| x = dict(name="John", age=36)                | dict       |
| x = set(("apple", "banana", "cherry"))       | set        |
| x = frozenset(("apple", "banana", "cherry")) | frozenset  |
| x = bool(5)                                  | bool       |
| x = bytes(5)                                 | bytes      |
| x = bytearray(5)                             | bytearray  |
| x = memoryview(bytes(5))                     | memoryview |
