# Komentar Python
Komentar dapat digunakan untuk menjelaskan kode Python. Komentar dapt digunakan untuk membuat kode lebih mudah dibaca. Komentar dapat digunakan untuk mencegah eksekusi saat menguji kode.
## Membuat komentar
Komentar dimulai dengan #, dan Python akan mengabaikanya:
Contoh:

```py
#ini adalah komentar
print("Hello, World!")
```

Komentar dapat ditempatkan di akhir baris, dan python akan mengabaikan sisa baris.
Contoh:

```py
print("Hello, World!") #ini adalah komentar
```

Komentar tidak harus berupa teks yang menjelaskan kode, komentar juga dapat digunakan untuk mencegah Python mengeksekusi kode.
Contoh:

```py
#print("Halo dunia")
print("Semangat kawan!")
```

## Komentar multiline / multibaris
Python tidak benar-benar memiliki sintaksis untuk komentar multibaris. UNtuk menambahkan komentar multiline, Anda dapat menyisipkan # untuk setiap baris.

```py
#This is a comment
#written in
#more than just one line
print("Hello, World!")
```

Atau, tidak sepenuhnya sesuai dengan yang diinginkan, Anda dapat menggunakan string multiline.

Karena Python akan mengabaikan literal string yang tidak ditetapkan ke variabel, Anda dapat menambahkan string multiline (tanda kutip tiga) dalam kode anda, dan menempatkan komentar Anda di dalamnya:

```py
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

Selama string tidak ditetapkan ke variabel, Python akan membaca kode tersebut, tetapi kemudian mengabaikanya, dan Anda telah membuat komentar multibaris.