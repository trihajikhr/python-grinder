# Python - While Loops
## Perulangan Python
Python memiliki dua perintah loop primitif:
- `while` loop
- `for` loop
## While loop
Dengan loop `while`, kita dapat mengeksekusi serangkaian pernyataan selama kondisinya benar.

Contoh, cetak i selama i kurang dari 6:

```py
i = 1
while i < 6:
  print(i)
  i += 1
```

> Note : ingat untuk menambah i, atau perulangan akan berlanjut selamanya.

Perulangan `while` memerlukan variabel relevan untuk siap, dalam contoh ini, kita perlu mendefinisikan variabel pengindeksan, `i`, yang kita tetapkan ke 1.

## Pernyataan Break
Dengan pernyataan `break`, kita dapat menghentikan loop bahkan jika kondisi while bernilai true.

Contoh, keluar dari look ketika i adalah 3:

```py
i = 1
while i < 6:
	print(i)
	if i == 3:
		break;
	i += 1
```

## Continue statement
Dengan pernyataan `continue`, kita dapat mengehntikan iterasi saat ini, dan melanjutkan dengan iterasi berikutnya:

Contoh, lanjutkan ke iterasi berikutnya jika i adalah 3:

```py
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

## Pernyataan else
Dengan pernyataan `else` kita dapat menjalankan blok kode sekali ketika kondisinya tidak lagi benar.

Contoh, cetak pesan jika kondisinya salah:

```py
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```