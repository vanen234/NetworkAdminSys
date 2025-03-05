from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello guys, this is my Network Administrations project!"

# Ensure the app runs on 0.0.0.0 to be accessible outside the container
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
