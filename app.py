
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/predict",methods=["POST"])
def predict():
    print(request.json)
    return {"info":"Done."}

@app.route("/api/get-result")
def predict():
    print(request.json)
    return {"info":"Done."}

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 5000
    app.run(HOST,PORT,debug=True)

