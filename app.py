# print("Hello World")
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Fantasy Cricket 3SM'

if __name__ == "__main__":
    app.run(debug=True)