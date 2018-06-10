

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
 
