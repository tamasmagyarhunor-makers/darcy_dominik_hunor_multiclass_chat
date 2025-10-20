from lib.student import Student
from lib.coach import Coach

def test_coach_can_add_students():
    student = Student('Loredana')
    student2 = Student('Mikhail')

    coach = Coach('Sarah')

    coach.add_student(student)
    coach.add_student(student2)

    assert coach.students == [student, student2]

def test_coach_can_count_student_submissions():
    student = Student('Loredana')
    student2 = Student('Mikhail')
    student.add_submission('tdd-a-class')
    student2.add_submission('tdd-a-function')
    student2.add_submission('tdd-a-class')

    coach = Coach('Sarah')

    coach.add_student(student)
    coach.add_student(student2)

    assert coach.count_submissions() == 3

def test_coach_can_print_student_names():
    student = Student('Loredana')
    student2 = Student('Mikhail')
    student3 = Student('Nguyen')

    coach = Coach('Sarah')

    coach.add_student(student)
    coach.add_student(student2)
    coach.add_student(student3)

    assert coach.print_student_names() == 'Loredana, Mikhail, Nguyen'

def test_coach_can_upload_submissions_for_students():
    student = Student('Loredana')
    student2 = Student('Mikhail')
    student.add_submission('tdd-a-class')
    student2.add_submission('tdd-a-function')
    student2.add_submission('tdd-a-class')

    coach = Coach('Hunor')

    coach.add_student(student)
    coach.add_student(student2)

    coach.upload_submission_for_students('HUNOR-extra-challenge')
    assert student.submissions[1] == 'HUNOR-extra-challenge'
    assert student2.submissions[2] == 'HUNOR-extra-challenge'
    assert coach.count_submissions() == 5