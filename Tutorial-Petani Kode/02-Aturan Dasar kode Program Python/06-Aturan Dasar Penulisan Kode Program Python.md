---
obsidianUIMode: preview
note_type: Book Theory
judul_materi: Aturan Dasar Penulisan Kode Program Python
sumber:
  - duniailkom
date_learned: 2025-10-03T16:44:00
tags:
  - python
---
Link Sumber: [Aturan Dasar Penulisan Kode Program Python \| Duniailkom](https://www.duniailkom.com/tutorial-belajar-python-aturan-dasar-penulisan-kode-program-python/#google_vignette)

---
# Aturan Dasar Penulisan Kode Program Python

Setelah aplikasi atau interpreter Python sudah tersedia dan bisa dijalankan, kita sudah bisa fokus membahas kode program Python itu sendiri, yang diawali dengan [Aturan Dasar Penulisan Kode Program Python](https://www.duniailkom.com/tutorial-belajar-python-aturan-dasar-penulisan-kode-program-python/).

## 1 | Struktur Kode Program Python

**Python** termasuk bahasa pemrograman yang sangat minimalis. Kita tidak butuh membuat struktur program apapun. Ini sering dijadikan "meme" di internet untuk menunjukkan betapa mudahnya membuat kode program dalam bahasa Python.

Sebagai contoh, berikut kode program dalam **bahasa C** untuk menampilkan teks "Hello World":

```c
#include <stdio.h>
int main(void)
{
  printf("Hello World");
  return 0;
}
```

Berikut kode program dalam **bahasa Pascal** untuk menampilkan teks "Hello World":

```pascal
program hello_world;
begin
  writeln('Hello World');
  readln;
end.
```

Dan berikut kode program dalam bahasa Python untuk menampilkan teks "Hello World":

```py
print("Hello World")
```

Yup, **hanya satu baris saja**. Dan dari kode program ini bisa disimpulkan bahwa **print** adalah perintah Python untuk menampilkan teks ke layar. Sangat sederhana.



---
## 2 | Statement Terminator

Selain tidak butuh struktur dasar, bahasa Python juga tidak perlu tanda titik koma ( ; ) di akhir setiap perintah sebagaimana yang sering ditemukan dalam bahasa pemrograman lain.

Secara teknis, Python menggunakan karakter _new line_ sebagai pemisah perintah. Karakter newline ini tidak lain adalah penanda pindah baris yang kita buat dengan cara menekan tombol Enter. Berikut contoh kode program Python dengan 4 baris perintah:

```py
print("Hello World")
web="Duniailkom"
print("Sedang belajar bahasa Python di "+web)
print("Semangat!!")
```

Selama tiap perintah berada dalam baris yang berlainan, itu sudah cukup.

Meskipun begitu, Python tidak protes seandainya kita tetap ingin menambah tanda titik dua di akhir setiap perintah:

```py
print("Hello World");
web="Duniailkom";
print("Sedang belajar bahasa Python di "+web);
print("Semangat!!");
```

Tanda titik koma ini menjadi harus ditulis jika kita ingin menulis beberapa perintah dalam 1 baris kode program:

```py
print("Hello World"); web="Duniailkom";
print("Sedang belajar bahasa Python di "+web); print("Semangat!!"); 
print('5+5');
```

Namun penulisan seperti ini tidak disarankan karena susah bagi kita untuk membacanya. Sebaiknya tempatkan 1 perintah dalam satu baris saja.


---
## 3 | Perbedaan Huruf Besar / Kecil dalam Bahasa Python

Bahasa Python menganut aturan penulisan **case sensitif**, yang artinya huruf besar dan kecil dianggap berbeda. Perintah **print** tidak bisa ditulis menjadi **Print** atau **PRINT**. Ini berlaku untuk perintah-perintah lain seperti _variabel_ dan _keyword_.

Berikut tampilan pesan error di Python ketika saya menulis perintah **Print** (dengan awalan huruf "P" besar):

![[06-Aturan Dasar Penulisan Kode Program Python-1.png]]



---
## 4 | Indentations

Dalam bahasa Indonesia, **indentations** bisa di translate sebagai **indentasi**. Bahasa bebasnya, _indentasi_ adalah menggeser atau "menjorokkan" beberapa baris kode program ke arah dalam.

Biasanya indentasi dipakai untuk sekedar memudahkan pembacaan kode program, namun dalam Python, indentasi berfungsi sebagai penanda blok kode program.

Perhatikan kode program berikut ini:

```py
for x in range(0, 5):
  print (x)
  if (x == 2):
    print("Yay, angka 2")
```

Hasil kode program Python:

```
0
1
2
Yay, angka 2
3
4
```

![[06-Aturan Dasar Penulisan Kode Program Python-2.png]]


Maksud dari kode program ini boleh diabaikan terlebih dahulu karena akan kita bahas secara bertahap dalam tutorial-tutorial berikutnya.

Tetapi perhatikan spasi di awal baris mulai dari baris ke 2 sampai ke 4. Inilah yang disebut dengan **indentasi**. Dalam bahasa pemrograman lain, indentasi ini hanya sebatas "pemanis" untuk mempermudah pembacaan kode program, tanpa tambahan spasi di awal pun kode program tetap berjalan sebagaimana mestinya.

Namun dalam bahasa Python, spasi di awal baris memiliki makna untuk membuat blok kode program. Jika indentasi di hapus, kode Python bisa menghasilkan error.

![[06-Aturan Dasar Penulisan Kode Program Python-3.png]]

Kode diatas menghasilkan error karena saya menghapus spasi di awal baris kedua.

Lebih jauh tentang indentasi dan blok kode program akan kita bahas pada saat masuk ke kondisi **if** dan **perulangan**. Untuk saat ini yang perlu dipahami adalah, spasi di awal kode program sangat penting di dalam Python.

---
## 5 | Comments

Dalam programming, **comments** atau **baris komentar** adalah istilah untuk menyebut keterangan tambahan. Comment ini ibarat _notes_ atau catatan yang biasa dipakai untuk menulis maksud dari kode tersebut. Comment tidak akan diproses oleh interpreter Python.

Untuk project yang besar dan melibatkan banyak programmer, comment akan mempermudah programmer lain untuk memahami maksud dari kode yang kita tulis.

Untuk membuat comment di dalam Python, awali sebuah baris dengan tanda **hash** atau tanda pagar ( # ), seperti contoh berikut:

```py
# ini adalah baris komentar
# kode program dibawah akan menampilkan angka 0 sampai 4
for x in range(0, 5):
  print (x)     # komentar juga bisa ditulis disini
```

Terlihat di baris 4 bahwa comment juga bisa berada di pertengahan baris. Mulai dari karakter hash hingga akhir baris tidak akan diproses oleh interpreter Python.

---
Dalam tutorial ini kita telah membahas secara singkat apa saja aturan dasar dari bahasa pemrograman Python. Diantaranya tentang struktur kode program, _statement terminator_, penggunaan huruf besar atau kecil, indentasi, dan _comment_.




