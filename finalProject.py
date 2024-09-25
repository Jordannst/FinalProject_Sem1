"""             FINAL PROJECT
      Nama    : Jordan
      Tanggal : 20 - 29 November 2023
      Program : Final Project (Nilai Mahasiswa)
"""

from tabulate import tabulate

# Fungsi untuk menghitung nilai akhir siswa (No. 1)
def hitung_nilai_akhir():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    data = []

    for i in range(jumlah_siswa):
        nama_siswa = input(f"\nMasukkan nama siswa {i + 1}: ")
        nim = int(input(f'Masukkan NIM {nama_siswa}: '))
        print(f"\nSiswa {i + 1} ({nama_siswa}):")

        # Assignment
        jumlah_assignment = int(input("Masukkan jumlah tugas assignment: "))
        nilai_assignment = [float(input(f'Masukkan Nilai Assignment Ke- {y + 1}: ')) for y in range(jumlah_assignment)]
        total_assignment = int(sum(nilai_assignment) / len(nilai_assignment) * 0.2)

        # Quiz
        jumlah_quiz = int(input("Masukkan jumlah tugas quiz: "))
        nilai_quiz = [float(input(f'Masukkan Nilai Quiz Ke- {a + 1}: ')) for a in range(jumlah_quiz)]
        total_quiz = int(sum(nilai_quiz) / len(nilai_quiz) * 0.15)

        # Project, Mid, Final
        project = int(input("Masukkan Nilai Project (0 - 15 %): "))
        mid = int(input("Masukkan Nilai MID (0 - 25 %): "))
        final = int(input("Masukkan Nilai FINAL (0 - 25 %): "))

        nilai_akhir = total_assignment + total_quiz + project + mid + final
        data.append({
            "nim": nim,
            "nama_siswa": nama_siswa,
            "nilai_assignment": nilai_assignment,
            "total_assignment": total_assignment,
            "nilai_quiz": nilai_quiz,
            "total_quiz": total_quiz,
            "project": project,
            "mid": mid,
            "final": final,
            "nilai_akhir": nilai_akhir,
            "grade_nilai": grade(nilai_akhir)
        })

    # Mengurutkan nilai akhir secara global
    return data

# Fungsi untuk menentukan grade (No. 2)
def grade(nilai_akhir):
    if 91 <= nilai_akhir <= 100:
        return 'A'
    elif 85 <= nilai_akhir <= 90:
        return 'A-'
    elif 82 <= nilai_akhir <= 84:
        return 'B+'
    elif 78 <= nilai_akhir <= 81:
        return 'B'
    elif 75 <= nilai_akhir <= 77:
        return 'B-'
    elif 70 <= nilai_akhir <= 74:
        return 'C+'
    elif 67 <= nilai_akhir <= 69:
        return 'C'
    elif 60 <= nilai_akhir <= 66:
        return 'C-'
    elif 40 <= nilai_akhir <= 59:
        return 'D'
    elif 0 <= nilai_akhir <= 39:
        return 'F'

