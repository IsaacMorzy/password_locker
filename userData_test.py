from userData import User
import unittest

class user_test(unittest.TestCase):
    """
	Test class that defines test cases for the userData class behaviors
	Args:
	unittest.TestCase:TestCase class that helps in creating test cases
	"""
    def setUp(self):
        """
		set up method to run each test case
		"""
        self.new_user = User("username", "password")


if __name__ == "__main__":
    unittest.main()
