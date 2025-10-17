from lib.student import Student

def test_student_instantiates():
    student = Student('Sarah')

    assert student.name == 'Sarah'
    assert student.submissions == []

def test_student_adds_submission():
    student = Student('Sarah')
    student.add_submission('tdd-a-function')
    student.add_submission('git-cmd-line-challenge')

    assert student.submissions == ['tdd-a-function', 'git-cmd-line-challenge']

def test_student_counts_submission():
    student = Student('Sarah')
    student.add_submission('tdd-a-function')
    student.add_submission('git-cmd-line-challenge')

    assert student.count_submissions() == 2