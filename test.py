import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

members = [
    {
        'id': 0,
        'name': "Oliver Logush",
        'role': "manager"
    },
    {
        'id': 1,
        'name': "Noah Wilder",
        'role': "subteam manager"
    },
    {
        'id': 2,
        'name': "Joshua Mac",
        'role': "team member"
    },
    {
        'id': 3,
        'name': "Luna Zhou",
        'role': "team member"
    },
    {
        'id': 4,
        'name': "Etan Ossip",
        'role': "team member"
    }
]

@app.route('/', methods=['GET'])
def home():
    return "test"

@app.route('/foodTinder/getMembers', methods=['GET'])
def get_members():
    #must convert dictionary to json format
    return jsonify(members)

@app.route('/foodTinder/getMember', methods=['GET'])
def get_member():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided, please specify an ID"
    
    results = []

    for member in members:
        if member['id'] == id:
            results.append(member)

    return jsonify(results)

@app.route('/foodTinder/getName/<int:member_id>')
def get_name(member_id):
    result = members['']

app.run()

