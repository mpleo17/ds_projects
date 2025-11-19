import unittest
from unittest.mock import patch, Mock
from code.my_calc import Calculations, Employee
from code.my_code import Calc

class TEST_CALCULATION(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Calculations(-5,5).get_sum(), 0)
        self.assertEqual(Calculations(10,5).get_sum(), 15)
    
    def test_sub(self):
        self.assertEqual(Calculations(-5,-5).get_diff(), 0)
        self.assertEqual(Calculations(-5, 5).get_diff(), -10)
        
    def test_product(self):
        self.assertEqual(Calculations(-5,5).get_product(), -25)
        self.assertEqual(Calculations(0,200).get_product(), 0)
        
    def test_divide(self):
        self.assertEqual(Calculations(-20,5).get_quotient(), -4)
        self.assertEqual(Calculations(0,200).get_quotient(), 0)
        with self.assertRaises(ValueError) as ar:
            Calculations(100,0).get_quotient()

class TEST_EMPLOYEE(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass runs only once in the beginning!')
        
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass runs only once in the end!')

    def setUp(self):
        print('Generating employee instances!')
        self.e1 = Employee(name='ABC', age=28, salary=60000)
        self.e2 = Employee(name='DEF', age=29, salary=70000)

    def tearDown(self):
        print('Destroying employee instances!')
        del self.e1
        del self.e2

    def test_employee_raise(self):
        print('testing employee raise amnt!')
        self.assertEqual(self.e1.raise_amt(), 60000 * 0.04)
        self.assertEqual(self.e2.raise_amt(), 70000 * 0.04)

    def test_employee_schedule(self):
        with patch('code.my_calc.requests.get') as mocked_obj:
            mocked_obj.return_value.ok = True
            mocked_obj.return_value.text = 'Success'

            schedule = self.e1.monthly_schedule('May')
            mocked_obj.assert_called_with('http:/example.com/ABC/May')
            self.assertEqual(schedule, 'Success')

            mocked_obj.return_value.ok = False

            schedule = self.e2.monthly_schedule('June')
            mocked_obj.assert_called_with('http:/example.com/DEF/June')
            self.assertEqual(schedule, 'Bad Response!')

class TEST_MY_CODE(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_add(self):
        print('test_add')
        self.assertEqual(Calc(10,15).calc_add(), 25)
        self.assertEqual(Calc(15, -15).calc_add(), 0)
        self.assertEqual(Calc(0, 0).calc_add(), 0)

    @unittest.expectedFailure
    def test_diff(self):
        print('test_diff')
        self.assertEqual(Calc(10,15).calc_sub(), -50)
        self.assertEqual(Calc(15, -15).calc_sub(), 300)
        self.assertEqual(Calc(0, 0).calc_sub(), 0)

    def test_mul(self):
        print('test_mul')
        self.assertEqual(Calc(10,15).calc_mult(), 150)
        self.assertEqual(Calc(15, -15).calc_mult(), -225)
        self.assertEqual(Calc(0, 0).calc_mult(), 0)

    def test_div(self):
        print('test_div')
        self.assertEqual(Calc(15,10).calc_div(), 1.5)
        self.assertEqual(Calc(15, -15).calc_div(), -1)
        self.assertEqual(Calc(0, -15).calc_div(), 0)
        with self.assertRaises(ValueError):
            Calc(0, 0).calc_div()

    def test_timestamp(self):
        with patch('code.my_code.time.time') as mocked_obj:
            mocked_obj.return_value = '12345678910'
            ts = Calc(15,10).get_timestamp()
            self.assertEqual(ts, '12345678910')
            mocked_obj.assert_called_once()
    
if __name__ == '__main__':
    unittest.main()