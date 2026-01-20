
# Laporan Akhir Proyek Kelompok
**Mini Simulasi Sistem Operasi**

---

## Nama Anggota Kelompok 
- Rizky Iqbal Hisyam (250202926)
- Nanang Apriyanto (250202957)
- Lintang Galih Prayogi (250202946)
- Putri Amaliya Rahmadani (250202924)
- Sukmani Intan Jumala (250202983)

## 1. Pendahuluan
### 1.1 Latar Belakang
Sistem operasi memiliki peran penting dalam mengelola sumber daya komputer agar dapat digunakan secara efisien oleh banyak proses secara bersamaan. Tiga mekanisme utama yang berperan dalam pengelolaan tersebut adalah CPU scheduling, page replacement, dan deadlock detection. Ketiga mekanisme ini tidak bekerja secara terpisah, melainkan saling berkaitan dalam satu sistem operasi yang utuh.

Proyek ini membangun sebuah mini simulasi sistem operasi yang mengintegrasikan ketiga mekanisme tersebut ke dalam satu aplikasi berbasis terminal. Aplikasi yang dikembangkan mengimplementasikan CPU scheduling untuk mensimulasikan pengaturan urutan eksekusi proses, page replacement untuk memodelkan pengelolaan memori ketika kapasitas terbatas, serta deadlock detection untuk mengidentifikasi kondisi kebuntuan akibat saling menunggu sumber daya antar proses. Melalui simulasi ini, perilaku sistem operasi dapat diamati secara lebih jelas melalui input dataset sederhana dan output berupa tabel serta metrik kinerja. 

Selain aspek simulasi, proyek ini juga dibuat dengan memperhatikan cara pengembangan yang teratur dengan memanfaatkan Docker agar aplikasi bisa dijalankan dengan cara yang sama di berbagai lingkungan, serta Git sebagai sarana pengelolaan kode sumber secara kolaboratif. Dengan pendekatan ini, proyek tidak hanya membantu memahami konsep sistem operasi, tetapi juga memberikan pengalaman membuat aplikasi secara terstruktur dan bekerja sama dalam tim.

### 1.2 Tujuan
Adapun tujuan dari pelaksanaan proyek ini, sebagai berikut:
1. Menerapkan kerja kolaboratif dalam tim melalui pembagian peran yang terstruktur, seperti Project Lead, Developer, dan Documentation/QA.
2. Mengimplementasikan dan mengintegrasikan konsep CPU scheduling, page replacement, dan deadlock detection ke dalam satu aplikasi simulasi sistem operasi.
3. Mengelola kode sumber proyek menggunakan Git, termasuk penerapan branching dan merge dalam proses pengembangan.
4. Membungkus aplikasi menggunakan Docker untuk memastikan kemudahan distribusi, eksekusi, dan demonstrasi pada berbagai lingkungan sistem operasi.
5. Menyusun laporan teknis serta menyajikan hasil pengujian dan analisis kinerja aplikasi secara sistematis.
---

## 2. Arsitektur Aplikasi
### 2.1 Modul dan Alur Data
**a. CPU Scheduling**
 - Studi Kasus: File Transfer       
    Kami menggunakan analogi file transfer, misal dalam sistem pemindahan file antar media penyimpanan, keterbatasan sumber daya membuat file diproses satu per satu dalam antrian. Sistem menggunakan algoritma First Come First Served (FCFS), yaitu file yang masuk lebih dulu akan dipindahkan terlebih dahulu hingga selesai, baru file berikutnya diproses. Dengan demikian, setiap file diproses secara adil sesuai waktu kedatangannya, meskipun ukuran file berbeda-beda.      
- Input : File `process.csv` yang mencakup Proses, Arrival Time, dan Burst Time
- Id Data :
    - VirtualBox 7.2.4 Win.exe (F1)
    - Data_Praktikum.xlsx (F2)
    - Video_Praktikum.mp4 (F3)
    - Laporan_Instalasi.pdf (F4)
    - Debian11.ova (F5)
- Alur  Data :  
    - Sistem membaca data file yang akan dipindahkan, termasuk informasi waktu    kedatangan masing-masing file.      
    - Sistem menyusun urutan file berdasarkan waktu kedatangannya, dari yang paling awal hingga yang paling akhir, menggunakan proses pengurutan sederhana.        
    - Sistem memproses antrean file secara berurutan, di mana file yang datang lebih awal akan dipindahkan hingga selesai sebelum memproses file selanjutnya.      
    - Selama proses berlangsung, sistem menghitung waktu tunggu (waiting time) untuk setiap file berdasarkan selisih antara waktu mulai diproses dan waktu kedatangannya.      
