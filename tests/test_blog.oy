import unittest
from app.models import Blog


class TestBlog(unittest.TestCase):
    def setUp(self):
        """
        Method that will run before every test
        """
        self.new_blog = Blog(
            user_id=1,
            category_id=1,
            title="Test Title",
            content="Test Content",
            image_path="https://res.cloudinary.com/james-m/image/upload/c_scale,w_455,f_webp/v1644698836/pexels-ella-olsson-1640777_qauhrg.jpg",
            created_at="2022-01-09"
        )

    def test_instance(self):
        """
        Test to check if the blog object is an instance of the Blog class
        """
        self.assertTrue(isinstance(self.new_blog, Blog))