# Application Areas

Python adalah bahasa pemrograman *general-purpose*. Bahasa ini cocok untuk mengembangkan berbagai jenis aplikasi perangkat lunak. Dalam beberapa tahun terakhir, Python menjadi pilihan utama para developer di berbagai bidang berikut:

* Data Science
* Machine Learning
* Web Development
* Computer Vision dan *Image Processing*
* Embedded Systems dan IoT
* *Job Scheduling* dan Otomatisasi
* Aplikasi Desktop GUI
* Aplikasi berbasis Console
* Aplikasi CAD
* Game Development

Mari kita lihat lebih detail tiap area aplikasinya:

## Data Science

Meningkatnya popularitas Python secara pesat belakangan ini banyak dipengaruhi oleh perpustakaan-perpustakaan Data Science yang dimilikinya. Python telah menjadi keahlian penting bagi para data scientist. Saat ini, aplikasi web real-time, aplikasi mobile, dan berbagai perangkat lain menghasilkan data dalam jumlah sangat besar. Library Python untuk data science membantu perusahaan mengekstrak wawasan bisnis dari data tersebut.

Library seperti **NumPy**, **Pandas**, dan **Matplotlib** digunakan secara luas untuk menerapkan algoritma matematika pada data dan menghasilkan visualisasi. Distribusi Python seperti **Anaconda** dan **ActiveState** sudah membundel semua library penting yang dibutuhkan untuk data science.

## Machine Learning

Library Python seperti **Scikit-learn** dan **TensorFlow** membantu membangun model untuk memprediksi tren, misalnya tingkat kepuasan pelanggan, nilai proyeksi saham, dan sebagainya berdasarkan data historis. Aplikasi *machine learning* mencakup (namun tidak terbatas pada) diagnosis medis, *statistical arbitrage*, *basket analysis*, prediksi penjualan, dan lain-lain.

## Web Development

Framework web Python memudahkan pengembangan aplikasi web dengan cepat. **Django**, **Pyramid**, dan **Flask** sangat populer di kalangan developer web. Framework-framework ini memungkinkan pembuatan dan deployment aplikasi web — baik sederhana maupun kompleks — dengan jauh lebih mudah.

Versi terbaru Python menyediakan dukungan *asynchronous programming*. Framework modern memanfaatkan fitur ini untuk membangun aplikasi web dan API yang cepat serta berperforma tinggi.

## Computer Vision dan Image Processing

**OpenCV** adalah library yang sangat populer untuk menangkap dan memproses gambar. Algoritma *image processing* mengekstrak informasi dari gambar, serta merekonstruksi data gambar dan video. *Computer vision* memanfaatkan teknik ini untuk pendeteksian wajah dan pengenalan pola. OpenCV sendiri merupakan library C++, namun versi Python-nya banyak digunakan karena memungkinkan pengembangan yang lebih cepat.

Beberapa bidang yang banyak menggunakan *computer vision* antara lain robotika, pengawasan industri, otomatisasi, dan biometrik

## Embedded Systems dan IoT

