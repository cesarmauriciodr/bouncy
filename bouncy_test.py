from unittest import TestCase

from bouncy import Bouncy

class TestBouncy(TestCase):
    """ test Bouncy """
    
    def setUp(self):
        self.bouncy_mock = Bouncy
        self.is_bouncy_mock = 132 
        self.is_not_bouncy_mock =321
    
    def test_is_bouncy_true(self):
        # test if number is bouncy
        self.assertEqual(self.bouncy_mock.is_bouncy(self.is_bouncy_mock), True)

    def test_is_bouncy_false(self):
        # test if number is not bouncy
        self.assertEqual(self.bouncy_mock.is_bouncy(self.is_not_bouncy_mock), False)

    def test_is_bouncy_if_param_is_not_int(self):
        # test if number is not int return 0
        self.assertEqual(self.bouncy_mock.is_bouncy("xyz"), 0)

    def test_least_number_bouncy_by_percentage_default_param(self):
        # test default param
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(), 21780)

    def test_least_number_bouncy_by_percentage_between(self):
        # test param between (1:99)  raises ValueError
        with self.assertRaises(ValueError):
            self.bouncy_mock.least_number_bouncy_by_percentage(100), 

    def test_least_number_bouncy_by_percentage_not_int(self):
        # test if number is not int raises TypeError
        with self.assertRaises(TypeError):
            self.bouncy_mock.least_number_bouncy_by_percentage("xyz"), 

    def test_least_number_bouncy_by_percentage(self):
        # test 0%
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(0), 99) 
        #  test 10%
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(10), 132)
        #  test 50%
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(50), 538)
        #  test 90%
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(90), 21780)
        #  test 99%
        self.assertEqual(self.bouncy_mock.least_number_bouncy_by_percentage(99), 1587000)
