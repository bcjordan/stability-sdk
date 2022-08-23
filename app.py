from flask import Flask, send_file
import subprocess
import re

app = Flask(__name__)


from subprocess import PIPE, Popen


@app.route('/')
def hello_world():
    command = 'python3 src/stability_sdk/client.py -W 512 -H 512 "An adorable happy puppy dog."'
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        output = process.communicate()[0].decode("utf-8")
        # return output
        result = re.search('to (.*\.png)', output, re.I | re.U).group(1)
        # return result
        return send_file(result, mimetype='image/png')
        # return send_file('src/stability_sdk/' + result, mimetype='image/png')
