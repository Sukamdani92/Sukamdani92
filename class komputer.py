class Komputer:
    def __init__(self, merk, penyimpanan, processor):
        # Atribut untuk menyimpan merk, penyimpanan, dan processor
        self.merk = merk
        self.penyimpanan = penyimpanan
        self.processor = processor

    def mengetik(self):
        # Metode untuk mengetik
        print(f"Komputer {self.merk} sedang digunakan untuk mengetik.")

    def menonton_video(self):
        # Metode untuk menonton video
        print(f"Komputer {self.merk} sedang menonton video dengan kualitas yang baik.")

    def mencari_informasi(self):
        # Metode untuk mencari informasi
        print(f"Komputer {self.merk} sedang digunakan untuk mencari informasi di internet.")

# Membuat objek dari kelas Komputer
komputer_saya = Komputer("Lenovo", "1TB", "Intel i7")

# Menggunakan metode dari objek
komputer_saya.mengetik()
komputer_saya.menonton_video()
komputer_saya.mencari_informasi()

# Menampilkan informasi atribut dari objek
print(f"Merk: {komputer_saya.merk}")
print(f"Penyimpanan: {komputer_saya.penyimpanan}")
print(f"Processor: {komputer_saya.processor}")
