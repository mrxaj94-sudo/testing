from flask import Flask , jsonify , request


app = Flask(__name__)

@app.route("/")

def home():
    return "CI/CD Pipeline Working"

@app.route("/predict", methods=["POST"])

def predict():
    data = request.get_json()

    a =  data.get("a")
    b =  data.get("b")

    result =  a + b

    return jsonify({"Result" : result})


if __name__ == "__main__":
    app.run(debug=True)