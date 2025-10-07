# Enhanced Playfair Cipher (6×6)

Program enkripsi dan dekripsi menggunakan algoritma Playfair yang dikembangkan menjadi matriks **6×6** sehingga mendukung huruf **A–Z** dan angka **0–9**.

## Fitur

- Enkripsi dan dekripsi teks alfanumerik (A–Z, 0–9)
- Visualisasi matriks kunci 6×6
- Input otomatis dinormalisasi (hanya A–Z dan 0–9, uppercase)
- Interface command-line sederhana

## Cara Kerja Singkat

Playfair 6×6 menggunakan matriks 6×6 yang dibentuk dari kunci (karakter unik lebih dulu), lalu diisi sisa karakter dari A–Z dan 0–9.

Aturan bigram (sama seperti Playfair klasik, namun pada grid 6×6):

- Baris sama: geser kanan untuk enkripsi, kiri untuk dekripsi
- Kolom sama: geser bawah untuk enkripsi, atas untuk dekripsi
- Persegi panjang: tukar kolom (ambil sudut persegi panjang)
- Wrapping menggunakan modulo 6

## Penggunaan

Jalankan program:

```bash
python playfair-6x6.py
```

Menu:

- `E` untuk enkripsi
- `D` untuk dekripsi

## Contoh

```
Encrypt or Decrypt (E/D): E
Enter the key: SECRET123
Enter the plain text: PROGRAMMING2024

Playfair Key Table (6x6):
+-------------+
| S E C R T 1 |
| 2 3 A B D F |
| G H I J K L |
| M N O P Q U |
| V W X Y Z 0 |
| 4 5 6 7 8 9 |
+-------------+
Cipher text: YBMICBOVHOMGVF6V
```

## Catatan

- Pasangan huruf yang sama akan disisipi 'X' (mis. HELLO → HELXLO)
- Panjang ganjil akan dipad dengan 'X' di akhir
- Kunci harus sama pada enkripsi dan dekripsi
- Hanya karakter A–Z dan 0–9 yang diproses

## Persyaratan

- Python 3.6+
- Tanpa dependensi tambahan

---

Program edukasi untuk pembelajaran kriptografi klasik yang disesuaikan dengan data alfanumerik modern.
