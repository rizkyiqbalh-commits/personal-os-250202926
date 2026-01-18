# Mini Simulasi Sistem Operasi      
Modul: CPU Scheduling, Page Replacement, dan Deadlock Detection

---

## 1. Deskripsi Singkat

Aplikasi ini merupakan program berbasis terminal yang mensimulasikan tiga konsep utama dalam Sistem Operasi, yaitu **CPU Scheduling**, **Manajemen Memori (*Page Replacement*)**, dan **Deadlock Detection**. Aplikasi menerima input berupa dataset sederhana, kemudian menampilkan hasil simulasi dalam bentuk tabel serta ringkasan metrik kinerja. Seluruh aplikasi dapat dijalankan menggunakan **Docker** untuk memastikan lingkungan eksekusi yang konsisten di berbagai sistem.

---

## 2. Modul yang Diimplementasikan
### Modul A – CPU Scheduling

  * Algoritma: FCFS 
  * Output: waiting time, turnaround time, serta nilai rata-rata

### Modul B – Page Replacement

  * Algoritma: FIFO 
  * Output: jumlah page fault dan hit ratio

### Modul C – Deadlock Detection

  * Deteksi kondisi deadlock berdasarkan allocation dan request
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

Pastikan bahasa pemrograman telah terpasang.

```
python main.py
```

### Menjalankan via Docker

Build Image Docker
```
docker build -t week15-proyek-kelompok .
```
Jalankan Container
```
docker run -it --rm week15-proyek-kelompok
```
---

## 5. Dataset

Dataset disimpan dalam folder `data/` dengan format csv/txt.

### process.csv (CPU Scheduling)

### reference_string.txt (Page Replacement)

### dataset.csv.txt (Deadlock Detection)