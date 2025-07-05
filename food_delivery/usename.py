
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

DATA_FILE = "food_data.json"

# Data functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def donate_food():
    name = name_entry.get()
    item = item_entry.get()
    quantity = qty_entry.get()

    if not name or not item or not quantity:
        messagebox.showerror("Error", "All fields are required!")
        return

    data = load_data()
    data.append({
        "donor": name,
        "item": item,
        "quantity": quantity,
        "status": "available"
    })
    save_data(data)
    messagebox.showinfo("Success", "Food donated successfully!")
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    update_list()

def update_list():
    food_list.delete(*food_list.get_children())
    data = load_data()
    for idx, entry in enumerate(data):
        if entry["status"] == "available":
            food_list.insert("", "end", iid=idx, values=(entry["donor"], entry["item"], entry["quantity"]))

def request_food():
    selected = food_list.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a food item to request.")
        return
    idx = int(selected[0])
    data = load_data()
    data[idx]["status"] = "taken"
    save_data(data)
    update_list()
    messagebox.showinfo("Success", "Food item requested successfully!")

# GUI setup
root = tk.Tk()
root.title("🥗 Food Sharing System (GUI)")
root.geometry("600x400")
root.configure(bg="#f2f2f2")

# Donation section
tk.Label(root, text="Donor Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="Food Item:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
item_entry = tk.Entry(root, width=25)
item_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
qty_entry = tk.Entry(root, width=25)
qty_entry.grid(row=2, column=1, padx=10)

tk.Button(root, text="Donate Food", command=donate_food, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

# Food list display
columns = ("Donor", "Item", "Quantity")
food_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    food_list.heading(col, text=col)
food_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Request button
tk.Button(root, text="Request Selected Food", command=request_food, bg="blue", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

update_list()
root.mainloop()
