# Nama file CSV
import os
filename = "dataset.csv"

# Baca CSV manual
proses = []
alokasi = []
request = []
def main():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "data", "dataset.csv")
        with open(file_path, "r") as f:
            next(f)  # skip header
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                proses.append(parts[0])
                alokasi.append(parts[1])
                request.append(parts[2])
    except FileNotFoundError:
        print("Error: File CSV tidak ditemukan. Pastikan 'dataset_deadlock.csv' ada di folder yang sama dengan script")
        exit()

    # Deteksi deadlock sederhana
    deadlock = []

    for i in range(len(proses)):
        path = []
        current = i
        while True:
            if current in path:
                for j in path[path.index(current):]:
                    if proses[j] not in deadlock:
                        deadlock.append(proses[j])
                break
            path.append(current)
            found = False
            for j in range(len(proses)):
                if alokasi[j] == request[current]:
                    current = j
                    found = True
                    break
            if not found:
                break

    # Tampilkan data proses
    print("=== Data Proses & Resource ===")
    print("Proses | Alokasi | Request")
    print("-------------------------")
    for i in range(len(proses)):
        print(proses[i], "     |", alokasi[i], "     |", request[i])

    # Kondisi sistem
    if deadlock:
        print("\nKondisi Sistem: DEADLOCK TERDETEKSI")
    else:
        print("\nKondisi Sistem: AMAN")

    # Status setiap proses
    print("\n=== Status Proses ===")
    print("Proses | Status")
    print("----------------")
    for p in proses:
        if p in deadlock:
            print(p, "     | Terlibat Deadlock")
        else:
            print(p, "     | Aman")

    # Pola circular wait
    if deadlock:
        print("\nPola Circular Wait:")
        print(" -> ".join(deadlock) + " -> " + deadlock[0])
if __name__ == "__main__":
    main()