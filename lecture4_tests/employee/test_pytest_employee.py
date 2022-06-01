import unittest
from employee import Employee


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Oleksandr', 'Bletska', 20)

    def test_email(self):
        self.assertEqual(self.employee.email, 'Oleksandr.Bletska@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Oleksandr Bletska')

    def test_apply_raise(self):
        self.assertEqual(self.employee.pay * Employee.raise_amt, 21)
# --------------------------------------------------------------------------------
# from employee import Employee
#
# employee = Employee('Oleksandr', 'Bletska', 20)
#
#
# def test_email():
#     assert employee.email == 'Oleksandr.Bletska@email.com'
#
#
# def test_fullname():
#     assert employee.fullname == 'Oleksandr Bletska'
#
#
# def test_apply_raise():
#     assert employee.pay * employee.raise_amt == 21
