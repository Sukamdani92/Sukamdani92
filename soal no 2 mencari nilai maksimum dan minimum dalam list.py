def main():
    angka_list = []

    for i in range(10):
        while True:
            try:
                angka = int(input(f"Masukkan angka ke-{i+1}: "))
                angka_list.append(angka)
                break
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka integer.")

    print("\nList angka yang telah diisi:")
    print(angka_list)

    if angka_list:
        max_angka = max(angka_list)
        min_angka = min(angka_list)
        
        print(f"\nNilai maksimum: {max_angka}")
        print(f"Nilai minimum: {min_angka}")
    else:
        print("List kosong.")

if __name__ == "__main__":
    main()
