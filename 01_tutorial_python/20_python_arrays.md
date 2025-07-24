# Array Python
> Note : Python tidak memiliki dukungan bawaan untuk Array, tetapi *python list* dapat digunakan sebagai gantinya.

## Susunan
> Note : Halaman ini menunjukan cara menggunakan LIST sebagai ARRAY, namun, untuk bekerja dengan array di Python Anda harus mengimpor pustaka, seperti pustaka Numpy

Array digunakan untuk menyimpan beberapa nilai dalam satu variabel tunggal.

Contoh:
Buat array yang berisi nama mobil:

```py
cars = ["Ford", "Volvo", "BMW"]
```
## Apa itu Array?
Array adalah variabel khusus, yang dapat menampung lebih dari satu nilai pada satu waktu.

Jika Anda memiliki daftar item (daftar nama mobil, misalnnya), menyimpan mobil dalam variabel tunggal dapat terlihat seperti ini:

```py
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
```

Namun, bagaimana jika Anda ingin menelusuri mobil-mobil tersebut dan menemukan satu mobil tertentu? Dan bagaimana jika Anda tidak memiliki 3 mobil, tetapi 300?

Solusinya adalah array!

Suatu array dapat menampung banyak nilai dibawah satu nama, dan Anda dapat mengakses nilai-nilai tersebut dengan merujuk ke nomor indeks.
## Mengakses Elemen Array
Anda merujuk pada elemen array dengan merujuk pada nomor indeks.

Contoh:
Dapatkan nilai item array pertama:

```py
x = cars[0]
```

Contoh:
Ubah nilai item arrray pertama:

```py
cars[0] = "Toyota"
```
## Panjang Sebuah Array
Gunakan method `len()` untuk mengembalika panjang suatu array (jumlah elemen dalam suatu array).

Contoh:
Mengembalikan jumlah elemen dalam array `cars`

```py
x = len(cars)
```

> Note : Panjang suatu array selalu satu lebih panjang dari indek array tertinggi

## Elemen Array Perulangan
Anda dapat menggunakan `for in` loop mengulang semua elemen array.

Contoh:
Cetak setiap item dalam array `cars`

```py
for x in cars:
  print(x)
```

## Menambahkan Elemen Array
Anda dapat menggunakan method `append()` untuk menambahkan elemen ke dalam array

Contoh:
Tambahkan satu elemen lagi ke array `cars`

```py
cars.append("Honda")
```
## Menghapus Elemen Array
Anda dapat menggunakan method `pop()` untuk menghapus elemen dari array.

Contoh:
Hapus elemen kedua dari array `cars`

```py
cars.pop(1)
```

Anda juga dapat menggunakan method `remove()` untuk menghapus elemen dari array.

Contoh:
Hapus elemen yang memiliki nilai "Volvo"

```py
cars.remove("Volvo")
```

> Note : Method `remove()` hanya menghapus kemunculan pertama dari nilai yang ditentukan.

## Method Array
Python memiliki seperangkan method bawaan yang dapat anda gunakan pada list/array:

| Metode      | Deskripsi                                                                              |
|------------|--------------------------------------------------------------------------------------|
| `append()` | Menambahkan elemen di akhir daftar                                                 |
| `clear()`  | Menghapus semua elemen dari daftar                                                |
| `copy()`   | Mengembalikan salinan dari daftar                                                 |
| `count()`  | Mengembalikan jumlah elemen dengan nilai yang ditentukan                          |
| `extend()` | Menambahkan elemen dari daftar lain (atau iterable apa pun) ke akhir daftar saat ini |
| `index()`  | Mengembalikan indeks dari elemen pertama dengan nilai yang ditentukan             |
| `insert()` | Menambahkan elemen pada posisi yang ditentukan                                    |
| `pop()`    | Menghapus elemen pada posisi yang ditentukan                                      |
| `remove()` | Menghapus item pertama dengan nilai yang ditentukan                              |
| `reverse()`| Membalik urutan elemen dalam daftar                                               |
| `sort()`   | Mengurutkan daftar                                                                |
> Note : Python tidak memiliki dukungan bawaan untuk Array, tetapi Python List dapat digunakan sebagai gantinya.
