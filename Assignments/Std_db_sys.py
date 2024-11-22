class StudentDatabase:
    def __init__(self):
        self.students = []
        self.id_counter = 1

    def add_student(self, name):
        if name.lower() in [student[1].lower() for student in self.students]:
            print(f"This name '{name}' is already in the list.")
        else:
            self.students.append((self.id_counter, name))
            self.id_counter += 1
            print(f"Student '{name}' added successfully.")

    def display_students(self):
        print("\nComplete List of Students (Tuples):")
        print(self.students)
        print("\nList of Students with IDs:")
        for student in self.students:
            print(f"ID: {student[0]}, Name: {student[1]}")

    def total_students(self):
        return len(self.students)

    def total_name_length(self):
        return sum(len(student[1]) for student in self.students)

    def longest_shortest_name(self):
        longest = max(self.students, key=lambda x: len(x[1]))
        shortest = min(self.students, key=lambda x: len(x[1]))
        return longest[1], shortest[1]

def main():
    db = StudentDatabase()
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        db.add_student(name)

    db.display_students()
    print(f"\nTotal number of students: {db.total_students()}")
    print(f"Total length of all student names combined: {db.total_name_length()}")
    longest, shortest = db.longest_shortest_name()
    print(f"The student with the longest name is: {longest}")
    print(f"The student with the shortest name is: {shortest}")

if __name__ == "__main__":
    main()
