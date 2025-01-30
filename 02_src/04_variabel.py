# 1. penulisan variabel
print("##== Penulisan didalam variabel")
x = 5
y = "John"
print(x)
print(y)

# jika menggunakan casting
z = str(3)

# mendapatkan tipe datanya
print(type(x))

# 2. multivalue variabel
print("##== Multivalue variabel")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# satu nilai ke beberapa variabel
x = y = z = "Orange"
print(x)
print(y)
print(z)

# metode unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output banyak sekaligus
x = "enjoying"
y = "learning"
z = "Python"
print("I am", x, y, z)

# 3. global variabel
print("##== Global Variabel")
a = "awesome"

def myfunc():
    print("Python is " + a)
    
myfunc()

# global variabel didalam fungsi
def myfunc():
    global b
    b = "fantastic"
    
myfunc()
print("Python is " + b)

# merubah global variabel didalam fungsi
c = "awesome"
def myfunc():
    global c
    c = "fantastic"

myfunc()
print("Python is " + c)
