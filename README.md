# Playfair Cipher

Program enkripsi dan dekripsi menggunakan algoritma **Playfair Cipher** dalam Python.

## Fitur

- Enkripsi dan dekripsi teks
- Visualisasi matriks kunci 5x5
- Input otomatis dinormalisasi
- Interface command-line sederhana

## Cara Kerja

Playfair menggunakan matriks 5x5 dari kunci untuk mengenkripsi teks berpasangan.

**Aturan:**

- Baris sama: geser kanan/kiri
- Kolom sama: geser bawah/atas
- Berbeda: tukar kolom

## Penggunaan

```bash
python playfair-main.py
```

**Menu:**

- `E` untuk enkripsi
- `D` untuk dekripsi

**Contoh:**

```
Encrypt or Decrypt (E/D): E
Enter the key: KEYWORD
Enter the plain text: HELLO WORLD

Key text: KEYWORD
Plain text: HELLO WORLD

Playfair Key Table:
+-----------+
| k e y w o |
| r d a b c |
| f g h i l |
| m n p q s |
| t u v x z |
+-----------+
Cipher text: dmyranvqrn
```

## Catatan

- Huruf 'J' otomatis diganti dengan 'I'
- Teks ganjil ditambah 'Z' di akhir
- Kunci harus sama untuk enkripsi dan dekripsi

## Persyaratan

- Python 3.6+
- Tidak perlu library tambahan

---

_Program edukasi untuk pembelajaran kriptografi klasik_
