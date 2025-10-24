def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari yang dimasukkan.
    """
    jadwal = {
        "Senin": ["Algoritma", "Basis Data"],
        "Selasa": ["Pemrograman", "Sistem Operasi"],
        "Rabu": ["Jaringan Komputer"],
        "Kamis": ["Kecerdasan Buatan"],
        "Jumat": ["Pemrograman Visual"]
    }

    if hari in jadwal:
        print(f"Jadwal hari {hari}: {', '.join(jadwal[hari])}")
    else:
        print("Tidak ada jadwal untuk hari tersebut.")


hari_input = input("Masukkan hari: ")
jadwal_hari(hari_input.capitalize())
