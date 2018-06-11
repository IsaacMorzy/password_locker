from userData import User
import unittest

class user_test(unittest.TestCase):
    """
    Test class that defines test cases for the userData class behaviors
    Args:
    unittest.TestCase:TestCase class that helps in creating test cases
    """

    def test_init(self):
        """
        test init test case to test if the object is initialised properly
        """
        self.assertEqual(self.new_user.username,"username")
        self.assertEqual(self.new_user.password, "password")

    def setUp(self):
        """
		set up method to run each test case
		"""
        self.new_user = User("username", "password")
        
    def test_create_new_account(self):
        """
		test create new account test case to test if the new user object is saved into the user list
		"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        """
    	tearDown() method that does clean up after each test case has run
		"""
        User.user_list = []
    def test_check_user_exists(self):
        """
        test check user exists to test if a user exists or not
        """
        self.test_user = User("username","password1")
        self.test_user.save_user()
        found_user = User.find_user("username")
        self.assertTrue(found_user)


if __name__ == "__main__":
    unittest.main()

