# Definisi set karakter A-Z dan 0-9
ALPHANUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def normalizeInput(text):
    text = text.upper() # Ubah ke huruf besar
    text = ''.join(filter(str.isalnum, text)) # Hapus karakter non-alfanumerik
    return text

def generateKeyTable(key, keyT):
    # Membuat matriks 6x6 berdasarkan key yang diberikan
    keyT.clear()
    for _ in range(6):
        keyT.append([''] * 6)

    # Menggunakan set untuk efisiensi pengecekan karakter yang sudah ada
    seen = set()
    temp_key = ""
    for char in key:
        if char not in seen:
            seen.add(char)
            temp_key += char

    # Tambahkan sisa karakter dari ALPHANUM
    for char in ALPHANUM:
        if char not in seen:
            temp_key += char

    # Isi matriks 6x6
    idx = 0
    for i in range(6):
        for j in range(6):
            keyT[i][j] = temp_key[idx]
            idx += 1

def printKeyTable(keyT):
    # Mencetak matriks 6x6 dengan format yang rapi.
    print("\nPlayfair Key Table (6x6):")
    print("+" + "-" * 13 + "+")
    for i in range(6):
        print("|", end="")
        for j in range(6):
            print(f" {keyT[i][j]}", end="")
        print(" |")
    print("+" + "-" * 13 + "+")

def search(keyT, char):
    # Mencari posisi (baris, kolom) sebuah karakter dalam matriks.
    for i in range(6):
        for j in range(6):
            if keyT[i][j] == char:
                return (i, j)
    return (None, None) # Seharusnya tidak pernah terjadi dengan input yang valid

def prepare(plain_text):
    # Mempersiapkan plaintext:
    # Menyisipkan 'X' di antara karakter yang sama dalam satu bigram.
    
    text_list = list(plain_text)
    i = 0
    while i < len(text_list) - 1:
        if text_list[i] == text_list[i+1]:
            text_list.insert(i + 1, 'X')
        i += 2
    
    # Memastikan panjang teks genap dengan menambahkan 'Z' jika perlu.
    if len(text_list) % 2 != 0:
        text_list.append('Z')
        
    return "".join(text_list)

def process_bigram(bigram, keyT, mode):
    # Memproses satu bigram (dua karakter) untuk enkripsi atau dekripsi.

    char1, char2 = bigram[0], bigram[1]
    row1, col1 = search(keyT, char1)
    row2, col2 = search(keyT, char2)
    
    # Aturan Playfair untuk matriks 6x6
    # Modulo 6: (x + shift) % 6. Untuk dekripsi, shift negatif.
    # (x - 1) % 6 sama dengan (x + 5) % 6
    shift = 1 if mode == 'encrypt' else 5

    if row1 == row2: # Karakter berada di baris yang sama
        return keyT[row1][(col1 + shift) % 6] + keyT[row2][(col2 + shift) % 6]
    elif col1 == col2: # Karakter berada di kolom yang sama
        return keyT[(row1 + shift) % 6][col1] + keyT[(row2 + shift) % 6][col2]
    else: # Karakter membentuk persegi
        return keyT[row1][col2] + keyT[row2][col1]

def playfair_cipher(text, keyT, mode):
    # Fungsi utama untuk enkripsi atau dekripsi seluruh teks.
    result = []
    for i in range(0, len(text), 2):
        bigram = text[i:i+2]
        processed = process_bigram(bigram, keyT, mode)
        result.append(processed)
    return "".join(result)

def main():
    
    while True:
        choice = input("Pilih mode Enkripsi (E) atau Dekripsi (D): ").strip().upper()
        if choice in ['E', 'D']:
            break
        print("Pilihan tidak valid. Silakan masukkan 'E' atau 'D'.")

    key = input("Masukkan key: ").strip()
    
    if choice == 'E':
        text = input("Masukkan plain text: ").strip()
        
        normalized_key = normalizeInput(key)
        normalized_text = normalizeInput(text)
        prepared_text = prepare(normalized_text)
        
        keyT = []
        generateKeyTable(normalized_key, keyT)
        printKeyTable(keyT)
        
        print("\n--- Proses Enkripsi ---")
        print(f"Key Asli       : {key}")
        print(f"Plain Text Asli: {text}")
        print(f"Teks Normal    : {normalized_text}")
        print(f"Teks Siap      : {' '.join([prepared_text[i:i+2] for i in range(0, len(prepared_text), 2)])}")
        
        cipher_text = playfair_cipher(prepared_text, keyT, 'encrypt')
        print(f"\nCipher Text    : {cipher_text}")
        
    elif choice == 'D':
        text = input("Masukkan cipher text: ").strip()
        
        normalized_key = normalizeInput(key)
        normalized_text = normalizeInput(text) # Ciphertext juga dinormalisasi
        
        keyT = []
        generateKeyTable(normalized_key, keyT)
        printKeyTable(keyT)
        
        print("\n--- Proses Dekripsi ---")
        print(f"Key Asli         : {key}")
        print(f"Cipher Text Asli : {text}")
        print(f"Cipher Teks Normal: {normalized_text}")
        
        plain_text = playfair_cipher(normalized_text, keyT, 'decrypt')
        print(f"\nHasil Plain Text : {plain_text}")


if __name__ == "__main__":
    main()