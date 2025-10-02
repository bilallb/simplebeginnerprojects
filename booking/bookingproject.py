from datetime import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt


my_file = 'empty_file.csv'
# opening the file and creating the columns
with open(my_file, 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(["Name","Status","Time"])
class Client:
    def __init__(self, name, status, time, min_gap=60):
        self.__name = name
        self.status = status
        self.time = time
        self.min_gap = min_gap

    @property
    def show_name(self):
        return self.__name

    @show_name.setter
    def show_name(self, value):
        self.__name = str(value)

    def is_time_valid(self, existing_times):
        new_dt = datetime.strptime(self.time, "%H:%M")
        for t in existing_times:
            existing_dt = datetime.strptime(t, "%H:%M")
            if abs((new_dt - existing_dt).total_seconds()) / 60 < self.min_gap:
                return False
        return True

clients = []
# function we use
def within_time_range(self):
    try:
        """Return True if the time is between 08:00 and 22:00 inclusive."""
        user_dt = datetime.strptime(self.time, "%H:%M")
        start_dt = datetime.strptime("08:00", "%H:%M")
        end_dt   = datetime.strptime("22:00", "%H:%M")
        return start_dt <= user_dt <= end_dt
    except ValueError:
        print("Invalid time")
def represent(x, y):
    choose = input('Bar, plot or scatter?')
    if choose.lower() == 'bar':
        plt.bar(x, y)
        plt.show()
    elif choose.lower() == 'plot':
        plt.plot(x, y)
        plt.show()
    elif choose.lower() == 'scatter':
        plt.scatter(x, y)
        plt.show()
def load_file(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("File not found or empty.")
    finally:
        print("File opened.")

def condition():
    if choice.lower() == 'yes':
        second_choice = input('What do you want to plot: Name, Status, Time? (ex: n&s, s&t) ')
        if second_choice.lower() == 'n&s':
            represent(data['Name'], data['Status'])
        elif second_choice.lower() == 's&t':
            represent(data['Status'], data['Time'])
        elif second_choice.lower() == 'n&t':
            represent(data['Name'], data['Time'])
        else:
            print("Invalid input. Please try again.")
#phase where we take info from the client
while True:
    thename = input("Enter your name ('stop' to exit): ")
    if thename.lower() == 'stop':
        break

    the_status = input("Are you active? (yes/no/'stop' to exit): ")
    while the_status.lower() not in ['yes', 'no', 'stop']:
        print("Invalid input. Please try again.")
        the_status = input("Are you active? (yes/no/'stop' to exit): ")
    if the_status.lower() == 'stop':
        break
    the_time = input("Enter your time ('stop' to exit): ")
    if the_time.lower() == 'stop':
        break
    client = Client(thename, the_status, the_time)
    # Validate time to avoid conflicts

    while not client.is_time_valid([c.time for c in clients]):
        print("Time already taken or too close to existing times.")
        new_time = input("Enter your time ('stop' to exit): ")
        if new_time.lower() == 'stop':
            break
        client.time = new_time

    clients.append(client)
    with open(my_file, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([client.show_name, client.status, client.time])
    print([c.show_name for c in clients], [c.status for c in clients], [c.time for c in clients])
    data = load_file('empty_file.csv')
    print(data)

data = load_file('empty_file.csv')
print(data)

counts = data['Status'].value_counts()
print(f'Active clients: {counts.get('yes', 0)}')
print(f'Non active clients: {counts.get('no', 0)}')

try:
    choice = input('Do you want to plot something and represent it ?')
    condition()
except ValueError:
    print("Invalid input. Please try again.")
