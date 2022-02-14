import unittest
from app.models import Role


class TestROle(unittest.TestCase):
    """
    Test class to test the behaviour of the Role class
    """

    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_role = Role(name="Admin")

    def test_instance(self):
        """
        Test to check if the new_comment is an instance of Subscriber
        """
        self.assertTrue(isinstance(self.new_role, Role))