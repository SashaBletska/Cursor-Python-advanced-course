from employee import Employee

employee = Employee('Oleksandr', 'Bletska', 20)


def test_email():
    assert employee.email == 'Oleksandr.Bletska@email.com'


def test_fullname():
    assert employee.fullname == 'Oleksandr Bletska'


def test_apply_raise():
    assert employee.pay * employee.raise_amt == 21
