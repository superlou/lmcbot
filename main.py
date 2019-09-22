#!/usr/bin/python3
from flask import Flask, request, jsonify
from lmctv import determine_watch_method
import os.path
from datetime import datetime
import csv


app = Flask(__name__)
log_filename = 'log.csv'


@app.route('/')
def index():
    return 'Index'


def log(filename, dialogue_sid, user, msg, channel, source):
    fields = ['timestamp', 'dialogue_sid', 'user', 'msg', 'channel', 'source']

    if not os.path.exists(filename):
        with open(filename, 'w') as log_file:
            writer = csv.writer

    with open(filename, 'a') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([datetime.now(), dialogue_sid, user, msg, channel, source])


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

    log(log_filename, dialogue_sid, user, msg, channel, source)

    response = {
        'actions': [
            {'say': say},
            {'listen': listen}
        ]
    }
    return jsonify(response)
