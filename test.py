import flask
import exampleFunctions as ex
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Dictionary for examples of sending and recieving data
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

#Basic get route
@app.route('/', methods=['GET'])
def home():
    return "test"

#######################


#Another basic get route
@app.route('/foodTinder/getMembers', methods=['GET'])
def get_members():
    #must convert dictionary to json format
    return jsonify(members)

#########################

#Get route with a parameter
#args are defined after the url following ?, seperated by &
#to access request.args[ID_OF_VAR]
@app.route('/foodTinder/getMember', methods=['GET'])
def get_member():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        ex.fail()
        return "Error: No id field provided, please specify an ID", 400
    
    results = []

    for member in members:
        if member['id'] == id:
            results.append(member)
    ex.success()
    return jsonify(results)

##############################

#Get route with variable rules
#Different way to pass arguments in get request, to pass in ur just do /VALUE
@app.route('/foodTinder/getName/<int:member_id>')
def get_name(member_id):
    result = ""
    for member in members:
        if member['id'] == member_id:
            result = member['name']
    ex.success()
    return jsonify(result)


#Post route with body data from requester
#When using the request object, need to create a new request object and bind it to that routes context
@app.route('/foodTinder/addMember', methods=['POST'])
def add_member():
    #First retrieve form data this way, converts it to a dictionary
    #Flask by default stores as ImmutableDict, converting makes manipulating the data easier
    reqData = request.form.to_dict()

    members.append(reqData)
    
    ex.success()
    return jsonify(members)


#Same post route, now checks if the id is there
@app.route('/foodTinder/addUniqueMember', methods=['POST'])
def add_unique_member():
    reqData = request.form.to_dict()

    for member in members:
        if(reqData['id'] == member['id']):
            return "User with that ID already exists", 500
    
    members.append(reqData)
    ex.print_formatted(members)
    ex.success()
    return jsonify(members)

#Removes a member, deals with POST parameters
@app.route('/foodTinder/removeMember', methods=['POST'])
def delete_member():
    delID = int(request.form['id'])
    delet = False
    for member in members:
        if member['id'] == delID:
            delet = member

    if delet != False:
        members.remove(delet)
    else:
        ex.fail()
        return "No user found with that id", 404
    ex.success()
    return jsonify(delet)
app.run()