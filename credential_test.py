import unittest
from credential import Credential
import pyperclip

class credential_test(unittest.TestCase):
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

    def test_create_new_profile(self):
        """
        test create_new_profile to test if a new object can be saved
        """
        self.new_profile.save_profile()
        self.assertEqual(len(Credential.profile_list),1)

    def tearDown(self):
        """
        tearDown() method that does clean up after each test case has run
        """
        Credential.profile_list = []
    
    def test_create_multiple_profiles(self):
        """
        test create_multiple_profile to test if multiple obejcts can be saved
        """
        self.new_profile.save_profile()
        test_profile = Credential("CircleCL","musyoka","musyokaisaac98@gmail.com")
        test_profile.save_profile()
        self.assertEqual(len(Credential.profile_list),2)

    def test_profile_exist(self):
        """
        test profile exists to check if there is another identical profile
        """
        test_profile1 = Credential("github","musyoka","musyokaisaac98@gmail.com")
        test_profile1.save_profile()
        prof = test_profile1.check_profile_exist("github","musyoka","musyokaisaac98@mail.com")
        self.assertTrue(prof)

    def test_search_profile(self):
        """
        test search profile to test if a user can be able to search for a profile_email
        """
        test_profile1 = Credential("github","musyoka","musyokaisaac98@gmail.com")
        test_profile1.save_profile()
        search_result = test_profile1.search_profile("github")
        self.assertEqual(test_profile1,search_result)

    def tearDown(self):
        """
		tearDown() method that does clean up after each test case has run
		"""
        Credential.profile_list = []

    def test_delete_profile(self):
        """
        test delete_profile to test if a user can be able to delete a particular profile
        """
        test_profile1 = Credential("github","musyoka","musyokaisaac98@mail.com")
        test_profile1.save_profile()
        test_profile1.delete_profile()
        self.assertEqual(len(Credential.profile_list),0)
    
    def test_copy_credentials(self):
        """
        test copy_credentials to test if a user can be able to copy an item to the clipboard
        """
        test_profile1 = Credential("github","musyoka","musyokaisaac98@gmail.com","testPassword")
        test_profile1.save_profile()
        Credential.copy_credentials("github")
        self.assertEqual(test_profile1.profile_password,pyperclip.paste())

    def test_display_all_profiles(self):
        """
        test display_all_profiles that tests if a user can be able to view all their profiles
        """
        self.assertEqual(Credential.display_profiles(),Credential.profile_list)


    
        
if __name__ == "__main__":
        unittest.main()         

