# Jurnal Refleksi Harian (Mood Tracker + Thought Journal)

Aplikasi untuk mencatat suasana hati (mood) dan refleksi harian menggunakan Python, Streamlit, dan CSV.

## Fitur

- **Tambah Entri**: Catat mood dan refleksi harian dengan tanggal
- **Lihat Entri**: Lihat entri sebelumnya dalam format yang mudah dibaca
- **Hapus Entri**: Hapus entri yang tidak ingin disimpan

## Struktur Proyek

Proyek ini menggunakan pendekatan pemrograman berorientasi objek (OOP) dengan struktur sebagai berikut:

- **libs.py**: Berisi kelas-kelas model data (`MoodEntry` dan `MoodJournal`)
- **main.py**: Berisi antarmuka pengguna Streamlit
- **data/mood_journal.csv**: File CSV untuk menyimpan data entri

## Cara Menggunakan

### Instalasi

1. Pastikan Python sudah terinstal di komputer Anda
2. Clone atau download repository ini
3. Buka terminal dan navigasi ke direktori aplikasi
4. Instal dependensi yang diperlukan:

```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi

Jalankan aplikasi dengan perintah:

```bash
streamlit run main.py
```

Aplikasi akan terbuka di browser web Anda secara otomatis (biasanya di http://localhost:8501).

### Penggunaan

1. **Tambah Entri**:

   - Pilih tanggal
   - Pilih mood dari dropdown
   - Tulis refleksi harian di kotak teks
   - Klik "Simpan Entri"

2. **Lihat Entri**:

   - Lihat semua entri sebelumnya
   - Klik pada entri untuk memperluas dan melihat detail

3. **Hapus Entri**:
   - Pilih tanggal entri yang ingin dihapus
   - Klik "Hapus Entri"

## Struktur Data

Data disimpan dalam file CSV di direktori `data/` dengan kolom:

- `date`: Tanggal entri (format YYYY-MM-DD)
- `mood`: Mood yang dipilih
- `journal_entry`: Catatan refleksi harian

## Opsi Mood

Aplikasi menyediakan beberapa opsi mood:

- Sangat Bahagia
- Bahagia
- Netral
- Sedih
- Sangat Sedih
- Stres
- Cemas
- Tenang
- Bersemangat
