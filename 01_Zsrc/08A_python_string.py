# dalam python, value dari tipe data string, bisa diapit oleh tanda kutip tunggal 
# atau tanda kutip ganda

print("Ini adalah latihan pertama")
print("Seputar materi string python")

a = "Hello World!"
print(a)

a = """Apapun yang datang dengan cepat,
akan pergi dengan cepat.
Jangan tertarik pada hasil yang instan,
tetapi pada sesuatu  yang mampu bertahan lama,
cukup berharga, dan dapat dibanggakan!"""
print(a)

if "cepat" in a:
    print("Kata cepat ada didalam teks")

if "terluka" not in a:
    print("kata terluka tidak ada didalam teks")