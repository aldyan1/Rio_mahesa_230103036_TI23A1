import os, csv, json, logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

try:
    os.makedirs("data", exist_ok=True)
    logging.info("Mulai proses...")

    with open("data/presensi.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerows([
            ["2310001", "Rio", 1],
            ["2310002", "Sinta", 0],
            ["2310003", "Rafi", 1]
        ])

    with open("data/presensi.csv") as f:
        data = list(csv.DictReader(f))
        total = len(data)
        hadir = sum(int(d["hadir_uts"]) for d in data)
        persen = (hadir / total) * 100

    with open("data/ringkasan.json", "w") as f:
        json.dump({"total": total, "hadir": hadir, "persentase": f"{persen:.2f}%"}, f, indent=4)

    logging.info("Proses selesai sukses.")

except Exception as e:
    logging.error(f"Terjadi error: {e}")
