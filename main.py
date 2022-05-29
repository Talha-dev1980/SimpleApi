from flask import Flask, json, jsonify, request
from test import chatbot_response
import ast
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello! this is Psychiatric chat</p>"

# @app.route("/age")
# def age():
#     return "<p>Hello! my age is 5 years</p>"

# @app.route("/name")
# def name():
#     return "<p>Hello! my name is Psychiatric chat</p>"


@app.route("/<string:s>")
def called(s):
    if s=="age":
        r="my age is 5 years"
    elif s=="name":
        r="my name is Talha's bot"
    elif s=="who":
        r="I am bot"
    else:
        r="Sorry i can only recognize (age,name,who)"
    result = {
        "user": s,
        "server": r
    }
    return jsonify(result)


@app.route('/', methods=['GET', 'POST'])
def returnChatbotResponse():
    if request.method == 'POST':
        userQuery = (request.args.get('user'))
        print('############')
        print(userQuery)
        print('############')
        print('type= ', type(userQuery))
        result = {
            "user": userQuery,
            "server": "Hi i am response"
        }
        return jsonify(result)
    else:
        return "<p>Please use proper API POST request call for chatbot response</p>"


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