**Micropython** ([https://micropython.org/](https://micropython.org/)) adalah versi ringan Python yang dirancang untuk mikrokontroler seperti Arduino. Banyak produk otomatisasi, robotika, IoT, dan aplikasi kiosk yang dibangun di atas Arduino dan diprogram dengan Micropython. **Raspberry Pi** juga sangat populer sebagai komputer papan tunggal berbiaya rendah untuk jenis aplikasi ini.

## Job Scheduling dan Automation

Salah satu penggunaan awal Python adalah untuk mengotomatiskan pekerjaan CRON (*Command Run ON*). Tugas-tugas tertentu seperti pencadangan data berkala dapat ditulis sebagai script Python dan dijalankan otomatis oleh scheduler sistem operasi.

Banyak perangkat lunak — seperti **Maya** — menyediakan API Python untuk menulis script otomatisasi (mirip *macro* di Excel).

## Desktop GUI Applications

Python adalah pilihan bagus untuk membuat aplikasi desktop GUI yang ergonomis, menarik, dan mudah digunakan. Banyak library grafis yang aslinya ditulis dalam C/C++ sudah di-*port* ke Python. Toolkit grafis populer **Qt** tersedia sebagai paket **PyQt** di Python. Begitu juga **WxWidgets**, yang di-*port* menjadi **WxPython**. Paket GUI bawaan Python, **Tkinter**, adalah antarmuka Python untuk toolkit grafis Tk.

### Tkinter 
Tkinter adalah antarmuka Python untuk toolkit GUI Tk, yang sudah disertakan dalam *standard library* Python.

### wxPython
wxPython adalah antarmuka Python untuk toolkit GUI wxWidgets. Aplikasi **BitTorrent Client** dibangun menggunakan wxPython.

### PyQtQt
Adalah salah satu toolkit GUI paling populer. Toolkit ini telah di-*port* ke Python sebagai paket **PyQt5**. Beberapa aplikasi desktop populer yang menggunakan PyQt antara lain **QGIS**, **Spyder IDE**, dan **Calibre Ebook Manager**.

### PyGTK
PyGTK adalah sekumpulan *wrapper* yang ditulis dalam Python dan C untuk library GUI GTK+. Tutorial lengkap PyGTK tersedia secara online.

### PySimpleGUI
PySimpleGUI adalah library GUI Python *open-source* dan *cross-platform*. Tujuannya adalah menyediakan API yang seragam untuk membuat GUI desktop berbasis toolkit Tkinter, PySide, dan WxPython.

### Jython
Jython adalah port Python untuk Java, yang memungkinkan script Python mengakses library GUI Java di mesin lokal secara langsung.

## Console-based Applications

Python sering digunakan untuk membuat aplikasi CLI (*command-line interface*). Script semacam ini bisa digunakan menjalankan *CRON jobs* terjadwal, seperti membuat *backup* database. Banyak library Python yang dapat mem-parsing argumen command line. Library **argparse** sudah termasuk dalam *standard library* Python.

Kamu juga bisa menggunakan **Click** (bagian dari framework Flask) dan **Typer** (bagian dari FastAPI) untuk membangun antarmuka konsol bagi aplikasi web. **Textual** adalah framework pengembangan cepat untuk membuat aplikasi yang berjalan di terminal maupun browser.

## CAD Applications

Engineer CAD dapat memanfaatkan fleksibilitas Python untuk mengotomatisasi tugas-tugas berulang seperti menggambar bentuk atau membuat laporan.

**Autodesk Fusion 360** adalah perangkat lunak CAD populer yang menyediakan API Python sehingga pengguna dapat mengotomatisasi tugas atau membuat alat kustom. **SolidWorks** juga memiliki *Python shell* bawaan yang memungkinkan pengguna menjalankan script Python di dalam software.

**CATIA** merupakan software CAD lain yang sangat populer. Selain VBScript, beberapa library Python pihak ketiga dapat digunakan untuk mengendalikan CATIA.

## Game Development

Beberapa aplikasi game terkenal dibuat menggunakan Python. Contohnya **Battlefield 2**, **The Sims 4**, **World of Tanks**, **Pirates of the Caribbean**, dan banyak lagi. Game-game tersebut dibangun menggunakan salah satu dari library Python berikut:

### Pygame

Pygame adalah salah satu library Python paling populer untuk membuat game. Library ini bersifat *open-source* dan digunakan untuk aplikasi multimedia, dibangun di atas library SDL. Pygame bersifat *cross-platform*, sehingga game yang dibuat dapat berjalan di berbagai sistem operasi.

### Kivy

Kivy adalah library lain yang banyak digunakan untuk membuat game berbasis desktop maupun mobile. Kivy mendukung antarmuka *multi-touch*. Library ini *open-source*, *cross-platform*, dan mendukung Linux, Windows, macOS, Android, iOS, dan Raspberry Pi.

### PyKyra

PyKyra berbasis SDL dan Kyra engine. Library ini termasuk salah satu framework pengembangan game tercepat. PyKyra mendukung format multimedia seperti **MPEG**, **MP3**, **Ogg Vorbis**, **WAV**, dan lainnya.