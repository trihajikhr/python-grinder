print("##== Menampilkan tipe data")
x = 5
print(type(x))


# ada banyak tipe data dalam python
# kita bisa mengaturnya dengan menentukan jenis tipe data yang kita masukan ke dalam variabel

# selain itu, kita juda bisa mengatur agar suatu variabel bisa menampung tipe data tertentu saja


y = int(20)
z = str("Hello World!")

print(y)
print(z)
print(type(y))
print(type(z))

print("Tampilan semua jenis tipe data")
x = "Hello World"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple","pisang"]
print(type(x))
x = ("apple","pisang")
print(type(x))
x = range(6)
print(type(x))
x = {"name":"John", "age":36}
print(type(x))
x = {"apple","banana","Cherry"}
print(type(x))
x = frozenset({"ape","pisang","cherry"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))
