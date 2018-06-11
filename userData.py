from pylint.test.functional.inconsistent_returns import bug_1771_with_user_config

class User:
    user_list = []
    def __init__(self, username, password):
        """
        class that generates new instances of users
        """
        self.username = username
        self.password = password