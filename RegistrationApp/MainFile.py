""" importing modules """
from database import *
from gui import *
from cli import *
# ------------------------
# Main program
# ------------------------
if __name__ == "__main__":
    global_choice = input('Do you want to use GUI? (y/n): ').strip().lower()

    if global_choice == 'y':
        tkinter_setup()
        print('GUI must be running right now! ')
    else:
        terminal_choice = int(input("Enter your choice (1-Add user / 2-View User / 3-Delete User): "))
        if terminal_choice == 1:
            clients_df = add_client(FILENAME)
            print('\nRegistered Users:')
            print(clients_df)
        elif terminal_choice == 2:
            df = load_file()
            print(df)
        elif terminal_choice == 3:
            df = load_file()
            email_to_delete = input("Enter email to delete: ").strip()
            df = df[df['Email'] != email_to_delete]
            df.to_csv(FILENAME, index=False)
            print(f'{email_to_delete} removed successfully')

