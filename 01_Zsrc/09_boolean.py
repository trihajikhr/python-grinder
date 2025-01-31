# nilai boolean
print(10<9)
print(10>12)
print(10==10)

a= 200
b=50

if b > a:
    print("b lebih besar dari ")
else:
    print("b lebih kecil dari a")


print("\nEvaluasi boolean dengan string")

print(bool("Hello"))
print(bool(15))

# fungsi mengemballikan nilai boolean

def myfunc():
    return True

if myfunc():
    print("YES")
else:
    print("NO!")

# fungsi boolean, apakah variabel x merupakan tipe data integer atau bukan
x = 200
print(isinstance(x, int))