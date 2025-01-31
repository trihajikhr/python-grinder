# Urutan list berdasarkan Alfanumetrik
Objek list memiliki fungsi `sort()` yang akan mengurutkan list secara alfanumetrik, menaik, secara default:

Contoh, urutkan berdasarkan abjad:

```py
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
```

Contoh, urutan list secara alfanumetrik:

```py
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
```
## Urutan secara menurun
Untuk mengurutkanya secara menurun, gunakan argumen dengan kata kunci `reverse = True`:

Contoh, urutkan list secara menurun:

```py
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
```

Contoh, urutkan list secara menurun:

```py
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
```

Sesuaikan Fungsi sort
Anda juga dapat menyesuaikan fungsi anda sendiri dengan menggunakan argumen dengan kata kunci `key = function`

Fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan list (angka terendah terlebih dahulu):

Contoh, urutkan list berdasarkan seberapa dekat angka tersebut dengan 50:

```py
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```

## Pengurutan Tanpa membedakan huruf besar dan kecil
Secara default, fungsi `sort()` peka terhadap huruf besar kecil, sehingga semua huruf kapital akan diurutkan terlebih dahulu sebelum huruf kecil.

Contoh, pengurutan peka terhadap huruf beesar/kecil dapat memberikan hasil yang tidak diharapkan:

```py
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
```

Untungnya kita dapat menggunakan fungsi bawaan sebagai fungsi utama saat mengurutkan list.

Jadi jika anga menginginkan fungsi pengurutan tanpa memperhatikan huruf besar/kecil, gunakan `str.lower` sebagai fungsi kunci.

Contoh, lakukan pengurutan list tanpa memperhatikan huruf besar/kecil:

```py
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
```
## Sort reverse
Bagaimana jika anda ingin membalik susunan list, apapun abjadnya? 

Fungsi ini `reverse()` membalik susunan penyortiran elemen saat ini.

Contoh, membalikan urutan item list:

```py
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
```
