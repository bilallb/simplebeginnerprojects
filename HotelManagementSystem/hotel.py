import tkinter as tk
import random
import csv
from tkinter import ttk

# --- Data setup ---
clients = []
client_ids = []
rooms = [i for i in range(1, 151)]

class Client:
    def __init__(self, name, client_id, room, duration):
        self.name = name
        self.client_id = client_id
        self.room = room
        self.duration = duration

# Create CSV file header if not exists
with open('hotel_data.csv', 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Client ID', 'Name', 'Room', 'Duration (days)'])

# --- Tkinter window setup ---
root = tk.Tk()
root.title("Hotel Management System")
root.geometry("350x350")

# --- Widgets ---
tk.Label(root, text="Client Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Room Number (1–150):").pack()
room_entry = tk.Entry(root)
room_entry.pack()

tk.Label(root, text="Duration (days):").pack()
duration_entry = tk.Entry(root)
duration_entry.pack()

output_box = tk.Text(root, height=8, width=40)
output_box.pack(pady=10)

# --- Functions ---
def add_client():
    try:
        name = name_entry.get()
        room = int(room_entry.get())
        duration = int(duration_entry.get())

        if room not in rooms:
            output_box.insert(tk.END, f"Room {room} not available.\n")
            return

        client_id = random.randint(1, 100000)
        client = Client(name, client_id, room, duration)
        clients.append(client)
        rooms.remove(room)

        with open('hotel_data.csv', 'a', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow([client_id, name, room, duration])

        output_box.insert(tk.END, f"Added: {name}, Room {room}, ID {client_id}\n")

    except ValueError:
        output_box.insert(tk.END, "Invalid input. Room and duration must be numbers.\n")
def show_clients():
    output_box.delete('1.0', tk.END)
    if not clients:
        output_box.insert(tk.END, "No clients added yet.\n")
    else:
        for c in clients:
            output_box.insert(tk.END, f"{c.name} - Room {c.room} ({c.duration} days)\n")

# --- Buttons ---
tk.Button(root, text="Add Client", command=add_client).pack(pady=5)
tk.Button(root, text="Show Clients", command=show_clients).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()

style = ttk.Style()
available_themes = style.theme_names()
print(f"Available themes: {available_themes}")
def change_theme(theme_name):
    style.theme_use(theme_name)

change_theme('classic')
