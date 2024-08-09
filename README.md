# Ollama - LLava Image Describer v1.0.0 🐍

Sebuah aplikasi PyQt6 yang terintegrasi dengan library `pyollama` untuk menjalankan model multi-modal seperti `llava`. Aplikasi ini menyediakan antarmuka yang mudah digunakan untuk mengunggah gambar, memasukkan prompt, dan menghasilkan respons.

![Screenshot Aplikasi](./Ollama%20-%20LLava%20Image%20Describer.jpeg)

## Fitur ✨

- **Unggah Gambar dengan Drag-and-Drop**: Unggah gambar dengan cara menyeretnya ke jendela aplikasi.
- **Pemilihan Model**: Pilih dari daftar model `llava` yang tersedia untuk menghasilkan respons.
- **Dukungan Markdown**: Respons ditampilkan dengan format Markdown untuk keterbacaan yang lebih baik.
- **Status Bar**: Menampilkan status aplikasi saat ini, seperti apakah Ollama sedang online atau offline, serta informasi tentang operasi terakhir.

## Persyaratan 🛠️

- Python 3.x
- PyQt6
- markdown
- pyollama

## Instalasi ⚙️

1. **Klon repository**:

    ```bash
    git clone https://github.com/username-kamu/nama-repo-kamu.git
    cd nama-repo-kamu
    ```

2. **Instal dependensi**:

    Install [Ollama](https://ollama.com/download) terlebih dahulu, kemudian download dan jalankan model [Llava](https://ollama.com/library/llava)
    ```bash
    ollama run llava
    ```

    Kamu bisa menggunakan `pip` untuk menginstal paket Python yang diperlukan.

    ```bash
    pip install ollama
    ```
    ```bash
    pip install pyqt6
    ```
    ```bash
    pip install markdown
    ```

3. **Jalankan aplikasi**:

    ```bash
    python app.py
    ```

## Penggunaan 🚀

1. **Pilih model**: Pilih salah satu model `llava` yang tersedia dari menu dropdown.
2. **Unggah gambar**: Seret gambar ke area yang ditentukan atau klik untuk mengunggah.
3. **Masukkan prompt**: Ketikkan prompt kamu di area teks.
4. **Hasilkan respons**: Klik tombol `Send` untuk menjalankan model dan melihat respons.
5. **Reset**: Gunakan tombol `Reset` untuk menghapus semua input dan memulai dari awal.

## Gambaran Kode 💻

### Aplikasi Utama (`MyApp`)

- **Inisialisasi**: Mengatur jendela utama dengan tata letak dan widget.
- **Komponen UI**:
  - **QComboBox**: Untuk memilih model.
  - **QTextEdit**: Untuk memasukkan prompt.
  - **QTextBrowser**: Untuk menampilkan respons.
  - **QStatusBar**: Untuk menampilkan status aplikasi.

### Fungsi

- **run_model**: Menjalankan model yang dipilih menggunakan prompt dan gambar yang diunggah, lalu menampilkan hasilnya.
- **reset**: Menghapus semua bidang input dan mengatur ulang aplikasi ke keadaan awal.

## Referensi 🤝

Untuk informasi lebih lanjut dan panduan video, kamu bisa menonton video YouTube berikut:
[referensi](https://youtu.be/8cg9jQHhQuc?si=668nS8k02SfY_6p2)