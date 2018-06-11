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
    