class MyClass:
    """ Init function to set the name and email (private)"""
    def __init__(self, name, email):
        if not email.endswith('@gmail.com'):
            raise ValueError('Email must end with "@gmail.com"')
        self.name = name
        self.__email = email


    @property
    def email(self):
        """
        This is the docstring for the 'email' property.
        It describes the purpose and behavior of the property.

        Returns:
            str: email.
        """
        return self.__email

    @email.setter
    def email(self, value):
        if not value.endswith('@gmail.com'):
            raise ValueError('Email address must end with "@gmail.com"')
        self.__email = str(value)
