def normalizeInput (plainT):
    plainT = plainT.lower() # ubah ke huruf kecil
    plainT = plainT.replace(" ", "") # hilangkan spasi
    plainT = ''.join(filter(str.isalpha, plainT)) # hilangkan karakter non-alfabet
    return plainT

# Generate matriks 5x5 dari key
def generateKeyTable(key, keyT):
    n = len(key)

    keyT.clear()
    for i in range(5):
        keyT.append([0]*5)

    hashMap = [0]*26

    for i in range(n):
        if key[i] != 'j':
            hashMap[ord(key[i]) - 97] = 2

    hashMap[ord('j') - 97] = 1

    i = 0
    j = 0

    for k in range(n):
        if hashMap[ord(key[k]) - 97] == 2:
            hashMap[ord(key[k]) - 97] -= 1
            keyT[i][j] = key[k]
            j += 1
            if j == 5:
                i += 1
                j = 0

    for k in range(26):
        if hashMap[k] == 0:
            keyT[i][j] = chr(k + 97)
            j += 1
            if j == 5:
                i += 1
                j = 0

# Print matriks 5x5
def printKeyTable(keyT):
    print("\nPlayfair Key Table:")
    print("+" + "-" * 11 + "+")
    for i in range(5):
        print("|", end="")
        for j in range(5):
            print(f" {keyT[i][j]}", end="")
        print(" |")
    print("+" + "-" * 11 + "+")

# Searching karakter dalam matriks 5x5 dan mengembalikan posisinya
def search(keyT, a, b, arr):
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a:
                arr[0] = i
                arr[1] = j
            elif keyT[i][j] == b:
                arr[2] = i
                arr[3] = j

# Mengubah panjang plain text menjadi genap
def prepare(string):
    if len(string) % 2 != 0:
        string += 'z'
    return string

# Fungsi untuk enkripsi dan dekripsi
def encrypt(string, keyT):
    n = len(string)
    arr = [0]*4

    result = list(string)
    for i in range(0, n, 2):
        search(keyT, result[i], result[i+1], arr)

        if arr[0] == arr[2]:
            result[i] = keyT[arr[0]][(arr[1] + 1) % 5]
            result[i+1] = keyT[arr[0]][(arr[3] + 1) % 5]
        elif arr[1] == arr[3]:
            result[i] = keyT[(arr[0] + 1) % 5][arr[1]]
            result[i+1] = keyT[(arr[2] + 1) % 5][arr[1]]
        else:
            result[i] = keyT[arr[0]][arr[3]]
            result[i+1] = keyT[arr[2]][arr[1]]

    return ''.join(result)

def decrypt(string, keyT):
    n = len(string)
    arr = [0]*4

    result = list(string)
    for i in range(0, n, 2):
        search(keyT, result[i], result[i+1], arr)

        if arr[0] == arr[2]:
            result[i] = keyT[arr[0]][(arr[1] + 4) % 5]
            result[i+1] = keyT[arr[0]][(arr[3] + 4) % 5]
        elif arr[1] == arr[3]:
            result[i] = keyT[(arr[0] + 4) % 5][arr[1]]
            result[i+1] = keyT[(arr[2] + 4) % 5][arr[1]]
        else:
            result[i] = keyT[arr[0]][arr[3]]
            result[i+1] = keyT[arr[2]][arr[1]]

    return ''.join(result)

# Wrapper 
def encryptByPlayfairCipher(string, key):
    keyT = []
    key = normalizeInput(key)
    string = normalizeInput(string)
    string = prepare(string)
    generateKeyTable(key, keyT)
    return encrypt(string, keyT)

def decryptByPlayfairCipher(string, key):
    keyT = []
    key = normalizeInput(key)
    string = normalizeInput(string)
    string = prepare(string)
    generateKeyTable(key, keyT)
    return decrypt(string, keyT)

def main():
    choice = input("Encrypt or Decrypt (E/D): ").strip().upper()
    if choice == 'E':
        key = input("Enter the key: ").strip()
        string = input("Enter the plain text: ").strip()
        print("Key text:", key)
        print("Plain text:", string)
        
        keyT = []
        normalizedKey = normalizeInput(key)
        generateKeyTable(normalizedKey, keyT)
        printKeyTable(keyT)
        
        string = encryptByPlayfairCipher(string, key)
        print("Cipher text:", string)
    else:
        key = input("Enter the key: ").strip()
        string = input("Enter the cipher text: ").strip()
        print("Key text:", key)
        print("Cipher text:", string)
        
        keyT = []
        normalizedKey = normalizeInput(key)
        generateKeyTable(normalizedKey, keyT)
        printKeyTable(keyT)
        
        string = decryptByPlayfairCipher(string, key)
        print("Plain text:", string)


if __name__ == "__main__":
    main()