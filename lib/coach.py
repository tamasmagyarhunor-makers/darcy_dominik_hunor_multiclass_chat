class Coach:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def count_submissions(self):
        count = 0
        for student in self.students:
            count += student.count_submissions()

        return count
    
    def print_student_names(self):
        names = [student.name for student in self.students]
        
        return ", ".join(names)
    
    def upload_submission_for_students(self, submission):
        for student in self.students:
            student.add_submission(submission)