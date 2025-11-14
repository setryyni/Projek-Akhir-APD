import questionary  # import questionary module for interactive command line prompts


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

    questionary.checkbox("Select toppings", choices=["foo", "bar", "bazz"]).ask()

    questionary.path("Path to the projects version file").ask()


def menu_Keranjang():
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
            from daftar_keranjang_belanja import daftar_Keranjang_Belanja

            daftar_Keranjang_Belanja()
        case "Lanjut ke Pembayaran":
            from lanjut_pembayaran import Lanjut_Pembayaran

            Lanjut_Pembayaran()
        case "Tambah Barang ke Keranjang":
            # fungsi untuk menambah barang ke keranjang
            pass
        case "Hapus Barang dari Keranjang":
            # fungsi untuk menghapus barang dari keranjang
            pass
        case "Kembali ke Menu Utama User":
            # fungsi untuk kembali ke menu utama user
            pass


menu_Keranjang()
