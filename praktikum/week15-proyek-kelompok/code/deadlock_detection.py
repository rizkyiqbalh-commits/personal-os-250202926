import os
filename = "dataset.csv"

proses = []
alokasi = []
request = []
def main():
    global proses, alokasi, request
    proses.clear()
    alokasi.clear()
    request.clear()
    
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "data", "dataset.csv")
        with open(file_path, "r") as f:
            next(f) 
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

    print("=== Data Philosopher & Fork ===")
    print("Philosopher | Allocation | Request")
    print("-------------------------")
    for i in range(len(proses)):
        print(proses[i], "     |", alokasi[i], "     |", request[i])

    if deadlock:
        print("\nKondisi Sistem: DEADLOCK TERDETEKSI")
    else:
        print("\nKondisi Sistem: AMAN")

    print("\n=== Status Proses ===")
    print("Philosopher | Status")
    print("----------------")
    for p in proses:
        if p in deadlock:
            print(p, "     | Terlibat Deadlock")
        else:
            print(p, "     | Aman")

    if deadlock:
        print("\nPola Circular Wait:")
        print(" -> ".join(deadlock) + " -> " + deadlock[0])
if __name__ == "__main__":
    main()