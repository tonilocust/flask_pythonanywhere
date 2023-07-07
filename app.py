from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])

def git_update():
    repo = git.Repo('./flask_pythonanywhere')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

def home_page():
    message="Welcome to the Home Page"
    response={"message":message}
    return jsonify({"response":response}), 200

if __name__ == '__main__':
    app.run()

