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
