class User:
    user_list = []

    def __init__(self, username, password):
        """
        class that generates new instances of users
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user object into user_list
        """
        User.user_list.append(self)

    @classmethod
    def find_user(cls, usern):
        """
        find_user method that checks if a username already exists
        """
        for user in cls.user_list:
            if user.username == usern:
                return True
            else:
                return False
    
    @classmethod
    def confirm_user(cls, usern, passw):
        """
        confirm_user method that checks if a given username matches the password
        """
        for user in cls.user_list:
            if cls.find_user(usern):
                password_match = user.password
                if password_match == passw:
                    return True
                else:
                    return False
            else:
                return False
    
    @classmethod
    def change_userpass(cls,usern,new_pass):
        """
        change_userpass method changes the password of a given user
        """
        for user in cls.user_list:
            if cls.find_user(usern):
                user.password = new_pass
                return user
            else:
                return

    def user_delete_account(self):
            User.user_list.remove(self)
   