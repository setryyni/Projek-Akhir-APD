import questionary
from prettytable import PrettyTable
import sys
import os

# Tambahkan path parent directory agar bisa import dari Program/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from main import daftar_barang, keranjang_belanja

def Questionary():
    questionary.text("What's your first name").ask()
    questionary.password("What's your secret?").ask()
    questionary.confirm("Are you amazed?").ask()

    questionary.select(
        "What do you want to do?",
        choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
    ).ask()

    questionary.rawselect(
        "What do you want to do?",
        choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],
    ).ask()

    questionary.checkbox(
        "Select toppings", choices=["foo", "bar", "bazz"]
    ).ask()

    questionary.path("Path to the projects version file").ask()
Questionary()
def menu_keranjang():
    pilihan = questionary.select(
        "Menu Keranjang Belanja:",
        choices=[
            "Lihat Daftar Keranjang Belanja",
            "Lanjut ke Pembayaran",
            "Tambah Barang ke Keranjang",
            "Hapus Barang dari Keranjang",
            "Kembali ke Menu Utama",
        ],
    ).ask()

    match pilihan:
        case "Lihat Daftar Keranjang Belanja":
            daftar_keranjang_belanja()
        case "Lanjut ke Pembayaran":
            from lanjut_pembayaran import Lanjut_Pembayaran
            Lanjut_Pembayaran()
        case "Tambah Barang ke Keranjang":
            # fungsi untuk menambah barang ke keranjang
            pass
        case "Hapus Barang dari Keranjang":
            # fungsi untuk menghapus barang dari keranjang
            pass
        case "Kembali ke Menu Utama":
            # fungsi untuk kembali ke menu utama
            pass

def daftar_keranjang_belanja():
    #deklarasi tabel_keranjang sebagai objek PrettyTable
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
            nama = daftar_barang[product_id]['nama']
            harga = daftar_barang[product_id]['harga']
            subtotal = harga * jumlah
            total += subtotal
            tabel_keranjang.add_row([i, nama, jumlah, f"Rp.{subtotal:,}"])
        tabel_keranjang.add_row(["", "", "Total:", f"Rp.{total:,}"])
        print(tabel_keranjang)
        menu_keranjang()
        #kembali  ke menu keranjang belanja