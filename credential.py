class Credential:
    '''
    class that generates new instances of user credentials
    '''
    profile_list = []

    def __init__(self,profile_name=None,profile_username=None,profile_email=None,profile_password=None,):
        self.profile_name = profile_name
        self.profile_username = profile_username
        self.profile_email = profile_email
        self.profile_password = profile_password
    
    def save_profile(self):
        """
        save_profile method saves user object into profile_list
        """
        Credential.profile_list.append(self)

    @classmethod
    def check_profile_exist(cls,prof_name,prof_username=None,prof_email=None):
        """
        check_profile_exist method checks if a similar identical account already test_check_user_exists
        """
        for prof in cls.profile_list:
            if (prof.profile_name==prof_name) or (prof.profile_username == prof_username) or (prof.profile_email == prof_email):
                return True
            else:
                return False

        
