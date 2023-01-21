import unittest

import employee_class
from employee_class import Employee

class TestEmployeeClass(unittest.TestCase):
    
    def setUp(self):
        first = 'Hadrian'
        last = 'Hu'
        salary = 60000        
        self.employee = Employee(first,last,salary)
        self.salaries = {70000, 260000}
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertIn(self.employee.salary+5000,self.salaries)
        
    def test_give_custom_raise(self):
        self.employee.give_custom_raise(100000)
        self.assertIn(self.employee.salary+100000,self.salaries)

if __name__ == '__main__':
    unittest.main()