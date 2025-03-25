import heapq

class AntrianDarurat:
    def __init__(self):
        # Heap untuk antrian darurat
        self.heap = []
        # Penanda untuk ID pasien (agar unik)
        self.counter = 0

    def tambah_pasien(self, nama, tingkat_keparahan):
        """
        Menambahkan pasien ke antrian darurat.
        Parameter:
        nama: Nama pasien
        tingkat_keparahan: Integer yang menunjukkan tingkat keparahan (semakin kecil, semakin parah)
        """
        # Menambahkan pasien dengan prioritas berdasarkan tingkat_keparahan
        # Menggunakan counter untuk memastikan elemen yang masuk memiliki urutan yang unik
        heapq.heappush(self.heap, (tingkat_keparahan, self.counter, nama))
        self.counter += 1
        print(f"Pasien {nama} dengan tingkat keparahan {tingkat_keparahan} telah ditambahkan ke antrian.")
    
    def proses_pasien(self):
        """
        Memproses pasien dengan prioritas tertinggi (tingkat keparahan terparah).
        """
        if self.heap:
            tingkat_keparahan, counter, nama = heapq.heappop(self.heap)
            print(f"Pasien {nama} dengan tingkat keparahan {tingkat_keparahan} sedang diproses.")
        else:
            print("Tidak ada pasien dalam antrian.")

    def tampilkan_antrian(self):
        """
        Menampilkan antrian saat ini.
        """
        if self.heap:
            print("Antrian Pasien:")
            for tingkat_keparahan, counter, nama in self.heap:
                print(f"{nama} - Tingkat Keparahan: {tingkat_keparahan}")
        else:
            print("Antrian kosong.")

# Contoh Penggunaan:
if __name__ == "__main__":
    antrian = AntrianDarurat()

    # Menambahkan pasien ke antrian
    antrian.tambah_pasien("John", 5)  # Pasien dengan tingkat keparahan 5
    antrian.tambah_pasien("Mary", 2)  # Pasien dengan tingkat keparahan 2
    antrian.tambah_pasien("Alice", 4)  # Pasien dengan tingkat keparahan 4

    # Menampilkan antrian
    antrian.tampilkan_antrian()

    # Memproses pasien dengan prioritas tertinggi (terparah)
    antrian.proses_pasien()

    # Menampilkan antrian setelah diproses
    antrian.tampilkan_antrian()

    # Memproses sisa pasien
    antrian.proses_pasien()
    antrian.proses_pasien()
    antrian.proses_pasien()
