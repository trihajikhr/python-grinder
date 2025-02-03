# Python - Hapus item yang ditetapkan
## Hapus item
Untuk menghapus item dalam satu set, gunakan method `remove()` atau `discard()`.

Contoh, hapus "banana" dengan menggunakan method `remove()`:

```py
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
```

> Note : Jika item yang akan dihapus tidak ada, `remove()` akan memunculkan kesalahan.

Contoh, hapus "banana" dengan menggunakan method `discard()`:

```py
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
```

> Note : Jika item yang akan dihapus tidak ada, `discard()` TIDAK akan menimbulkan kesalahan.

Anda juga, dapat menggunakan method `pop()` untuk menghapus suatu item, tetapi metode ini akan menghapus item secara acak, jadi anda tidak dapat memastikan item mana yang dihapus.

Nilai pengembalian metode `pop()` adalah item yang dihapus.

Contoh, hapus item acak dengan menggunakan `pop()`:

```py
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
```

> Note : Set tidak diurutkan, jadi saat menggunakan `pop()`, anda tidak tahu item mana yang dihapus.

Contoh, method `clear()` mengosongkan set:

```py
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
```

> Contoh, kata kunci `del` akan menghapus set sepenuhnya:

```py
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
```