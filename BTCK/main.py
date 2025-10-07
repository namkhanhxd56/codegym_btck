import csv
import os
students = []
def add_student(student_id, name, age, major):
    for s in students:
        if s["student_id"] == student_id:
            print("ID đã tồn tại!")
            return
    student = {"student_id": student_id, "name": name, "age": age, "major": major}
    students.append(student)
    print(f"Thêm sinh viên {name} thành công!")

def update_student(student_id, name, age, major):
    for s in students:
        if s["student_id"] == student_id:
            if name != "":
                s["name"] = name
            if age != "":
                s["age"] = age
            if major !="":
                s["major"] = major
            print(f"Đã cập nhật thông tin Sinh viên {student_id}!")
            return
    print("Không tìm thấy sinh viên!")

def delete_student(student_id):
    for s in students:
        if s["student_id"] == student_id:
            students.remove(s)
            print(f"Đã xóa sinh viên")
            return
    print("Không tìm thấy sinh viên!")

def search_student_by_name(name_search):
    found = False
    for s in students:
        if name_search.lower() in s["name"].lower():
            print(f"ID: {s['student_id']}, Name: {s['name']}, Age: {s['age']}, Major: {s['major']}")
            found = True
    if not found:
        print("Không tìm thấy sinh viên nào với tên này!")


def show_students():
    if not students:
        print("Danh sách trống!")
        return
    print("\nDanh sách sinh viên:")
    for s in students:
        print(f"ID: {s['student_id']}, Name: {s['name']}, Age: {s['age']}, Major: {s['major']}")



def save_to_csv(filename="students.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["student_id", "name", "age", "major"])
        writer.writeheader()
        writer.writerows(students)
    print(f"Đã lưu danh sách vào {filename}")


def load_from_csv(filename="students.csv"):
    if not os.path.exists(filename):
        return
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    print(f"Đã tải dữ liệu từ {filename}")


def main():
    load_from_csv()

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Hiển thị danh sách sinh viên")
        print("6. Lưu & Thoát")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            student_id = input("Nhập ID: ")
            name = input("Nhập tên: ")
            age = input("Nhập tuổi: ")
            major = input("Nhập ngành học: ")
            add_student(student_id, name, age, major)
        elif choice == "2":
            student_id = input("Nhập ID sinh viên cần cập nhật: ")
            name = input("Tên mới (bỏ trống nếu giữ nguyên): ")
            age = input("Tuổi mới (bỏ trống nếu giữ nguyên): ")
            major = input("Ngành học mới (bỏ trống nếu giữ nguyên): ")
            update_student(student_id, name, age, major)
        elif choice == "3":
            student_id = input("Nhập ID sinh viên cần xóa: ")
            delete_student(student_id)
        elif choice == "4":
            name_search = input("Nhập tên cần tìm: ")
            search_student_by_name(name_search)
        elif choice == "5":
            show_students()
        elif choice == "6":
            save_to_csv()
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()