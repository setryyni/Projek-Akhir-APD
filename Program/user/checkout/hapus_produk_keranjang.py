from prettytable import PrettyTable
import sys  # import sys module untuk memanipulasi path
import os  # import os module untuk mendapatkan path file
from prettytable import PrettyTable  # import PrettyTable untuk membuat tabel yang rapi

# Tambahkan path parent directory agar bisa import dari Program/
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)  # menambahkan path parent directory ke sys.path agar bisa mengimpor modul dari folder Program
from main import (
    daftar_barang,
    keranjang_belanja,
)  # import daftar_barang dan keranjang_belanja dari main.py

# from keranjang_belanja import menu_keranjang #import menu_keranjang dari keranjang_belanja.py


def hapus_Produk_Keranjang():
    tabel_hapus = PrettyTable()
    # DEKLARASI tabelHapus_dariKeranjang
    tabelHapus_dariKeranjang = PrettyTable()
    print("\nHapus produk dari keranjang belanja...\n")
    if not keranjang_belanja:  # Cek apakah keranjang belanja kosong
        print("Keranjang belanja kosong.")
        # kembaliKeMenu(menuCustomer) #kembali ke menu user
        pass
    else:  # Jika tidak kosong, tampilkan isi keranjang belanja
        items = list(keranjang_belanja.items())
        for no_id, (id_produk, jumlah) in enumerate(items, 1):
            nama = daftar_barang[id_produk]["nama"]
            harga = daftar_barang[id_produk]["harga"]
            # Prettytable tabelHapus_dariKeranjang
            tabelHapus_dariKeranjang.field_names = [
                "No",
                "Nama Produk",
                "Jumlah",
                "Harga",
            ]
            tabelHapus_dariKeranjang.add_row([no_id, nama, jumlah, f"Rp.{harga * jumlah:,}"])
        tabelHapus_dariKeranjang.align["Nama Produk"] = "l"
        tabelHapus_dariKeranjang.align["Harga"] = "l"
        print(tabelHapus_dariKeranjang)
        hapus_produk = input("\nMasukkan nomor produk yang ingin dihapus: ")
        if hapus_produk.isdigit():
            hapus_noId = int(hapus_produk)
            if 1 <= hapus_noId <= len(items):
                id_produk_to_remove = items[hapus_noId - 1][0]
                del keranjang_belanja[id_produk_to_remove]
                print("\n- Produk berhasil dihapus dari keranjang belanja.")
                # opsiLagi(menu_keranjang, "Hapus produk lagi dari keranjang?", opsiHapusDariKeranjang)
                # disini harusnya ada output nanya ntuk coba lagi...
                pass
            else:
                print("\n!! Nomor produk tidak valid. Silahkan coba lagi. !!\n")
                return hapus_Produk_Keranjang()
        else:
            print("\n! Tolong ikuti instruksi yang tersedia. Silahkan coba lagi.\n")
            return hapus_Produk_Keranjang()
