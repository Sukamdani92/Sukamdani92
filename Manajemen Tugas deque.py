from collections import deque

class ManajemenTugas:
    def __init__(self):
        # Menggunakan deque untuk menyimpan tugas
        self.tugas = deque()

    def tambah_tugas(self, tugas, posisi='akhir'):
        """
        Menambahkan tugas ke antrian.
        tugas: Deskripsi tugas
        posisi: Tempat menambahkan tugas ('depan' atau 'akhir')
        """
        if posisi == 'depan':
            self.tugas.appendleft(tugas)  # Menambahkan tugas ke depan antrian
        else:
            self.tugas.append(tugas)  # Menambahkan tugas ke akhir antrian
        print(f"Tugas '{tugas}' ditambahkan di {posisi} antrian.")

    def selesaikan_tugas(self):
        """
        Menghapus dan menyelesaikan tugas yang ada di depan antrian.
        """
        if self.tugas:
            tugas = self.tugas.popleft()  # Mengambil tugas pertama dari antrian
            print(f"Tugas '{tugas}' telah diselesaikan dan dihapus dari antrian.")
        else:
            print("Tidak ada tugas yang perlu diselesaikan.")

    def lihat_tugas(self):
        """
        Melihat tugas yang ada dalam antrian.
        """
        if self.tugas:
            print("Tugas yang ada dalam antrian:")
            for i, tugas in enumerate(self.tugas, start=1):
                print(f"{i}. {tugas}")
        else:
            print("Antrian tugas kosong.")

# Contoh Penggunaan
if __name__ == "__main__":
    manajemen = ManajemenTugas()

    # Menambahkan tugas
    manajemen.tambah_tugas("Tugas A")
    manajemen.tambah_tugas("Tugas B")
    manajemen.tambah_tugas("Tugas C", posisi='depan')

    # Melihat tugas dalam antrian
    manajemen.lihat_tugas()

    # Menyelesaikan tugas
    manajemen.selesaikan_tugas()
    manajemen.selesaikan_tugas()

    # Melihat tugas setelah beberapa selesai
    manajemen.lihat_tugas()

    # Menyelesaikan tugas yang tersisa
    manajemen.selesaikan_tugas()
    manajemen.selesaikan_tugas()  # Tidak ada tugas yang tersisa
