import unittest
from app.models import Category


class TestCategory(unittest.TestCase):
    """
    Test class to test the behaviour of the Category class
    """

    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_category = Category(name="Food")

    def test_instance(self):
        """
        Test to check if the new_comment is an instance of category
        """
        self.assertTrue(isinstance(self.new_category, Category))