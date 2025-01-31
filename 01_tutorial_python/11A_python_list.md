# List Python
## List
List digunakan untuk menyimpan beberapa item dalam satu variabel.

List adalah salah satu dari 4 ttipe data bawaan dalam python yang digunakan untuk menyimpan kumpulan data, 3 lainya adalah `Tuple`, `Set`, dan `Dictionary`, semuanya dengan kualitas dan penggunaan yang berbeda.

List dibuat menggunakan tanda kurung siku.
Contoh, buat list:

```py
thislist = ["Apel","Pisang","Semangka"]
print(thislist)
```

## List item
Item dalam list diurutkan, dapat diubah, dan memperbolahkan nilai duplikat. Item dalam list diindeks, item pertama mempunyai indek `[0]`, item kedua mempunya indeks `[1]`, dan seterusnya.
## Ordered
Ketika kita mengatakan bahwa list diurutkan, artinya item-itemnya memiliki urutan yang psaati, dan urutan itu tidak akan berubah.

Jika anda menambahkan item baru ke suatu list, item baru tersebut akan ditempatkan di akhir list.

> Catatan: Ada beberapa fungsi list yang akan mengubah urutan, tetapi secara umum: urutan item tidak akan berubah.

## Dapat diubah
List tersebut dapat diubah, artinya kitta dapat mengubah, menambah, dan menghapus item dalam list setelah list dibuat.
## Izinkan Duplikat
Karena list diindeks, list dapat memiliki item dengan nilai yang sama.
Contoh: list memperbolehkan nilai duplikat:

```py
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```
## Panjang list
Untuk menentukan berapa banyak item yang dimiliki suatu list, gunakan fungsi `len()`.
Contoh: cetak jumlah item dalam list:


```py
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
## List item - Tipe data
Item dalam list dapat berupa tipe data apapun.
Contoh, tipe data string, int, dan boolean:

```py
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

Suatu list dapat berisi berbagai tipe data.
Contoh, list dengann string, integer, dan nilai boolean:

```py
list1 = ["abc", 34, True, 40, "male"]
```
## Type
Dari perpekstif Python, list didefinisikan sebagai objek dengan tipe data `list`.

```shell
<class `list`>
```

Contoh, apa tipe data dari sebuah list?

```py
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
```
## The list() Constructor
Dimungkinkan juga untuk menggunakan konstruktor list() saat membuat list baru.
Contoh: menggunakan `list()` konstruktor untuk membuat list:

```py
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
```
## Koleksi Python (Arrays) 
Terdapat empat jenis tipe data koleksi dalam bahasa pemrograman Python:

- **List** adalah koleksi yang **terurut** dan **dapat diubah**. Memungkinkan adanya anggota duplikat.
- **Tuple** adalah koleksi yang **terurut** dan **tidak dapat diubah**. Memungkinkan adanya anggota duplikat.
- **Set** adalah koleksi yang **tidak terurut**, **tidak dapat diubah**\*, dan **tidak memiliki indeks**. Tidak memungkinkan adanya anggota duplikat.
- **Dictionary** adalah koleksi yang **terurut** (**sejak Python 3.7**) dan dapat diubah\*\*. Tidak memungkinkan adanya anggota duplikat.

> * _Items_ yang ditetapkan tidak dapat diubah, tetapi Anda dapat menghapus dan/atau menambahkan item kapan saja Anda mau.
> 
> \*\*Pada Python versi 3.7, dictionary _diurutkan_ . Pada Python 3.6 dan sebelumnya, dictionary _tidak diurutkan_ .

Saat memilih jenis koleksi, penting untuk memahami properti jenis tersebut. Memilih jenis yang tepat untuk kumpulan data tertentu dapat berarti mempertahankan makna, dan dapat berarti peningkatan efisiensi atau keamanan.