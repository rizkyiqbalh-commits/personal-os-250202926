import csv
import os

def load_data(file):
    data = []
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                "proses": row["Proses"],
                "kedatangan": int(row["Arrival Time"]),
                "Lama_proses": int(row["Burst Time"])
            })
    return data

def fcfs(data):
    waktu = data[0]["kedatangan"]
    total_wt = total_tat = 0

    judul = "Implementasi CPU Scheduling : File Transfer"
    line = "-" * 75  

    print("\n" + line)
    print(judul.center(75))
    print(line + "\n")
    print(line)
    print(f"| {'Proses'} | {'Arrival Time'} | {' Burst Time'}   | {'Waiting Time'}  | {'Turnaround Time'} |")
    print(line)

    for d in data:
        if waktu < d["kedatangan"]:
            waktu = d["kedatangan"]

        wt = waktu - d["kedatangan"]
        tat = wt + d["Lama_proses"]

        total_wt += wt
        total_tat += tat

        print(f"|   {d['proses']:<4} |     {d['kedatangan']:<9}| {d['Lama_proses']:>4} seconds  |  {wt:>3} seconds  | {tat:>6} seconds  |")

        waktu += d["Lama_proses"]


    print(line) 
    print("\nSemua file telah selesai dipindah.\n") 

    print(line)

    wt_avg = total_wt / len(data)
    tat_avg = total_tat / len(data)

    print(f"Rata-rata Waiting Time       : {wt_avg:.2f} seconds")
    print(f"Rata-rata Turnaround Time    : {tat_avg:.2f} seconds")



def main():
    path = os.path.join(os.path.dirname(__file__), "data", "process.csv")
    fcfs(load_data(path))
if __name__ == "__main__":
    main()
