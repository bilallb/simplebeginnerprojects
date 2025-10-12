"""
Importing things we need
"""

from Models import MyClass
from database import dataframe
def add_client(filename):
    """
    Adding the client infos to the csv file
    """
    existing_email = set(dataframe['Email'].tolist())

    while True:
        username = input("Please enter your username ('exit' to stop): ").strip()
        if username.lower() == "exit":
            break
        if not username.isalnum() or not (3 <= len(username) <= 20):
            print("Username must contain only alphanumeric characters (3–20 chars).")
            continue

        email = input("Please enter your email ('exit' to stop): ").strip()
        if email.lower() == "exit":
            break
        if not email.endswith('@gmail.com'):
            print("Email format is incorrect! ")
            continue
        elif email in existing_email:
            print('Email already in use')
            continue

        the_client = MyClass(username, email)
        dataframe.loc[len(dataframe)] = [the_client.name, the_client.email]
        existing_email.add(email)
        print(f'Added {username} successfully')

    dataframe.to_csv(filename, index=False)
    print(f'Data saved to {filename}')
    return dataframe
