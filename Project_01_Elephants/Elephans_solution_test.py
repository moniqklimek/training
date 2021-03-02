"""
"ElephantsTest" class to test file: "Elephans_solution.py" and inside class: "Elephants"
"""
#import Elephans_solution
from Elephans_solution import Elephants 
import unittest

import mock #input from User 


class ElephantsTest(unittest.TestCase):
    def setUp(self):
        self.elephants=Elephants()

    def test_read_data(self):
        line1 = "6"
        line2 = "2400 2000 1200 2400 1600 4000"
        line3 = "1 4 5 3 6 2"
        line4 = "5 3 2 4 6 1"
        with mock.patch('builtins.input', return_value=line1):
            self.elephants.read_data_n()
        self.assertEqual(self.elephants.n_amouth_elephans_in_ZOO, 6)

        with mock.patch('builtins.input', return_value=line2):
            self.elephants.read_data_elephans_weight()
        self.assertEqual(self.elephants.elephants_in_kilograms, [2400, 2000, 1200, 2400, 1600, 4000])

        with mock.patch('builtins.input', return_value=line3):
            self.elephants.read_data_a1_employee()
        self.assertEqual(self.elephants.a1, [1, 4, 5, 3, 6, 2])

        with mock.patch('builtins.input', return_value=line4):
            self.elephants.read_data_b1_boss()
        self.assertEqual(self.elephants.b1, [5, 3, 2, 4, 6, 1])


    def test_create_dict_KEY_valueb1_and_VALUE_indexb1(self):
        whole_dict_create_with_tab_b1 = self.elephants.create_dict_KEY_valueb1_and_VALUE_indexb1([5, 3, 2, 4, 6, 1])
        self.assertEqual(whole_dict_create_with_tab_b1, {5: 0, 3: 1, 2: 2, 4: 3, 6: 4, 1: 5})

        first_value=whole_dict_create_with_tab_b1[5]
        self.assertEqual(first_value,0)

        last_value = whole_dict_create_with_tab_b1[6]
        self.assertNotEqual(last_value, 1)


    def test_create_dict_KEY_valueb1_and_VALUE_indexb1_negative(self):
        whole_dict_create_with_tab_b1 = self.elephants.create_dict_KEY_valueb1_and_VALUE_indexb1([5, 3, 2, 4, 6, 1])
       
        first_value_is_not = whole_dict_create_with_tab_b1[5]
        self.assertNotEqual(first_value_is_not, 5)

    def test_create_cycles(self):
        tab_cycles = self.elephants.create_cycles([1, 4, 5, 3, 6, 2], [5, 3, 2, 4, 6, 1])
        self.assertEqual(tab_cycles[0], [1, 2, 5])
        self.assertEqual(tab_cycles[1], [4, 3])
        self.assertEqual(tab_cycles[2], [6])
        self.assertEqual(len(tab_cycles), 3)

    def test_create_cycles_negative(self):
        tab_cycles_negative = self.elephants.create_cycles([1, 4, 5, 3, 6, 2], [5, 3, 2, 4, 6, 1])
        self.assertNotEqual(tab_cycles_negative[0], [6])
        self.assertNotEqual(tab_cycles_negative[1], [3, 3])
        self.assertNotEqual(tab_cycles_negative[2], [1, 2, 5])
        self.assertNotEqual(len(tab_cycles_negative), 2)

    def test_sum_mass_elephants_one_cycle(self):
        check = self.elephants.sum_mass_elephants_one_cycle([1, 2, 5], [0, 2400, 2000, 1200, 2400, 1600, 4000])
        self.assertEqual(check, (2400+2000+1600))
        
        tab = self.elephants.sum_mass_elephants_one_cycle([4, 3], [0,2400, 2000, 1200, 2400, 1600, 4000])
        self.assertEqual(tab, (1200+2400))

        tab = self.elephants.sum_mass_elephants_one_cycle([6], [0,2400, 2000, 1200, 2400, 1600, 4000])
        self.assertEqual(tab, (4000))
    
    def test_sum_mass_elephants_one_cycle_negative(self):
        tab = self.elephants.sum_mass_elephants_one_cycle([4, 3], [0, 2400, 2000, 1200, 2400, 1600, 4000])
        self.assertNotEqual(tab, (12000+2400))

        tab = self.elephants.sum_mass_elephants_one_cycle([6], [0, 2400, 2000, 1200, 2400, 1600, 4000])
        self.assertNotEqual(tab, (40000))
    
    def test_calculate_chose_method1_or_method2(self):
        check = self.elephants.calculate_chose_method1_or_method2(
            [[1, 2, 5], [3, 4], [6]], [2400, 2000, 1200, 2400, 1600, 4000])
        self.assertEqual(check, (11200))

        check_wrong = self.elephants.calculate_chose_method1_or_method2(
            [[1, 2, 5], [3, 4], [6]], [2400, 2000, 1200, 2400, 1600, 4000])
        self.assertIsNot(check_wrong, (11000))


if __name__ == "__main__":
    unittest.main()


"""
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK

"""