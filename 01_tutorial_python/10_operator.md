# Python Operator
## Operator Python
Operator digunakan untuk melakukan operasi pada variabel dan nilai. Dalam contoh di bawah ini, kami menggunakan operator `+` untuk menambahkan dua nilai:

```py
print(10 + 5)
```

Python membagi operator ke dalam kelompok berikut:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators
## Operator Aritmatika Python
Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum:

| Operator | Name           | Contoh |
| -------- | -------------- | ------ |
| +        | Penambahan     | x + y  |
| -        | Pengurangan    | x - y  |
| *        | Perkalian      | x * y  |
| /        | Pembagian      | x / y  |
| %        | Modulus        | x % y  |
| **       | Exponentiation | X ** y |
| //       | Floor division | x // y |
## Operator penugasan Python
Operator penugasan digunakan untuk menetapkan nilai ke variabel:

| Operator | Contoh        | Sama dengan       |
| -------- | ------------- | ----------------- |
| =        | x = 5         | x = 5             |
| +=       | x += 5        | x = x + 3         |
| -=       | x -= 5        | x = x - 3         |
| *=       | x *= 5        | x = x * 3         |
| /=       | x /=5         | x = x / 3         |
| %=       | x %= 3        | x = x % 3         |
| //=      | x //= 3       | x = x // 3        |
| **=      | x **= 3       | x = x ** 3        |
| %=       | x &= 3        | x = x & 3         |
| \|=      | x \|= 3       | x = x \| 3        |
| ^=       | x ^= 3        | x = x ^ 3         |
| >>=      | x >>= 3       | x = x >> 3        |
| <<=      | x <<= 3       | x = x << 3        |
| :=       | print(x := 3) | x = 3<br>print(x) |
## Operator Perbandingan Python
Operator perbandingan digunakan untuk membandingkan dua nilai:

| Operator | Nama                         | Contoh   |
|----------|------------------------------|----------|
| ==       | Sama dengan                  | x == y   |
| !=       | Tidak sama dengan            | x != y   |
| >        | Lebih besar dari             | x > y    |
| <        | Lebih kecil dari             | x < y    |
| >=       | Lebih besar dari atau sama dengan | x >= y   |
| <=       | Lebih kecil dari atau sama dengan | x <= y   |
## Operasi Logika Python
Operasi logika digunakan untuk menggabungkan pernyataan kondisional:

| Operator | Deskripsi                                              | Contoh                |
| -------- | ------------------------------------------------------ | --------------------- |
| and      | Mengembalikan True jika kedua pernyataan benar         | x < 5 and x < 10      |
| or       | Mengembalikan True jika salah satu pernyataan benar    | x < 5 or x < 4        |
| not      | Membalik hasil, mengembalikan False jika hasilnya True | not(x < 5 and x < 10) |
## Operator Identitas Python
Operator identitas digunakan untuk membandingkan objek, bukan jika objek tersebut sama, tetapi jika objek tersebut sebenarnya adalah objek yang sama, dengan lokasi memory yang sama:

| Operator  | Deskripsi                                           | Contoh    |
|-----------|----------------------------------------------------|-----------|
| is        | Mengembalikan True jika kedua variabel adalah objek yang sama | x is y   |
| is not    | Mengembalikan True jika kedua variabel bukan objek yang sama  | x is not y |
## Operator Keanggotaan Python
Operator keanggotaan digunakan untuk menguji apakah suatu urutan disajikan dalam suatu objek:

| Operator  | Deskripsi                                                    | Contoh      |
|-----------|--------------------------------------------------------------|------------|
| in        | Mengembalikan True jika suatu urutan dengan nilai tertentu ada dalam objek | x in y     |
| not in    | Mengembalikan True jika suatu urutan dengan nilai tertentu tidak ada dalam objek | x not in y |
## Operator Bitwise Python
Operator bitwise digunakan untuk membandingkan angka (biner):

| Operator | Nama                      | Deskripsi                                                                 | Contoh    |
|----------|---------------------------|---------------------------------------------------------------------------|-----------|
| &        | AND                        | Menetapkan setiap bit menjadi 1 jika kedua bit adalah 1                   | x & y     |
| \|       | OR                         | Menetapkan setiap bit menjadi 1 jika salah satu dari dua bit adalah 1     | x \| y    |
| ^        | XOR                        | Menetapkan setiap bit menjadi 1 jika hanya salah satu dari dua bit adalah 1 | x ^ y    |
| ~        | NOT                        | Membalik semua bit                                                        | ~x        |
| <<       | Zero fill left shift       | Geser ke kiri dengan memasukkan nol dari kanan, bit kiri terbuang         | x << 2    |
| >>       | Signed right shift         | Geser ke kanan dengan menyalin bit kiri terluar, bit kanan terbuang       | x >> 2    |
## Prioritas Operator
Prioritas operator menggambarkan urutan pelaksanaan operasi.

Contoh, tanda kurung memiliki prioritas tertinggi, yang berarti bahwa ekspresi di dalam tanda kurung harus dievaluasi terlebih dahulu:

```py
print((6 + 3) - (6 + 3))
```

Contoh, perkalian `*` mempunyai priorritas lebih tinggi daripada penjumlaahn `+`, dan karenanya perkalian dievaluasi sebelum penjumlahan:

```py
print(100 + 5 * 3)
```

Urutan prioritas dijelaskan dalam tabel di bawah ini, dimulai dengan prioritas tertinggi di bagian atas:

| Operator                                     | Deskripsi                                           |
| -------------------------------------------- | --------------------------------------------------- |
| ()                                           | Tanda kurung                                        |
| **                                           | Pemangkatan (Eksponensiasi)                         |
| +x, -x, ~x                                   | Unary plus, unary minus, dan bitwise NOT            |
| *, /, //, %                                  | Perkalian, pembagian, pembagian lantai, dan modulus |
| +, -                                         | Penjumlahan dan pengurangan                         |
| <<, >>                                       | Pergeseran bit ke kiri dan ke kanan                 |
| &                                            | Bitwise AND                                         |
| ^                                            | Bitwise XOR                                         |
| \|                                           | Bitwise OR                                          |
|                                              |                                                     |
| ==, !=, >, >=, <, <=, is, is not, in, not in | Operator perbandingan, identitas, dan keanggotaan   |
| not                                          | Logical NOT (Negasi logis)                          |
| and                                          | Logical AND                                         |
| or                                           | Logical OR                                          |
Jika dua operator memiliki prioritas yang sama, ekspresi dievaluasi dari kiri ke kanan.

Contoh, penjumlahan dan  pengurangan memiliki prioritas yang sama, dan karenanya kita mengevaluasi ekspresi dari kiri ke kanan:

```py
print(5 + 4 - 7 + 3)
```