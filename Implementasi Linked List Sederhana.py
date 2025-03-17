def main():
    angka_list = []
    angka_list.extend([10, 20, 30, 40, 50])
    
    print("List sebelum operasi:")
    print(angka_list)

    if len(angka_list) > 0:
        angka_list.pop(0)  
        angka_list.pop()   
    
    print("\nList setelah menghapus elemen pertama dan terakhir:")
    print(angka_list)

    if len(angka_list) >= 2:
        angka_list.insert(2, 25)
    
    print("\nList setelah menyisipkan angka 25 pada indeks ke-2:")
    print(angka_list)

if __name__ == "__main__":
    main()
