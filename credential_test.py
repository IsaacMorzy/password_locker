import unittest 
from credential import Credential
import pyperclip


class CredentialTest(unittest.TestCase):
    """Test class that defines test cases for the credential class behaviours
        Args:
        unittest.TestCase:TestCase class that helps in creating cases
    """
    def setUp(self):
        """
        setup method to define instructions that will be executed before each test method.
        """
        self.new_profile = Credential("Codewars","Isaac","musyokaisaac98@gmail.com","password") # setUp() method to create a new instance of Credential class,before each test method declared, and store it in an instance variable in the test class self.new_profile.

    def test_init(self):
        """
        test init to check if our objects are instantiated correctly
        """
        self.assertTrue(self.new_profile.profile_name,"Codewars") #  self.assertEqual():A TestCase method that checks for an expected result.
        self.assertTrue(self.new_profile.profile_username,"Isaac")
        self.assertTrue(self.new_profile.profile_email,"musyokaisaac98@gmail.com")
        self.assertTrue(self.new_profile.profile_password)

if __name__ == '__main__':
    unittest.main()

    # def test_create_new_profile(self):
    #     """
    #     test create_new_profile to test if a new object can be saved
    #     """
    #     self.new_profile.save_profile()
    #     self.assertEqual(len(Credential.profile_list),1)

