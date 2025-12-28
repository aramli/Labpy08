# Praktikum 8
Tugas Pemrograman Dasar Pertemuan Ke 13 <br>

NAMA    : Andi Ramli Hidayat <br>
NIM     : 312510385 <br>
KELAS   : TI.25 C.5

# Tugas Praktikum Kalkulator
<ul>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/1.png" width="750"/>
  <li>Hasil Program</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/2.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/3.png" width="850"/><br>
  1. Pertama-tama, Kode berfungsi untuk menampilkan judul program, kemudian meminta dua inputan dimana jika yang di input bukan angka maka akan muncul pesan error dan exit dari program dengan menggunakan statement "try-except ValueError".
<br><br>

 <img src="https://github.com/aramli/labpy08/raw/main/img/4.png" width="850"/><br>
  2. Selanjutnya, kode merupakan daftar operasi yang dapat di pilih. Terdapat Kali, Bagi, Tambah, Kurang.
<br><br>

<img src="https://github.com/aramli/labpy08/raw/main/img/5.png" width="850"/><br>
  3. Kemudian, Kode merupakan inputan untuk pemilihan operasi mana yang akan digunakan.
<br><br>

<img src="https://github.com/aramli/labpy08/raw/main/img/6.png" width="850"/><br>
  4. Lalu, kode meurupakan pengondisian dari operasi yang di pilih. try-except ZeroDivisionError digunakan agar program tidak crash saat pembagian dengan nol.raise Exception digunakan untuk menampilkan pesan error kustom jika operator tidak valid.
<br><br>

<img src="https://github.com/aramli/labpy08/raw/main/img/7.png" width="850"/><br>
  5. Lalu, Jika operasi berhasil maka akan menampilkan hasil perhitungan ke layar.
<br><br>

<img src="https://github.com/aramli/labpy08/raw/main/img/8.png" width="850"/><br>
  6. Terakhir, Jika ada error lain (misalnya operator tidak valid), program akan menampilkan pesan error sesuai masalahnya.
<br><br>

# Tugas Praktikum Validasi Data
<ul>
  <li>Program</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/9.png" width="750"/>
  <li>Hasil Program</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/10.png" width="750"/><br>
  
  <li>Penjelasan Kode</li>
  <img src="https://github.com/aramli/labpy08/raw/main/img/11.png" width="850"/><br>
  1. Pertama-tama, Terdapat list yang berisikan campuran angka dan huruf . Angka akan di hitung sedangkan huruf akan menimbulkan error jika di proses sebagai angka. Kemudian variable total akan digunakan untuk menjumlahkan semua angka valid. Variable jum_data digunakan untuk menghitung berapa banyak data angka yang berhasil di proses nantinya.
<br><br>

 <img src="https://github.com/aramli/labpy08/raw/main/img/12.png" width="850"/><br>
  2. Selanjutnya, kode merupakan perulangan dimana akan memproses setiap elemen i dalam list nilai. Jika i berupa angka, maka ditambahkan ke total dan jum_data bertambah satu. Jika i bukan angka (misalnya 'A' atau 'B'), akan muncul TypeError. Program menangkap error itu dan menampilkan pesan bahwa data tersebut dilewati.
<br><br>

<img src="https://github.com/aramli/labpy07/raw/main/img/13.png" width="850"/><br>
  3. Kemudian, Setelah perulangan selesai, program memeriksa apakah ada data angka yang valid (jum_data > 0). Jika ada, rata-rata dihitung dengan total / jum_data lalu ditampilkan. Jika tidak ada angka sama sekali, program menampilkan pesan bahwa tidak ada data valid.
