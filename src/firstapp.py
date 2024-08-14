from flask import Flask, request

from schema.authSchema import AuthSchema

app = Flask(__name__)


def query_all_tasks(clan_id):
    #Use ID to query tasks
    print(f"{clan_id} was here")
    return f"<p>here are tasks for clan {clan_id}</p>"


def validate(json):

    user = AuthSchema(json["key"], json["rsn"])

    print(user.key, user.rsn)

    return False


@app.route("/tasks/query", methods=["GET"])
def query():
    if request.is_json:
        val = validate(request.get_json())
        if val:
            return "tasks"
        else:
           return "false"
    else:
        return "not json"


with app.test_client() as client:
    req = client.get("/tasks/query", json={"key": "2313232", "rsn" : "doubt"})
