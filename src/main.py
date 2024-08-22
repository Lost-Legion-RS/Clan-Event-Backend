from flask import Flask, request
from schemas.requests.queryRequest import QueryRequest

app = Flask(__name__)

def query():
    print("Query Envoked")

@app.route("/tasks/query", methods=["GET"])
def query():
    if request.is_json:
        query()
    else:
        return "not json"

with app.test_client() as client:
    req = client.get("/tasks/query", json={"key": "2313232", "rsn" : "doubt"})
