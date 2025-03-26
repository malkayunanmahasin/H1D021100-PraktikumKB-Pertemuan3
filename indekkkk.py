import random
import datetime

tasks = [] 

def add_task():
    task_name = input("Masukkan nama tugas: ")
    due_date = input("Masukkan tenggat waktu (YYYY-MM-DD): ")
    task_id = random.randint(1000, 9999) 
    
    task = {
        "id": task_id,
        "name": task_name,
        "due_date": due_date,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print(f"Tugas '{task_name}' berhasil ditambahkan dengan ID {task_id}\n")

def view_tasks():
    if not tasks:
        print("Tidak ada tugas yang tersedia.\n")
        return
    
    print("Daftar Tugas:")
    for task in tasks:
        print(f"ID: {task['id']}, Nama: {task['name']}, Tenggat: {task['due_date']}, Dibuat: {task['created_at']}")
    print()

def delete_task():
    task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Tugas dengan ID {task_id} berhasil dihapus.\n")
            return
    print("Tugasnya tidak ada.\n")

def main():
    while True:
        print("=== Sistem Manajemen Tugas ===")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih menu (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Terima kasih orang baik.")
            break
        else:
            print("Pilihan tidak valid, coba lagi ya.\n")

if __name__ == "__main__":
    main()
