from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """ 
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Arial', sans-serif;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.2);
                padding: 20px 40px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
            }
            h1 {
                font-size: 2.5rem;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Live Demo </h1>
            <p>Hope you like it, and welcome fellow classmates! 😎</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
