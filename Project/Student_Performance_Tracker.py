class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0  # Avoid division by zero
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self, passing_score=40):
        for student in self.students.values():
            average = student.calculate_average()
            passing_status = "Passing" if student.is_passing(passing_score) else "Failing"
            print(f"Name: {student.name}, Average Score: {average:.2f}, Status: {passing_status}")


def main():
    tracker = PerformanceTracker()

    while True:
        print("\n1. Add Student\n2. Display Performance\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter {subject} score: "))
                        scores.append(score)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            tracker.add_student(name, scores)

        elif choice == "2":
            if not tracker.students:
                print("No students added.")
            else:
                tracker.display_student_performance()
                print(f"\nClass Average: {tracker.calculate_class_average():.2f}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
