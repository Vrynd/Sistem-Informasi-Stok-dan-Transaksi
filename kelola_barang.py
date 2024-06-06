from datetime import datetime
class Node:
    def __init__(self, noSku, namaBarang, jumlahStokBarang, hargaBarang):
        self.noSku = noSku
        self.namaBarang = namaBarang
        self.jumlahStokBarang = jumlahStokBarang
        self.hargaBarang = hargaBarang
        self.right = None
        self.left = None

class StokBarang:
    def __init__(self):
        self.root = None

    def InputDataStokBarang(self):
        no_sku = int(input("Masukkan No.SKU 4 Digit Angka [1234] : "))
        nama_barang = input("Masukkan Nama Barang : ")
        jumlah_stok = int(input("Masukkan Jumlah Barang : "))
        harga_satuan = float(input("Masukkan Harga Satuan : "))
        if self.CroscheckBarang(no_sku) is not None:
            print(f"Barang Dengan No.SKU {no_sku} Sudah Ada")
        else:
            new_node = Node(no_sku, nama_barang, jumlah_stok, harga_satuan)
            if self.root is None:
                self.root = new_node
            else:
                temp = self.root
                while True:
                    if no_sku < temp.noSku:
                        if temp.left is None:
                            temp.left = new_node
                            break
                        temp = temp.left
                    else:
                        if temp.right is None:
                            temp.right = new_node
                            break
                        temp = temp.right
            print(f"Barang Dengan No.SKU {no_sku} Berhasil Ditambahkan")
        return True

    def CroscheckBarang(self, no_sku):
        temp = self.root
        while (temp is not None):
            if no_sku < temp.noSku:
                temp = temp.left
            elif no_sku > temp.noSku:
                temp = temp.right
            else :
                return temp
        return None

    def RestokBarang(self):
        no_sku = int(input("Masukkan No.SKU Barang : "))
        temp = self.CroscheckBarang(no_sku)
        if temp is None:
            print(f"Barang Dengan No.SKU {no_sku} Belum Terdaftar! Lakukan Penginputan Dulu")
            input_barang = input("Apakah ingin menginputkan barang [Y/N] : ")
            if input_barang != 'Y' and input_barang != 'y':
                self.InputDataStokBarang()
                print(f"Berhasil Menambahkan Barang Dengan No.SKU {no_sku}")
        else:
            stok_baru = int(input("Masukkan Jumlah Stok Baru : "))
            totalStok = temp.jumlahStokBarang + stok_baru
            temp.jumlahStokBarang = totalStok
            print(f"Berhasil Menambah Stok Barang dengan No.SKU {no_sku}")
            print(f"Jumlah Stok Barang Sekarang = {totalStok}")

class TransaksiKonsumen:
    def __init__(self):
        self.transaksi = StokBarang()
        self.data_transaksi = []
        self.riwayat_transaksi = []

    def InputDataTransaksi(self):
        nama_konsumen = input("Masukkan Nama Konsumen: ")
        while True:
            sku_beli = int(input("Masukkan No.SKU Barang Yang Dibeli: "))
            temp = self.transaksi.CroscheckBarang(sku_beli)
            if temp is None:
                print(f"Barang Dengan No.SKU {sku_beli} Belum Terdaftar.")
                lanjut_transaksi = input("Apakah ingin melanjutkan transaksi [Y/N] : ")
                if lanjut_transaksi != 'Y' and lanjut_transaksi != 'y':
                    break
            else:
                jumlah_beli = int(input("Masukkan Jumlah Barang Yang Dibeli: "))
                if temp.jumlahStokBarang >= jumlah_beli:
                    waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    temp.jumlahStokBarang -= jumlah_beli
                    subtotal = temp.hargaBarang * jumlah_beli
                    transaksi_list = [nama_konsumen, temp.namaBarang, sku_beli, jumlah_beli, subtotal,
                                    waktu_transaksi]
                    self.data_transaksi.append(transaksi_list)
                    self.riwayat_transaksi.append([nama_konsumen, temp.namaBarang, waktu_transaksi.split(' ')[0],
                                                waktu_transaksi.split(' ')[1]])
                    print(f"Data Transaksi Konsumen a.n {nama_konsumen} Berhasil Ditambahkan")
                    print(f"Sisa Stok Barang = {temp.jumlahStokBarang}")
                    transaksi_lagi = input(f"Apakah ingin menambahkan data pembelian untuk konsumen a.n {nama_konsumen} [Y/N] : ")
                    if transaksi_lagi != 'Y' and transaksi_lagi != 'y':
                        break
                else:
                    print(f"Jumlah Stok Barang dengan No.SKU {sku_beli} Tidak Mencukupi.")
                    lanjut_transaksi = input("Apakah ingin melanjutkan transaksi [Y/N] : ")
                    if lanjut_transaksi != 'Y' and lanjut_transaksi != 'y':
                        break

    def LihatDataTransaksi(self):
        if self.data_transaksi:
            print("Berikut Data Transaksi Seluruh Konsumen")
            print("="*75)
            print("{:<20}{:<20}{:<10}{:<15}{:<12}".format("Nama Konsumen", "Nama Barang", "No.Sku ", "Jumlah", "Subtotal"))
            print("="*75)
            for transaksi in self.data_transaksi:
                nominal = "{:,.0f}".format(transaksi[4]).replace(",", ".")
                print("{:<20}{:<20}{:<10}{:<15}{:<12}".format(transaksi[0], transaksi[1], transaksi[2], transaksi[3], nominal))
                print("-"*75)
        else:
            print("* Belum ada transaksi yang dilakukan!")


    def LihatDataTransaksiSubtotal(self):
        for i in range (len(self.data_transaksi)-1, 0, -1):
            for j in range(i):
                if self.data_transaksi[j][4] < self.data_transaksi[j+1][4]:
                    temp = self.data_transaksi[j]
                    self.data_transaksi[j] = self.data_transaksi[j+1]
                    self.data_transaksi[j+1] = temp
        if self.data_transaksi:
            print("Berikut Data Transaksi Konsumen Berdasarkan Subtotal")
            print("="*75)
            print("{:<20}{:<20}{:<10}{:<15}{:<12}".format("Nama Konsumen", "Nama Barang", "No.Sku ", "Jumlah", "Subtotal"))
            print("="*75)
            for transaksi in self.data_transaksi:
                nominal = "{:,.0f}".format(transaksi[4]).replace(",", ".")
                print("{:<20}{:<20}{:<10}{:<15}{:<12}".format(transaksi[0], transaksi[1], transaksi[2], transaksi[3], nominal))
                print("-"*75)
        else:
            print("* Belum ada transaksi yang dilakukan!!")

    def LihatRiwayatTransaksi(self):
        if self.riwayat_transaksi:
            print("Berikut Riwayat Transaksi")
            print("="*65)
            print("{:<20}{:<20}{:<20}{:<20}".format("Nama Konsumen", "Nama Barang", "Tanggal", "Waktu"))
            print("="*65)
            for riwayat in self.riwayat_transaksi:
                print("{:<20}{:<20}{:<20}{:<20}".format(riwayat[0], riwayat[1], riwayat[2], riwayat[3]))
                print("-"*65)
        else:
            print("* Belum ada riwayat transaksi yang dilakukan!")
