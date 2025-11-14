import questionary as qs
from fungsi import clear_terminal
import sys


# Fungsi Register Yang Mengambilakan Nilai berupa hak user dan username
# Selain itu Keluar dari Program
def register(penyimpanan_akun: dict) -> dict:
    while True:
        hitung = 1
        print(penyimpanan_akun)
        pilihan = qs.select("", ["Register", "Login", "Keluar"]).ask()
        match pilihan:

            case "Register":
                username = input("Input Username : ")
                password = input("Input Password : ")
                if password == "" or username == "":
                    clear_terminal()
                    print("Password atau Username Tidak Boleh Kosong")
                    continue
                for i in penyimpanan_akun.values():
                    if username == i["username"]:
                        clear_terminal()
                        print("Username Telah Digunakan")
                        break
                    elif username != i["username"] and hitung == len(penyimpanan_akun):
                        banyak_akun = len(penyimpanan_akun)
                        penyimpanan_akun[banyak_akun + 1] = {
                            "username": username,
                            "password": password,
                            "hak": "user",
                        }
                        print("Akun Berhasil Di Buat")
                        break

            case "Login":
                username = input("Input Username : ")
                password = input("Input Password : ")
                for i in penyimpanan_akun.values():
                    if i["username"] == username and i["password"] == password:
                        if i["hak"] == "admin":
                            return [i["username"], i["hak"]]
                        elif i["hak"] == "user":
                            return [i["username"], i["hak"]]
                        else:
                            return "Keluar"
                    elif i["username"] != username and i["password"] != password and hitung == len(penyimpanan_akun):
                        print("Username Atau Password Salah")
                    else:
                        print("Akun Belum Di Buat")
            case "Keluar":
                sys.exit()
