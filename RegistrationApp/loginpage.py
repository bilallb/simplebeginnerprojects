import pandas as pd
import tkinter as tk
from tkinter import messagebox

class MyClass:
    def __init__(self, name, class_email):
        self.__class_email = class_email
        self.name = name

    @property
    def email(self):
        return self.__class_email

    @email.setter
    def email(self, value):
        if not value.endswith('@gmail.com'):
            raise ValueError('Email address must end with "@gmail.com"')
        self.__class_email = str(value)

# ------------------------
# File functions
# ------------------------
def load_file(filename):
    try:
        df = pd.read_csv(filename)
        if df.empty:
            print('File is empty')
            return pd.DataFrame(columns=['Name', 'Email'])
        return df
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame(columns=['Name', 'Email'])
    except pd.errors.EmptyDataError:
        print('File is empty [no data]')
        return pd.DataFrame(columns=['Name', 'Email'])

def add_client(filename):
    df = load_file(filename)
    existing_email = set(df['Email'].tolist())

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
        df.loc[len(df)] = [the_client.name, the_client.email]
        existing_email.add(email)
        print(f'Added {username} successfully')

    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')
    return df

# ------------------------
# GUI
# ------------------------
def tkinter_setup():
    root = tk.Tk()
    root.title('User Registration')
    root.geometry('400x250')
    root.resizable(False, False)

    tk.Label(root, text='Username:', font=('Arial', 12)).pack(pady=10)
    username_entry = tk.Entry(root, width=40)
    username_entry.pack()

    tk.Label(root, text='Email:', font=('Arial', 12)).pack(pady=10)
    email_entry = tk.Entry(root, width=40)
    email_entry.pack()

    def submit():
        username = username_entry.get().strip()
        email = email_entry.get().strip()

        if not username:
            messagebox.showerror('Error', 'Username cannot be empty')
            return
        if not username.isalnum() or not (3 <= len(username) <= 20):
            messagebox.showerror('Error', 'Username must be 3–20 chars and alphanumeric')
            return
        if not email.endswith('@gmail.com'):
            messagebox.showerror('Error', 'Email format is incorrect')
            return

        try:
            df = load_file('empty_file.csv')
            client = MyClass(username, email)
            df.loc[len(df)] = [client.name, client.email]
            df.to_csv('empty_file.csv', index=False)
            messagebox.showinfo('Success', f"User '{client.name}' added successfully!")
            username_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror('Error', str(e))

    tk.Button(root, text='Register', command=submit, bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=20)
    root.mainloop()

# ------------------------
# Main program
# ------------------------
if __name__ == "__main__":
    global_choice = input('Do you want to use GUI? (y/n): ').strip().lower()

    if global_choice == 'y':
        tkinter_setup()
    else:
        terminal_choice = int(input("Enter your choice (1-Add user / 2-View User / 3-Delete User): "))
        if terminal_choice == 1:
            clients_df = add_client('empty_file.csv')
            print('\nRegistered Users:')
            print(clients_df)
