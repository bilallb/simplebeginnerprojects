from datetime import datetime

import csv

my_file = 'empty_file.csv'

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
