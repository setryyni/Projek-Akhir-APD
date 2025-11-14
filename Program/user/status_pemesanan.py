from datetime import datetime
from prettytable import PrettyTable
import questionary as qs


def status(riwayat_transaksi, history_pesanan, username):
    simpan_barang = []
    if riwayat_transaksi:
        # Menampilkan Riwayat Barang Dalam Tabel
        tabel_riwayat = PrettyTable()
        tabel_riwayat.field_names = ["No", "Nama", "Jumlah", "Sub Total"]
        for i, value in enumerate(riwayat_transaksi["items"].values(), start=1):
            simpan_barang.append(i)
            for j in value.values():
                simpan_barang.append(j)
            tabel_riwayat.add_row(simpan_barang.copy())
            simpan_barang.clear()
        print(tabel_riwayat)

        # Cek Barang Sudah Sampai Atau Belum
        if riwayat_transaksi["waktu_estimasi"] <= datetime.now():
            print("Pesanan Telah Sampai Di Tujuan Silahkan Konfirmasi Pesanan")
            pilihan = qs.select(
                "Konfirmasi Pesanan", ["Konfirmasi Pesanan", "Ajukan Pengembalian"]
            ).ask()
            if pilihan == "Konfirmasi Pesanan":
                print("Terimakasih Telah Berbelanja")
                history_pesanan.append(riwayat_transaksi.copy())
                history_pesanan["username"] = username
                riwayat_transaksi.clear()
            else:
                print("Pesanan Akan Di Kembalikan")
                riwayat_transaksi.clear()
        else:
            print(
                f"Barang Akan Sampai Dalam {riwayat_transaksi["waktu_estimasi"].minute}"
            )
