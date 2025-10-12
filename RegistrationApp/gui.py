"""
Importing things we need
"""
import tkinter as tk
from tkinter import messagebox
from database import dataframe
from Models import MyClass
def tkinter_setup():
    """
    Setting up the interface of the GUI
    """
    root = tk.Tk()
    root.title('User Registration') #App title
    root.geometry('400x250') # size of the figure
    root.resizable(False, False) # disabling changing the size

    tk.Label(root, text='Username:', font=('Arial', 12)).pack(pady=10) # first label username
    username_entry = tk.Entry(root, width=40) # creating the entry where we get the username from the user
    username_entry.pack() # packing

    tk.Label(root, text='Email:', font=('Arial', 12)).pack(pady=10) # Second label
    email_entry = tk.Entry(root, width=40) # Creating the entry where we get the email from user
    email_entry.pack() #packing again

    def submit():
        """
        Checking GUI data and raising errors when needed
        """
        username = username_entry.get().strip()
        email = email_entry.get().strip()
        emails = dataframe['Email'].tolist()
        # if statement to check for errors
        if not username: # if nothing is entered in username raise error
            messagebox.showerror('Error', 'Username cannot be empty')
            return
        if not username.isalnum() or not (3 <= len(username) <= 20): # if name is not alphanumeric or less than 3 words raise error
            messagebox.showerror('Error', 'Username must be 3–20 chars and alphanumeric')
            return
        if not email.endswith('@gmail.com'): # if the format of the email is incorrect
            messagebox.showerror('Error', 'Email format is incorrect')
            return
        if email in emails:
            messagebox.showerror('Error', 'Email already in use')
            return
        try:
            client = MyClass(username, email)
            dataframe.loc[len(dataframe)] = [client.name, client.email]
            dataframe.to_csv('empty_file.csv', index=False)
            messagebox.showinfo('Success', f"User '{client.name}' added successfully!")
            username_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror('Error', str(e))

    tk.Button(root, text='Register', command=submit, bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=20)
    root.mainloop()



