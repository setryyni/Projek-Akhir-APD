import sys  # import sys module untuk memanipulasi path import os  # import os module untuk mendapatkan path file
from prettytable import PrettyTable  # import PrettyTable untuk membuat tabel yang rapi

# Tambahkan path parent directory agar bisa import dari Program/
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)  # menambahkan path parent directory ke sys.path agar bisa mengimpor modul dari folder Program
from main import (
    daftar_barang,
    keranjang_belanja,
)  # import daftar_barang dan keranjang_belanja dari main.py
from keranjang_belanja import (
    menu_keranjang,
)  # import menu_keranjang dari keranjang_belanja.py


def daftar_Keranjang_Belanja():
    # deklarasi tabel_keranjang sebagai objek PrettyTable
    tabel_keranjang = PrettyTable()
    tabel_keranjang.field_names = ["No", "Nama Produk", "Jumlah", "Subtotal"]
    print("")
    tabel_keranjang.align["Nama Produk"] = "l"
    tabel_keranjang.align["Subtotal"] = "l"
    if not keranjang_belanja:
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer)
        # #setelah ini seharusnya akan kembali ke menu user
    else:
        total = 0
        for i, (product_id, jumlah) in enumerate(keranjang_belanja.items(), 1):
            nama = daftar_barang[product_id]["nama"]
            harga = daftar_barang[product_id]["harga"]
            subtotal = harga * jumlah
            total += subtotal
            tabel_keranjang.add_row([i, nama, jumlah, f"Rp.{subtotal:,}"])
        tabel_keranjang.add_row(["", "", "Total:", f"Rp.{total:,}"])
        print(tabel_keranjang)
        menu_keranjang()
        # kembali  ke menu keranjang belanja
