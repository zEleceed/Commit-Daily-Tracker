from pathlib import Path
from datetime import datetime


def append_comments(file_path: Path, comment: str):
    # Function to append a comment with current date/time to a students .txt
    current_date = datetime.now().strftime("%Y/%m/%d")  # Formatting with Year/Month/Day
    with open(file_path, "a") as file:
        file.write(f"{current_date}: {comment}\n")


def create_student_file(file_path: Path):
    # Create an empty file for the student.
    file_path.touch()


def read_file(file_path: Path):
    # If needed, read and display all comments from the file.
    with open(file_path, "r") as file:
        print(f'All saved comments:')
        print(file.read())


def get_all_students_files(directory: Path):
    # This function will return all student.txt in a directory to view.
    # It will return a dictionary, so it will be easier to access them later.
    txt_files = sorted(directory.glob(".txt"), key=lambda f: f.name)  # Sort students alphabetically
    students_dictionary = {}
    index = 1

    for student in txt_files:
        students_dictionary[index] = student
        index += 1
    return students_dictionary


def main():
    working_dir = Path.cwd()

    while True:
        list_of_students = get_all_students_files(working_dir)
        print("All Listed Students!")

        # Print out all the students in the directory with x: student format
        for index, student in list_of_students.items():
            print(f'{index}: {student}')

        input_command = input(F"Choose or Create a Student(+), or type 'break' to exit: ")

        if input_command == "+":
            input_students_name = input(f"Student's name: ")
            if not input_students_name.endswith(".txt"):
                student_file_name = input_students_name + ".txt"
            else:
                student_file_name = input_students_name

            create_student_file(working_dir / student_file_name) # This will create our student .txt file


        elif input_command == "break":
            break


if __name__ == "__main__":
    main()
