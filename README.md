Nama : Muhammad Syarifudin
NPM : 2506657112
Kelas : PBP B
Foto : ![Muhammad Syarifudin](/static/img/syarif.png)
Bio : Mahasiswa S1 Ilmu Komputer Universitas Indonesia yang antusias dalam bidang web development, software engineering, dan teknologi AI.

---

### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
   > Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<main>`, `<section>`, dan `<article>`. Elemen ini membantu menstrukturkan *static web* secara logis dan terstruktur sehingga mudah dibaca oleh pengembang lain serta ramah aksesibilitas (*screen reader*). Tag `<section>` digunakan untuk mengelompokkan blok konten tematik (seperti Hero, Skills, dan Projects), sedangkan `<article>` digunakan pada setiap kartu proyek karena isinya merupakan entitas mandiri yang utuh.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisionsinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
   > Tantangan utamanya adalah mengelola tata letak asimetris pada bagian *Hero section*. Pada layar besar, saya menggunakan CSS Grid dua kolom. Ketika beralih ke layar seluler yang sempit, dua kolom akan membuat teks terlalu padat. Evaluasi dilakukan dengan memprioritaskan urutan alur informasi (identitas -> foto -> bio/detail). Saya menggunakan *media query* `@media (max-width: 600px)` untuk mengubah Grid menjadi satu kolom vertikal agar proporsional dan rapi.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
   > Batasan utamanya adalah keharusan memodifikasi kode HTML secara manual setiap kali ingin memperbarui data atau menambahkan proyek baru. Pada iterasi proyek selanjutnya, saya ingin menambahkan fungsionalitas dinamis menggunakan database relasional dan kerangka kerja *backend* (Django) sehingga data portofolio dapat dikelola secara dinamis melalui sistem CRUD tanpa harus mengubah struktur kode sumber HTML secara manual.

---

### Tugas 2

1. **Alur Pengaksesan Halaman Portofolio Baru:**
   - **Browser -> `portofolio/urls.py`**: Mengarahkan permintaan utama ke aplikasi `main`.
   - **`main/urls.py`**: Memetakan path `/projects/` ke fungsi view `show_project`.
   - **`main/views.py` (`show_project`)**: Memanggil `Project.objects.all()` dari **Model** untuk mengambil seluruh data proyek dari database.
   - **Model (`main/models.py`)**: Mengkueri database SQLite/PostgreSQL dan mengembalikan QuerySet berisi data proyek.
   - **View -> Template**: View menyusun dictionary `context` berisi data tersebut dan merendernya bersama `templates/project.html`.
   - **Template**: Django Template Language (DTL) me-loop `context` dan merender elemen HTML akhir yang dikirimkan kembali ke **Browser**.

2. **Mengapa Data Harus Disimpan di Model (Tidak Hard-coded di Template)?**
   - **Kemudahan Pemeliharaan (*Maintainability*)**: Jika data berubah, kita cukup memperbarui database melalui admin panel atau API tanpa perlu mengubah kode HTML dan melakukan re-deploy aplikasi.
   - **Pemisahan Tanggung Jawab (*Separation of Concerns*)**: Menjaga template fokus pada tampilan (UI) dan menyerahkan pengelolaan data bisnis sepenuhnya kepada Model.
   - **Skalabilitas**: Memungkinkan integrasi fitur seperti pencarian, penyaringan (filtering), pagination, serta manipulasi data secara dinamis.

3. **Perbedaan `makemigrations` dan `migrate` pada Django:**
   - **`makemigrations`**: Bertugas mendeteksi perubahan pada berkas `models.py` dan membuat berkas cetak biru instruksi migrasi baru di folder `migrations/`. Perintah ini belum mengubah struktur tabel basis data secara nyata.
   - **`migrate`**: Bertugas mengeksekusi berkas cetak biru migrasi yang belum terapkan ke dalam basis data (database) aktual sehingga tabel atau kolom baru benar-benar dibuat/diubah.
   - **Contoh kondisi**: Ketika menambahkan model baru `Project` atau menambahkan field baru pada model yang sudah ada, kita wajib menjalankan `makemigrations` terlebih dahulu lalu diikuti dengan `migrate`.

---

### Tugas 3

1. **Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan `{% csrf_token %}` pada form tersebut!**
   > * **Penggunaan ModelForm:** `ModelForm` secara otomatis membangun form HTML berdasarkan skema model Django yang sudah ada. Menggunakan `ModelForm` mengurangi penulisan kode berulang (*boilerplate*), menangani validasi tipe data secara otomatis di sisi server, serta mengamankan dan menyederhanakan proses penyimpanan data ke database via metode `.save()`.
   > * **Kewajiban `{% csrf_token %}`:** Tag ini menghasilkan *token rahasia* unik untuk mencegah serangan *Cross-Site Request Forgery* (CSRF). Token ini memastikan bahwa permintaan *POST* yang dikirimkan ke server benar-benar berasal dari pengguna sah melalui form aplikasi kita, bukan dari situs berbahaya pihak ketiga.

2. **Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?**
   > * **Ukuran Data Lebih Ringkas:** JSON menggunakan sintaks pasangan *key-value* yang jauh lebih bersih tanpa penutup tag bertumpuk seperti pada XML, sehingga memperkecil ukuran payload transfer data.
   > * **Kecepatan Parsing Native:** JSON berformat *native* JavaScript sehingga dapat di-parse secara instan oleh browser menggunakan `JSON.parse()`, sedangkan XML memerlukan *DOM Parser* yang relatif lebih berat.
   > * **Kemudahan Pembacaan:** Sintaks JSON jauh lebih mudah dibaca dan dipahami oleh pengembang (*human-readable*).

3. **Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?**
   > * **Alur Pengembalian JSON:**
   >   1. Client mengirimkan permintaan HTTP GET ke endpoint API (misalnya `/api/experience/`).
   >   2. Fungsi view mengambil query data dari database menggunakan Django ORM (`Experience.objects.all()`).
   >   3. Data QuerySet di-serialize menjadi format string JSON menggunakan `serializers.serialize('json', data)`.
   >   4. View mengembalikan objek `HttpResponse(data_json, content_type='application/json')` ke client.
   > * **Alasan Perlunya Serialization:** Objek QuerySet Django berbentuk instance kelas Python kompleks yang tidak dapat secara langsung dikirimkan melalui protokol HTTP. Serialization berfungsi mentranslasikan objek Python kompleks tersebut menjadi string teks terstruktur (JSON) yang dapat dikirim dan dimengerti oleh sistem/aplikasi client mana pun.

---

### AI Disclosure
*Pembuatan skrip unit test, komponen modal CSS, refactoring views, serta draf jawaban reflektif dipandu menggunakan Google Gemini.*