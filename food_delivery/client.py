
import tkinter as tk
import requests

API_BASE = "http://127.0.0.1:5000/api"

class FoodDeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Delivery App")
        self.food_items = []
        self.cart = []

        self.food_frame = tk.Frame(root)
        self.food_frame.pack()

        self.cart_frame = tk.Frame(root)
        self.cart_frame.pack()

        self.load_food_items()

    def load_food_items(self):
        response = requests.get(f"{API_BASE}/foods")
        if response.status_code == 200:
            self.food_items = response.json()
            self.show_food_items()

    def show_food_items(self):
        tk.Label(self.food_frame, text="Food Menu", font=("Arial", 16)).pack()
        for item in self.food_items:
            text = f"{item['name']} - ₹{item['price']}"
            btn = tk.Button(self.food_frame, text=text,
                            command=lambda i=item: self.add_to_cart(i))
            btn.pack(pady=2)

        self.cart_label = tk.Label(self.cart_frame, text="Cart: ", font=("Arial", 14))
        self.cart_label.pack()

        self.order_button = tk.Button(self.cart_frame, text="Place Order", command=self.place_order)
        self.order_button.pack(pady=10)

    def add_to_cart(self, item):
        self.cart.append(item)
        self.update_cart()

    def update_cart(self):
        cart_text = "Cart:\n" + "\n".join([f"{i['name']} - ₹{i['price']}" for i in self.cart])
        self.cart_label.config(text=cart_text)

    def place_order(self):
        if not self.cart:
            self.cart_label.config(text="Cart is empty!")
            return

        data = {
            "customer": {
                "name": "Test User",
                "address": "123 Example Street"
            },
            "items": self.cart
        }

        response = requests.post(f"{API_BASE}/order", json=data)
        if response.status_code == 201:
            self.cart = []
            self.update_cart()
            tk.messagebox.showinfo("Success", "Order placed successfully!")
        else:
            tk.messagebox.showerror("Error", "Failed to place order.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodDeliveryApp(root)
    root.mainloop()