- Output : Tabel simulasi CPU Scheduling yang menampilkan urutan proses yang akan dieksekusi, kemudian waiting time, turnaround time, rata-rata total waktu tunggu serta total waktu penyelesaian transfer file.      
        
**b. Page Replacement**     
- Studi Kasus : Mapping CCTV        
Kami menggunakan analogi mapping CCTV, misal sebuah kampus memiliki beberapa CCTV. Karena keterbatasan memori, CCTV tersebut bisa di pantau maksimal 3 rekaman  dalam satu waktu, untuk mengelola keterbatasan memori itu, sistem pengawas menggunakan algoritma FIFO yaitu algoritma yang mengeluarkan page berdasarkan waktu kedatangannya, pertama kali masuk juga akan menjadi yang pertama kali keluar.        
- Input : File `reference_string.txt` yang berisi id cctv, yang berupa gerbang (1), gudang (2), halaman (3), kantin (4), lorong A (5), lorong B (6), lobby (7).      
- Alur Data :       
    - Sistem membaca urutan rekaman CCTV (representasi page reference string).     
    - Setiap rekaman yang diterima akan dimuat ke dalam memori pengawas.       
    - Batas memori (frame) hanya 3 rekaman.        
    - Jika rekaman sudah ada di memori (Hit), posisi rekaman tidak berubah.        
    - Jika rekaman belum ada dan memori penuh (Miss/Page Fault), sistem akan menghapus rekaman yang paling lama masuk  untuk memberi ruang bagi rekaman baru.      
- Output : Tabel yang berisi urutan page yang akan masuk ke memori, isi memori saat ini, status (page fault atau hit fault), total page fault, page hit, dan hit ratio.     

**c. Deadlock Detection**       
- Studi Kasus : Dining Philosophers     
Pada suatu meja makan terdapat beberapa orang yang makan secara bersamaan. Setiap orang membutuhkan 2 garpu untuk dapat makan. Dalam kondisi ini, masing-masing orang telah memegang satu alat makan, namun masih menunggu alat makan lain yang sedang digunakan oleh orang lain. Akibatnya, tidak ada satu pun yang dapat mulai makan karena seluruhnya berada dalam keadaan saling menunggu. Situasi tersebut merepresentasikan kondisi deadlock, yang dapat dideteksi melalui adanya pola circular wait antar individu.      
- Input :       
    - Data diambil dari file dataset.csv dan diproses oleh program.     
    - Proses (Philosopher): P1, P2, P3, P4      
    - Resource (Fork): F1, F2, F3, F4       
- Alokasi Resource:     
    P1 -> F1     
    P2 -> F2     
    P3 -> F3     
    P4 -> F4     
- Request Resource:      
    P1 -> F2     
    P2 -> F3     
    P3 -> F4     
    P4 -> F1     
- Alur Data :
    - Data proses, alokasi, dan permintaan resource disimpan dalam file dataset.csv.           
    - Program membaca data CSV dan menyimpannya ke dalam list proses, alokasi, dan request.     
    - Sistem melakukan penelusuran hubungan antar proses berdasarkan resource yang diminta.     
    - Jika suatu proses menunggu resource yang dialokasikan proses lain, penelusuran dilanjutkan.       
    - Penelusuran berhenti ketika tidak ada proses pemegang resource atau ditemukan siklus.     
    - Jika ditemukan pola circular wait, sistem mendeteksi terjadinya deadlock.     
    - Program menampilkan status sistem dan daftar proses yang terlibat deadlock.              
- Output:                
    - Kondisi Sistem: DEADLOCK TERDETEKSI         
    - Proses Terlibat Deadlock: P1, P2, P3, P4      
    - Pola Circular Wait:       
    - P1 → P2 → P3 → P4 → P1        

---

## 3. Implementasi dan Demo Aplikasi
### 3.1 Build Aplikasi
Sebelum dijalankan, aplikasi perlu di-build terlebih dahulu menggunakan perintah:   
`docker build -t week15-proyek-kelompok .`

![build image](<screenshots/build_aplikasi.png>)      

### 3.2 Running
Setelah proses build selesai, jalankan aplikasi dengan perintah:
`docker run -it --rm week15-proyek-kelompok`        
Penjelasan flag:   
flag `-it`(interactive) digunakan untuk program yang butuh interaksi user.           
flag `rm` (remove container otomatis) yang digunakan untuk menghapus container setelah selesai running.  