# Fungsi untuk menampilkan tabel nilai (No. 3)
def nilai_tabel(data, file_name="student.txt"):
    headers = ["NIM", "Nama Siswa", "Assignment 20%", "Quiz 15%", "Project 15%", "MID 25%", "Final 25%", "Nilai Akhir", "Grade"]
    table_data = []

    for row in data:
        nim = row["nim"]
        nama_siswa = row["nama_siswa"]
        nilai_assignment = row["nilai_assignment"]
        total_assignment = row["total_assignment"]
        nilai_quiz = row["nilai_quiz"]
        total_quiz = row["total_quiz"]
        project = row["project"]
        mid = row["mid"]
        final = row["final"]
        nilai_akhir = row["nilai_akhir"]
        grade_result = row["grade_nilai"]

        assignment_table = tabulate([nilai_assignment + [total_assignment]], headers=[f" {i}" for i in range(1, len(nilai_assignment) + 1)] + ["20%"], tablefmt="fancy_grid", numalign="right")
        quiz_table = tabulate([nilai_quiz + [total_quiz]], headers=[f" {i}" for i in range(1, len(nilai_quiz) + 1)] + ["15%"], tablefmt="fancy_grid", numalign="right")

        table_data.append([
            nim,
            nama_siswa,
            assignment_table,
            quiz_table,
            project,
            mid,
            final,
            nilai_akhir,
            grade_result
        ])

    # Simpan ke File
    with open(file_name, 'a') as file:
        file.write("\n### Menu 3: Menampilkan Data Nilai Dengan Tabel ###\n")
        file.write(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

    # Menampilkan tertinggi, terendah, dan jumlah yang tidak lulus
    highest_assignment = max([float(row["total_assignment"]) for row in data])
    lowest_assignment = min([float(row["total_assignment"]) for row in data])
    highest_quiz = max([float(row["total_quiz"]) for row in data])
    lowest_quiz = min([float(row["total_quiz"]) for row in data])
    highest_project = max([row["project"] for row in data])
    lowest_project = min([row["project"] for row in data])
    highest_mid = max([row["mid"] for row in data])
    lowest_mid = min([row["mid"] for row in data])
    highest_final = max([row["final"] for row in data])
    lowest_final = min([row["final"] for row in data])
    highest_nilai_akhir = max([row["nilai_akhir"] for row in data])
    lowest_nilai_akhir = min([row["nilai_akhir"] for row in data])
    tidak_lulus = sum([1 for row in data if row["nilai_akhir"] < 67])

    # Nilai tertinggi, terendah dan tidak lulus
    with open(file_name, 'a') as file:
        file.write("\n### Nilai Tertinggi dan Terendah serta Jumlah yang Tidak Lulus ###\n")
        file.write(f"Nilai Tertinggi: Assignment {highest_assignment}, Quiz {highest_quiz}, Project {highest_project}, MID {highest_mid}, Final {highest_final}, Nilai Akhir {highest_nilai_akhir}\n")
        file.write(f"Nilai Terendah: Assignment {lowest_assignment}, Quiz {lowest_quiz}, Project {lowest_project}, MID {lowest_mid}, Final {lowest_final}, Nilai Akhir {lowest_nilai_akhir}\n")
        file.write(f"Jumlah Orang Yang Tidak Lulus: {tidak_lulus}\n")


# Fungsi untuk menampilkan frekuensi grade (No. 4)
def frekuensi_grade(data, file_name="student.txt"):
    # Menyimpan ke File
    with open(file_name, 'a') as file:
        file.write("\n### Menu 4: Tampilkan Frekuensi Grade ###\n")
        grade_count = {'A': 0, 'A-': 0, 'B+': 0, 'B': 0, 'B-': 0, 'C+': 0, 'C': 0, 'C-': 0, 'D': 0, 'F': 0}
        for row in data:
            grade_count[row["grade_nilai"]] += 1
        file.write("\n\t Grade:\n")
        for key, value in grade_count.items():
            file.write(f"Yang Mendapat Grade {key}: {value} Orang\n")


# Fungsi untuk menampilkan menu (No. 6)
def menu():
    print('\n\tMenu  (Pilih Menu Untuk Ditampilkan Pada File)\n'
          '1. Menampilkan Nilai Akhir Mahasiswa\n'
          '2. Menampilkan Grade Bedasarkan Nilai Akhir Mahasiswa\n'
          '3. Menampilkan Data Nilai Dengan Tabel\n'
          '4. Tampilkan Frekuensi Grade\n'
          '5. Menampilkan Nilai Akhir Terurut (terbesar-terkecil)\n'
          '6. Memulai Ulang Program dari Awal\n'
          '7. Keluar'
          )

# Memulai program
data_result = hitung_nilai_akhir()
# Menu
while True:
    menu()
    pilihan = int(input('\nMasukan Pilihan Pada Menu: '))

    if pilihan == 1:
        file_name = "student.txt"
        with open(file_name, 'a') as file:
            file.write("\n### Menu 1: Menampilkan Grade Berdasarkan Nilai Akhir ###\n")
            for row in data_result:
                file.write(f"NIM: {row['nim']}, Nama: {row['nama_siswa']}, Nilai Akhir: {row['nilai_akhir']}\n")
        print("Output disimpan di:", file_name)

    elif pilihan == 2:
        file_name = "student.txt"
        with open(file_name, 'a') as file:
            file.write("\n### Menu 2: Menampilkan Grade Bedasarkan Nilai Akhir Mahasiswa ###\n")
            for row in data_result:
                file.write(f"NIM: {row['nim']}, Nama: {row['nama_siswa']}, Grade: {row['grade_nilai']}\n")
        print("Output disimpan di:", file_name)

    elif pilihan == 3:
        nilai_tabel(data_result)
        print("Output disimpan di:", file_name)

    elif pilihan == 4:
        frekuensi_grade(data_result)
        print("Output disimpan di:", file_name)

    elif pilihan == 5:
        file_name = "student.txt"
        with open(file_name, 'a') as file:
            file.write("\n### Menu 5: Menampilkan Nilai Akhir Terurut (terbesar-terkecil) ###\n")
            sorted_data = sorted(data_result, key=lambda x: x['nilai_akhir'], reverse=True)  # Mengurutkan Nilai Terbesar ke Terkecil (No. 5)
            for row in sorted_data:
                file.write(f"NIM: {row['nim']}, Nama: {row['nama_siswa']}, Nilai Akhir: {row['nilai_akhir']}, Grade: {row['grade_nilai']}\n")
        print("Output disimpan di:", file_name)

    elif pilihan == 6:
        data_result = hitung_nilai_akhir()

    elif pilihan == 7:
        print('Program Selesai.\nSilahkan Buka File Student.txt')
        break