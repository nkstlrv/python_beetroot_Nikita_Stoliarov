# Task 1

# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. 
# The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.

# Email validations:
# Valid email address format 
# Email address 


class SignUp:

    def __init__(self, email, password):

        self._email_validator(email)
        self.email = email
        self.__password = password
        print("Congratulations! You have succesfully signed-up")


    def _email_validator(self, email: str):

        email_list = list(email)
        unsupported_chars = ['!', '#', '$', '%', '^', ';', ':', '&', '?', '*', ')', '(', '=', '+', '}', '{']

        if any(item in unsupported_chars for item in email_list):
            raise ValueError("Email can not contain unsupported chars: {}".format(unsupported_chars))
        
        elif len(email) > 30 or len(email) == 0:
            raise ValueError("Inapropriate email lenght")
        
        elif email[-1] == '@' or email[-1] == '.':
            raise ValueError("Email can not end by '@' or '.'")
        
        elif '@' not in email_list:
            raise ValueError("Wrong email format! Example: example@mail.com")
        
        elif '.' not in email_list:
            raise ValueError("Wrong email format! Example: example@mail.com")
        
        elif email_list.count('@') > 1:
            raise ValueError("Wrong email format! Example: example@mail.com")
        
        
        
    
s = SignUp('example@mail.com', 123456)



