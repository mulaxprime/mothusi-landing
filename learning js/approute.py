from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route("/hello")
def hello_page():
    return "Hello page!"

@app.route("/data")
def data():
    return jsonify({"name": "Mmoni", "status": "Learning Flask"})

@app.route("/greet", methods=['GET', 'POST'])
def greet():
    if request.method == "POST":
        return "You sent a POST request!"
    else:
        return "You sent a GET request! "

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)