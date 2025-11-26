import questionary as qs
from fungsi import clear_terminal
import sys, variabel_global as var


# Fungsi Register Yang Mengambilakan Nilai berupa hak user dan username
# Selain itu Keluar dari Program
def register():
    while True:
        pilihan = qs.select("", ["Register", "Login", "Keluar"]).ask()
        match pilihan:

            case "Register":
                username = qs.text("Input Username : ").ask()
                password = qs.password("Input Password : ").ask()
                if password == "" or username == "":
                    clear_terminal()
                    print("Password atau Username Tidak Boleh Kosong")
                    continue
                username_akun = [i["username"] for i in var.akun.values()]
                if username in username_akun:
                    clear_terminal()
                    print("Username Telah Digunakan")
                    continue
                elif not (username in username_akun):
                    if len(password) < 8:
                        print("Password Minimal 8 Karakter")
                        continue

                    banyak_akun = len(var.akun.values()) + 1
                    var.akun[banyak_akun] = {
                        "username": username,
                        "password": password,
                        "hak": "user",
                    }
                    var.keranjang_belanja[username] = {}
                    var.riwayat_transaksi[username] = {}
                    var.history_pesanan[username] = {}
                    print("Akun Berhasil Di Buat")
                    continue

            case "Login":
                username = qs.text("Input Username : ").ask()
                password = qs.text("Input Password : ").ask()
                for id, akun in var.akun.items():
                    if username == akun["username"] and password == akun["password"]:
                        return {"username": akun["username"], "hak": akun["hak"]}
                    elif username == akun["username"] and password != akun["password"]:
                        print("Password Salah")
                        return {"username": 0, "hak": 0}
                print("Akun Tidak Di Temukan")
                return {"username": 0, "hak": 0}

            case "Keluar":
                sys.exit()
