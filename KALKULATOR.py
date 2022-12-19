print("SELAMAT DATANG DI INDOMARET TAMATIRT0 01")

# Meminta input nama pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")

# Meminta input jumlah barang yang dibeli
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

# Meminta input harga satuan untuk setiap barang
harga_satuan = float(input("Masukkan harga satuan untuk setiap barang: "))

# Menghitung total harga yang harus dibayar
total_harga = jumlah_barang * harga_satuan

# Menampilkan struk belanja ke layar
print("==========STRUK BELANJA==========")
print("Nama pelanggan:", nama_pelanggan)
print("Jumlah barang:", jumlah_barang)
print("Harga satuan:", harga_satuan)
print("Total harga:", total_harga)
print("Terima kasih atas kunjungan Anda!")
print("tidak percaya dengan total harga tersebut ?")
print("Anda dapat mencoba menjumlahkan total belanjaan anda secara manual di bawah ini")

# Kalkulator sederhana

# Fungsi untuk menambah dua bilangan
def tambah(x, y):
   return x + y

# Fungsi untuk mengurangi dua bilangan
def kurang(x, y):
   return x - y

# Fungsi untuk mengalikan dua bilangan
def kali(x, y):
   return x * y

# Fungsi untuk membagi dua bilangan
def bagi(x, y):
   return x / y

print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

# Meminta input dari user
pilihan = input("Masukkan pilihan (1/2/3/4): ")

bilangan1 = int(input("Masukkan Jumlah barang belanja: "))
bilangan2 = int(input("Masukkan harga satuan nya: "))

if pilihan == '1':
   print(bilangan1,"+",bilangan2,"=", tambah(bilangan1,bilangan2))

elif pilihan == '2':
   print(bilangan1,"-",bilangan2,"=", kurang(bilangan1,bilangan2))

elif pilihan == '3':
   print(bilangan1,"*",bilangan2,"=", kali(bilangan1,bilangan2))

elif pilihan == '4':
   print(bilangan1,"/",bilangan2,"=", bagi(bilangan1,bilangan2))
else:
   print("Input salah")