### 3.3 Tahapan demo Aplikasi
Demo dilakukan melalui beberapa modul utama, sebagai berikut:       
- **CPU Scheduling**        
Pengguna memilih menu “1” untuk menjalankan simulasi CPU Scheduling. 
    - Program membaca data dari file `process.csv`
    - Hasil penjadwalan proses ditampilkan menggunakan algoritma FCFS dalam bentuk tabel.
    - Setelah selesai, pengguna menekan Enter untuk kembali ke menu utama.
- **Page Replacement**      
Pengguna memilih menu “2” untuk menjalankan simulasi Page Replacement.
    - Modul ini membaca data dari file `reference_string.txt`
    - Proses penggantian halaman ditampilkan langsung di terminal menggunakan algoritma FIFO.
- **Deadlock Detection**        
Pengguna memilih menu “3” untuk menjalankan modul Deadlock Detection. 
    - Program membaca data dari file `dataset.csv`
    - Hasil pendeteksian deadlock ditampilkan berdasarkan hubungan allocation dan resource.
- **Terminasi Aplikasi**        
Untuk mengakhiri demo, pengguna memilih menu “0”

---

## 4. Analisis Hasil Pengujian
### 4.1 Hasil Pengujian Modul CPU Scheduling-FCFS
![image](<screenshots/cpu_scheduling.png>)    

**Tabel Hasil Simulasi CPU Scheduling**    
| Proses | Arrival Time | Burst Time | Waiting Time | Turnaround Time |
|:---:|:--:|:--:|:--:|:--:|
| F1 | 0 | 12 | 0 | 12 |
| F2 | 1 | 1 | 11 | 12 | 
| F3 | 2 | 30 | 11 | 41 |
| F4 | 3 | 3 | 40 | 43 |
| F5 | 4 | 70 | 42 | 112 | 
|**Total** |  |  | 104 | 220 |
|**Rata - rata** |  |  | 20.80 | 44 |

**Analisis:**       
- Algoritma FCFS memproses file berdasarkan urutan kedatangan tanpa mempertimbangkan lama waktu proses. 
- File dengan burst time besar di awal antrean menyebabkan peningkatan waktu tunggu file lain.
- Variasi burst time yang signifikan mengakibatkan rata-rata waiting time dan turnaround time menjadi tinggi, yang terlihat pada output ketika file F1 memiliki burst time lebih besar dan diproses lebih awal, sehingga file F2 dan selanjutnya harus menunggu cukup lama meskipun waktu prosesnya lebih kecil. Akumulasi waktu tunggu tersebut menyebabkan nilai rata-rata waiting time dan turnaround time meningkat.

### 4.2 Hasil Pengujian Modul Page Replacement-FIFO
![image](<screenshots/page_replacement.png>)

**Tabel Hasil Simulasi Page Replacement**
| Page  | F1 | F2 | F3 | Status |
| :-----: | :------: | :----: | :----: |:----:|
| 1      | 1 | - | -| Fault|
| 3      | 1 | 3 | -| Fault|
| 4      | 1 | 3 | 4| Fault|
| 7      | 7 | 3 | 4| Fault|
| 3      | 7 | 3 | 4| Hit  |
| 1      | 7 | 1 | 4| Fault|
| 2      | 7 | 1 | 2| Fault|
| 1      | 7 | 1 | 2| Hit  |
| 5      | 5 | 1 | 2| Fault|
| 7      | 5 | 7 | 2| Fault|

**Analisis:**       
Sistem memuat rekaman kamera (page) ke dalam memori satu persatu setiap frame, saat page tersebut belum ada di memori maka akan disebut page fault, sedangkan jika page sudah ada di dalam memori maka disebut page hit. Saat sistem ingin memuat page baru, tetapi memori penuh, maka sistem akan mengeluarkan page yang paling awal masuk ke dalam memori


### 4.3 Hasil Pengujian Modul Deadlock Detection-Dining Philosophers
![image](<screenshots/deadlock_detection.png>)

**Tabel Hasil Simulasi Deadlock Detection** 
| Philosopher | Status |
|:---:|:--:|
| P1 | Terlibat Deadlock | 
| P2 | Terlibat Deadlock |
| P3 | Terlibat Deadlock |
| P4 | Terlibat Deadlock | 

