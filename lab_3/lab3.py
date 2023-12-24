import csv
from sys import argv

class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class StudentList:
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        insert_position = 0
        for item in self.students_list:
            if student.name > item.name:
                insert_position += 1
            else:
                break
        self.students_list.insert(insert_position, student)

    def delete_student(self, name):
        delete_position = -1
        for item in self.students_list:
            if name == item.name:
                delete_position = self.students_list.index(item)
                break
        if delete_position != -1:
            del self.students_list[delete_position]

    def update_student(self, updated_student):
        update_position = -1
        for item in self.students_list:
            if updated_student.name == item.name:
                update_position = self.students_list.index(item)
                break

        if update_position != -1:
            del self.students_list[update_position]
            self.add_student(updated_student)

    def print_all_students(self):
        print("#" * 10 + '  All list  ' + '#' * 10)
        for student in self.students_list:
            print(f'Student: name is {student.name}, phone is {student.phone}')
        print("#" * 20)

class Utils:
    @staticmethod
    def load_back_file(file_path):
        data = []
        with open(file_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lowercased_row = {key.lower(): value for key, value in row.items()}
                data.append(lowercased_row)
        params = tuple(data[0].keys()) if data else ('name', 'phone')
        return data, params

    @staticmethod
    def save_all_data(students_list, params, path):
        with open(path, "w", newline='') as csvfile:
            fieldnames = params
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students_list:
                writer.writerow(vars(student))
        print('All data saved!')


def get_new_params(param_tuple):
    new_params = {}
    for param in param_tuple:
        new_params[param] = input(f'Please enter student {param}: ')
    return new_params


def main():
    back_file = 'lab3.csv' if len(argv) == 1 else argv[1]

    students_data, params = Utils.load_back_file(back_file)
    student_list = StudentList()

    for data in students_data:
        student_list.add_student(Student(**data))

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.lower() == "c":
            new_student = Student(**get_new_params(params))
            student_list.add_student(new_student)
            student_list.print_all_students()
        elif choice.lower() == "u":
            updated_student = Student(**get_new_params(params))
            student_list.update_student(updated_student)
            student_list.print_all_students()
        elif choice.lower() == "d":
            name_to_delete = input("Please enter name to be deleted: ")
            student_list.delete_student(name_to_delete)
        elif choice.lower() == "p":
            student_list.print_all_students()
        elif choice.lower() == "x":
            break
        else:
            print("Wrong choice")

    Utils.save_all_data(student_list.students_list, params, "lab3_out.csv")


if __name__ == '__main__':
    main()