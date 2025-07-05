
import json
import os

DATA_FILE = "food_data.json"

# Load existing data or create new
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def donate_food():
    name = input("👤 Donor Name: ")
    item = input("🍽️ Food Item: ")
    quantity = input("🔢 Quantity: ")

    data = load_data()
    data.append({
        "donor": name,
        "item": item,
        "quantity": quantity,
        "status": "available"
    })
    save_data(data)
    print("✅ Food donated successfully!\n")

def view_food():
    data = load_data()
    print("\n📦 Available Food Items:")
    found = False
    for idx, entry in enumerate(data):
        if entry["status"] == "available":
            found = True
            print(f"{idx + 1}. {entry['item']} - {entry['quantity']} (by {entry['donor']})")
    if not found:
        print("❌ No food available right now.\n")

def request_food():
    view_food()
    data = load_data()
    item_no = int(input("📥 Enter item number to request: ")) - 1
    if 0 <= item_no < len(data) and data[item_no]["status"] == "available":
        data[item_no]["status"] = "taken"
        save_data(data)
        print("✅ Food item requested successfully!\n")
    else:
        print("❌ Invalid selection.\n")

def main():
    while True:
        print("=== 🥗 FOOD SHARING SYSTEM ===")
        print("1. Donate Food")
        print("2. View Available Food")
        print("3. Request Food")
        print("4. Exit")
        choice = input("👉 Enter your choice: ")

        if choice == "1":
            donate_food()
        elif choice == "2":
            view_food()
        elif choice == "3":
            request_food()
        elif choice == "4":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again!\n")

if __name__ == "__main__":
    main()
