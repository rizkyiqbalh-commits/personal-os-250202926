# Mini Simulasi Sistem Operasi      
Modul: CPU Scheduling, Page Replacement, dan Deadlock Detection

---

## 1. Deskripsi Singkat

Aplikasi ini merupakan program berbasis terminal yang mensimulasikan tiga konsep utama dalam Sistem Operasi, yaitu **CPU Scheduling**, **Manajemen Memori (*Page Replacement*)**, dan **Deadlock Detection**. Aplikasi menerima input berupa dataset sederhana, kemudian menampilkan hasil simulasi dalam bentuk tabel serta ringkasan metrik kinerja. Seluruh aplikasi dapat dijalankan menggunakan **Docker** untuk memastikan lingkungan eksekusi yang konsisten di berbagai sistem.

---

## 2. Modul yang Diimplementasikan
### Modul A – CPU Scheduling

  * Algoritma: FCFS 
  * Skenario : Transfer File
  * Output: waiting time, turnaround time, serta nilai rata-rata

### Modul B – Page Replacement

  * Algoritma: FIFO 
  * Skenario : Pemantauan CCTV
  * Output: jumlah page fault dan hit ratio

### Modul C – Deadlock Detection

  * Deteksi kondisi deadlock berdasarkan allocation dan request
  * Skenario : Dining Philosophers
  * Output: status deadlock dan daftar proses yang terlibat

---

## 3. Struktur Folder

```
code/
├─ data/
│    ├── dataset.csv
│    ├── process.csv
│    └── reference_string.txt
├─ cpu_scheduling.py
├─ deadlock_detection.py
├─ Dockerfile
├─ main.py
├─ page_replacement.py 
└─ README.md
```

---

## 4. Cara Menjalankan Aplikasi 
### Menjalankan Tanpa Docker

1. Pastikan bahasa pemrograman python telah terpasang.
2. Buka terminal, masuk ke folder `week15-proyek-kelompok/code/`.
3. Jalankan file main.py 
4. Pilihan menu 1 menjalankan simulasi CPU Scheduling menggunakan algoritma FCFS.
5. Pilihan menu 2 menjalankan simulasi Page Replacement menggunakan algoritma FIFO.
6. Pilihan menu 3 menjalankan simulasi Deadlock Detection untuk mendeteksi kondisi deadlock.
7. Pilihan menu 0 digunakan untuk mengakhiri program dan keluar dari aplikasi.

### Menjalankan via Docker
1. Masuk ke direktori `week15-proyek-kelompok/code/` melalui terminal.
2. Build image docker dengan perintah `docker build -t week15-proyek-kelompok .`
3. Setelah proses build image selesai, jalankan program dengan perintah `docker run -it --rm week15-proyek-kelompok`
4. Pilihan menu 1 menjalankan simulasi CPU Scheduling menggunakan algoritma FCFS.
5. Pilihan menu 2 menjalankan simulasi Page Replacement menggunakan algoritma FIFO.
6. Pilihan menu 3 menjalankan simulasi Deadlock Detection untuk mendeteksi kondisi deadlock.
7. Pilihan menu 0 digunakan untuk mengakhiri program dan keluar dari aplikasi.

---

## 5. Dataset

Dataset disimpan dalam folder `data/` dengan format csv/txt.

### process.csv (CPU Scheduling)
File ini berisi data sebagai berikut:
|Proses|Arrival Time|Burst Time|
|:----:|:----:|:----:|
|F1|0|12|
|F2|1|1 |
|F3|2|30|
|F4|3|3 |
|F5|4|70|

### reference_string.txt (Page Replacement)
File ini berisi deretan angka yang merepresentasikan reference string untuk simulasi page replacement, yaitu:     

```
1,3,4,7,3,1,2,1,5,7
```

### dataset.csv (Deadlock Detection)
File ini berisi data sebagai berikut:
|Philosopher|Allocation|Request|
|:----:|:----:|:----:|
|P1|F1|F2|
|P2|F2|F3|
|P3|F3|F4|
|P4|F4|F1|