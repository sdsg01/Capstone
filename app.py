# print("Hello World")
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request)
        data = []   #empty dict to store data
        data = request.json['team1']
        print(data)

        # return jsonify(data)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)