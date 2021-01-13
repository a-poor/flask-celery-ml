
from flask import Flask, render_template, request

from celery.result import AsyncResult
from predict import papp
from predict import predict as cpredict

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/predict",methods=["POST"])
def predict():
    print(request.json)
    data = request.json.get("input-data")
    task = cpredict.delay(data)
    return {"status":"working","result-id":task.id}

@app.route("/api/get-result")
@app.route("/api/get-result/<taskid>")
def get_result(taskid: str = None):
    if taskid is None:
        return {"status":"error",
            "message":"No taskid supplied"}
    try:
        task = AsyncResult(taskid,app=papp)
    except Exception as e:
        return {"status":"error","error":str(e)}
    if task.state != "SUCCESS":
        return {"status":task.state}
    return {"status":task.state,"result":task.get()}


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 5000
    app.run(HOST,PORT,debug=True)

