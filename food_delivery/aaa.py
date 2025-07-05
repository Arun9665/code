
from flask import Flask
import webview
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Webview App!"

def start_flask():
    app.run()

if __name__ == '__main__':
    # Flask ko background thread mein run karo
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Webview window create karo
    webview.create_window("My App", "http://127.0.0.1:5000")
    webview.start()