**Analisis:** 
- Setiap filsuf memegang satu garpu (allocation) dan secara bersamaan meminta garpu lain (request).
- Resource yang diminta oleh suatu proses sedang dialokasikan oleh proses lain, sehingga proses tidak dapat melanjutkan eksekusi.
- Penelusuran pada program membentuk jalur:
    - P1 meminta F2 -> dialokasikan ke P2
    - P2 meminta F3 -> dialokasikan ke P3
    - P3 meminta F4 -> dialokasikan ke P4
    - P4 meminta F1 -> dialokasikan ke P1
- Jalur tersebut membentuk circular wait, sehingga seluruh proses berada dalam kondisi saling menunggu.
Karena tidak ada proses yang dapat melepaskan resource, sistem berada dalam kondisi deadlock.      

---

## 5. Pembagian Peran dan Kontribusi Anggota

![image](<screenshots/kontribusi_kelompok.png>)


| NIM | Nama | Peran | Kontribusi |
| :---: | :---: | :---: | :---: |
| 250202926 | Rizky Iqbal Hisyam | Project Lead/Integrator| - Inisiasi project (merancang struktur awal dan main.py) <br> - merge PR & fix conflict <br> - Uji modul aplikasi  |
| 250202957 | Nanang Apriyanto | Developer 1 (Modul CPU Scheduling) | - Merancang modul aplikasi CPU Scheduling <br> - Membuat dataset process.csv <br> - Analisis eksekusi aplikasi | 
| 250202946 | Lintang Galih Prayogi | Developer 2 (Modul Page Replacement) | - Merancang modul aplikasi Page Replacement (FIFO) <br> - Membuat dataset reference_string.txt <br> - Analisis eksekusi aplikasi |
| 250202924 | Putri Amaliya Rahmadani | Developer 3 (Deadlock Detection) | - Merancang modul apllikasi Deadlock Detection <br> - Membuat dataset.csv <br> - Analisis eksekusi aplikasi |
| 250202983 | Sukmani Intan Jumala | Dokumentasi & QA | - Menyusun laporan proyek <br> - Mengumpulkan dokumentasi eksekusi (screenshots) <br> - Menyelesaikan quiz |
--- 

## 6. Quiz
**1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?**    
Tantangan terbesar yang kami alami adalah menyatukan tiga modul yang dibuat terpisah ke dalam satu menu utama. Setiap modul memiliki alur eksekusi sendiri, sehingga perlu penyesuaian agar saat dipanggil dari main.py tidak terjadi bentrok dan program tetap berjalan rapi.      
Solusinya, kami menyepakati struktur pemanggilan fungsi yang sama, yaitu dengan menyediakan fungsi main() di setiap modul. Selanjutnya, modul-modul tersebut dipanggil melalui menu sederhana di program utama. Kami juga sering berdiskusi dan mencari referensi dari internet untuk memastikan integrasi berjalan lancar  

**2. Mengapa Docker membantu proses demo dan penilaian proyek?**
Docker membantu proses demo dan penilaian proyek karena membuat lingkungan aplikasi konsisten di berbagai komputer. Dengan Docker, semua dependensi, konfigurasi, dan versi perangkat lunak yang dibutuhkan sudah dikemas dalam satu container. Sehingga penilai tidak perlu menginstal banyak software secara manual dan bisa langsung menjalankan proyek dengan satu perintah. Selain itu, Docker membuat proses penilaian lebih rapi dan aman karena setiap aplikasi berjalan di dalam container yang terisolasi, tidak mengganggu sistem utama penilai dan mudah dihapus setelah selesai.

**3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan**
Modul yang paling terdampak performanya pada implementasi kami adalah CPU Scheduling.
Hal ini karena modul tersebut memproses dan menghitung data untuk setiap proses, sehingga ketika jumlah proses bertambah, jumlah perhitungan juga ikut meningkat. Sementara itu, modul lainnya masih menggunakan logika yang relatif sederhana, sehingga dampaknya tidak sebesar CPU Scheduling

--- 

## 7. Penutup
### 7.1 Kesimpulan
1. Proyek ini berhasil menggambarkan mekanisme dasar sistem operasi melalui aplikasi simulasi sederhana berbasis command line.
2. Modul CPU Scheduling (FCFS), Page Replacement (FIFO), dan Deadlock Detection dapat dijalankan dalam satu aplikasi dengan alur menu yang terstruktur.
3. Penggunaan Git dan Docker mendukung proses pengembangan yang terorganisir serta memastikan aplikasi dapat dijalankan secara konsisten di berbagai lingkungan.
4. Melalui output tabel dan hasil perhitungan, konsep seperti waiting time, page fault, dan deadlock menjadi lebih mudah dipahami secara praktis
