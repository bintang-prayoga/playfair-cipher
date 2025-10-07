# Playfair Cipher 6×6 (A–Z dan 0–9)

Program enkripsi dan dekripsi menggunakan algoritma Playfair yang dikembangkan menjadi matriks **6×6** sehingga mendukung huruf **A–Z** dan angka **0–9**. Program interaktif ini menggunakan file `playfair-main.py`.

## Fitur

- Mendukung karakter alfanumerik: **A–Z** dan **0–9** (total 36)
- **Matriks kunci 6×6** yang dibentuk dari key unik + sisa karakter
- **Normalisasi otomatis**: uppercase dan hanya A–Z/0–9
- **Visualisasi** matriks kunci 6×6
- **Log proses**: Key Asli, Plain/Cipher Text Asli, Teks Normal, Teks Siap (digram)
- **Opsi simpan/buka file**:
  - Enkripsi: simpan ciphertext ke file `.txt`
  - Dekripsi: buka ciphertext dari file `.txt`

## Cara Kerja Singkat

- Teks diproses per **bigram** (pasangan karakter)
- Aturan Playfair pada grid 6×6:
  - Baris sama: geser kanan (enkripsi) / kiri (dekripsi)
  - Kolom sama: geser bawah (enkripsi) / atas (dekripsi)
  - Persegi panjang: tukar kolom (ambil sudut persegi)
  - Wrapping menggunakan modulo 6
- Penanganan teks:
  - Karakter berulang dalam satu bigram disisipi **'X'** (mis. HELLO → HELXLO)
  - Panjang ganjil dipad dengan **'Z'** di akhir

## Menjalankan Program

```bash
python playfair-main.py
```

## Alur Prompt (Interaktif)

1. `Pilih mode Enkripsi (E) atau Dekripsi (D):`
2. `Masukkan key:`
3. Jika Enkripsi: `Masukkan plain text:`
   - Program menampilkan tabel kunci 6×6 dan log proses
   - Opsi: `Apakah Anda ingin menyimpan hasil enkripsi ke file? (Y/N)`
4. Jika Dekripsi:
   - Opsi: `Apakah Anda ingin membuka hasil dekripsi dari file? (Y/N)`
   - Jika tidak, `Masukkan cipher text:`
   - Program menampilkan tabel kunci 6×6 dan log proses

## Contoh Enkripsi

```
Pilih mode Enkripsi (E) atau Dekripsi (D): E
Masukkan key: SECRET123
Masukkan plain text: PROGRAMMING2024

Playfair Key Table (6x6):
+-------------+
| S E C R T 1 |
| 2 3 A B D F |
| G H I J K L |
| M N O P Q U |
| V W X Y Z 0 |
| 4 5 6 7 8 9 |
+-------------+

--- Proses Enkripsi ---
Key Asli       : SECRET123
Plain Text Asli: PROGRAMMING2024
Teks Normal    : PROGRAMMING2024
Teks Siap      : PR OG RA MM IN G2 02 4Z

Cipher Text    : YBMICBOVHOMGVF6V
```

## Contoh Dekripsi (buka dari file optional)

```
Pilih mode Enkripsi (E) atau Dekripsi (D): D
Masukkan key: SECRET123
Apakah Anda ingin membuka hasil dekripsi dari file? (Y/N): N
Masukkan cipher text: YBMICBOVHOMGVF6V

Playfair Key Table (6x6):
+-------------+
| S E C R T 1 |
| 2 3 A B D F |
| G H I J K L |
| M N O P Q U |
| V W X Y Z 0 |
| 4 5 6 7 8 9 |
+-------------+

--- Proses Dekripsi ---
Key Asli         : SECRET123
Cipher Text Asli : YBMICBOVHOMGVF6V
Cipher Teks Normal: YBMICBOVHOMGVF6V

Hasil Plain Text : PROXRAMXING2024
```

Catatan: Tanda **X** dan **Z** yang ditambahkan saat enkripsi tidak dihapus otomatis saat dekripsi. Anda bisa menghilangkannya secara manual jika dibutuhkan.

## Persyaratan

- Python 3.6+
- Tidak ada dependensi tambahan

---

Program edukasi untuk pembelajaran kriptografi klasik yang disesuaikan dengan data alfanumerik modern.
