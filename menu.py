from kelola_barang import TransaksiKonsumen, StokBarang
import os

def Dashboard():
    mytransaki = TransaksiKonsumen()
    while True:
        print("*"*5, "MENU UTAMA", "*"*5)
        print("1. Kelola Stok Barang")
        print("2. Kelola Transaksi Konsumen")
        print("0. Keluar Program")
        menu = input(">> Masukkan Pilihan Menu [1/2/3] : ")
        os.system('cls')
        if menu == "1":
            while True:
                print("*"*5, "Menu Kelola Barang", "*"*5)
                print("1.1 Input Data Stok Barang")
                print("1.2 Restok Barang")
                print("0.  Kembali Ke Menu Utama")
                pilih = input(">> Masukkan Pilihan Menu [1.1/1.2/0] : ")
                os.system('cls')
                if pilih == "1.1":
                    mytransaki.transaksi.InputDataStokBarang()
                elif pilih == "1.2":
                    mytransaki.transaksi.RestokBarang()
                elif pilih == "0":
                    break
        elif menu == "2":
            while True:
                print("*"*5, "Menu Transaksi Konsumen", "*"*5)
                print("2.1 Input Data Transaksi Baru")
                print("2.2 Lihat Data Seluruh Transaksi Konsumen")
                print("2.3 Lihat Data Transaksi Berdasarkan Subtotal")
                print("2.4 Riwayat Transaksi")
                print("0.  Kembali Ke Menu Utama")
                pilih = input(">> Masukkan Pilihan Menu [2.1/2.2/2.3/0] : ")
                os.system('cls')
                if pilih == "2.1":
                    mytransaki.InputDataTransaksi()
                elif pilih == "2.2":
                    mytransaki.LihatDataTransaksi()
                elif pilih == "2.3":
                    mytransaki.LihatDataTransaksiSubtotal()
                elif pilih == "2.4":
                    mytransaki.LihatRiwayatTransaksi()
                elif pilih == "0":
                    break
        elif menu == "0":
            print("Anda Telah Keluar Dari Program!")
            exit()
        else:
            print("Menu Tidak Tersedia, Silahkan Coba Lagi!")
            coba_lagi = input(">> Pilih Menu Lagi [Y/T] : ")
            if coba_lagi != 'Y' and coba_lagi != "y":
                print("Program Berakhir!")
                break
if __name__ == "__main__":
    Dashboard()