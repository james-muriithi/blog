import unittest
from app.models import Subscriber


class TestSubscriber(unittest.TestCase):
    """
    Test class to test the behaviour of the Subscriber class
    """

    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_subscriber = Subscriber(name="Food")

    def test_instance(self):
        """
        Test to check if the new_comment is an instance of Subscriber
        """
        self.assertTrue(isinstance(self.new_subscriber, Subscriber))