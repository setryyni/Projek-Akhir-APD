from main import keranjang_belanja
import questionary
import sys
import os

# Tambahkan path parent directory agar bisa import dari Program/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from main import daftar_barang, riwayat_transaksi
from datetime import datetime

def Lanjut_Pembayaran():
    #kalau tidak ada produk di keranjang belanja
    try:
        not keranjang_belanja
    except ValueError:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
    
    opsi_lanjut = questionary.confirm("Apakah Anda ingin melakukan pembayaran?").ask()
    if opsi_lanjut == True:
        print("\nBerhasil melakukan pembelian! Terima kasih telah berbelanja di KlikCodemaret.\n")
         # Simpan snapshot keranjang beserta waktu transaksi
        riwayat_transaksi.append({
            "waktu": datetime.now(),
            "items": keranjang_belanja.copy()
        })
        keranjang_belanja.clear()
        print("Kembali ke menu customer...\n")
        # return menuCustomer()\
        #disini seharusnya kembali ke menu customer
        pass
    elif opsi_lanjut == False:
        print("\nTransaksi dibatalkan. Kembali ke menu customer...\n")
        # return menuCustomer()
        #disini seharusnya kembali ke menu customer
        pass
    else:
        print("\n!! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi. !!\n")
        return Lanjut_Pembayaran()