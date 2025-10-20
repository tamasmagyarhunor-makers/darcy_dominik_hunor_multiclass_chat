from lib.coach import Coach
from unittest.mock import Mock

def test_coach_instantiates():
    coach = Coach('Eddie')

    assert coach.name == 'Eddie'
    assert coach.students == []

def test_coach_adds_students():
    coach = Coach('Eddie')
    student = Mock()
    student2 = Mock()

    coach.add_student(student)
    coach.add_student(student2)

    assert coach.students == [student, student2]

def test_coach_counts_learners_submissions():
    student = Mock()
    student.count_submissions.return_value = 2

    student2 = Mock()
    student2.count_submissions.return_value = 1

    coach = Coach('Eddie')
    coach.add_student(student)
    coach.add_student(student2)

    assert coach.count_submissions() == 3

def test_coach_can_print_student_names():
    student = Mock()
    student.name = 'Asha'

    student2 = Mock()
    student2.name = 'Jake'

    coach = Coach('Eddie')
    coach.add_student(student)
    coach.add_student(student2)

    assert coach.print_student_names() == 'Asha, Jake'

def test_coach_can_upload_submissions_for_students():
    student = Mock()
    student2 = Mock()

    coach = Coach('Eddie')
    coach.add_student(student)
    coach.add_student(student2)
    coach.upload_submission_for_students('tdd-a-function')

    student.add_submission.assert_called_once_with('tdd-a-function')
    student2.add_submission.assert_called_once_with('tdd-a-function')


    