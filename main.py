#!/usr/bin/python3
from flask import Flask, request, jsonify
from lmctv import determine_watch_method


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/api/v1/tasks/what_watching', methods=['POST'])
def what_watching():
    dialogue_sid = request.form.get('DialogueSid')
    task = request.form.get('CurrentTask')
    msg = request.form.get('CurrentInput')
    user = request.form.get('UserIdentifier')

    source, channel = determine_watch_method(msg)

    listen = (source is None) or (channel is None)

    if source is None:
        say = "Sorry, I didn't understand that. Who's your cable provider? Online? Roku?"
    else:
        say = "Thanks for watching!"

    response = {
        'actions': [
            {'say': say},
            {'listen': listen}
        ]
    }
    return jsonify(response)
