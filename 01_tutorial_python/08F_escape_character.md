# Python Escape Character
## Escape Character
Untuk menyisipkan karakter yang ilegal dalam suatu string, gunakan karakter escape.

Karakter escape adalah garis miring terbalik `\` yang diikuti oleh karakter yang ingin anda masukan. Contoh Karakter ilegal adalah tanda kutip gannda didalam string yang dikelilingi tanda kutip ganda.

Contoh, anda akan mendapatkan kesalahan jika Anda menggunakan tanda kutip ganda di dalam string yang dikelilingi tanda kutip ganda:

```py
txt = "We are the so-called "vikings" from the north"
```

Untuk memperbaiki masalah ini, gunakan karakter escape `\"`.
Contoh, karakter escape memungkinkan Anda menggunakan tanda kutip ganda ketika biasanya tidak diperbolehkan:

```py
txt = "We are the so-called \"Vikings\" from the north."
```
## Escape Character
Escape character lain yang bisa digunakan di Python:

| Code  | Result           |
|-------|-----------------|
| \'    | Single Quote    |
| \\    | Backslash       |
| \n    | New Line        |
| \r    | Carriage Return |
| \t    | Tab            |
| \b    | Backspace       |
| \f    | Form Feed       |
| \ooo  | Octal value     |
| \xhh  | Hex value       |
