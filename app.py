import os
from utils import tts
from flask import Flask, render_template, request

app = Flask(__name__)

def read_credentials(filename):
    try:
        f = open("credentials/" + filename, "r")
        creds = f.readlines()
        for i in range(0, len(creds)):
            creds[i] = creds[i].strip()
        return creds
    except Exception as e:
        print e
        print "============Credentials invalid=============="
        return [-1, -1]


@app.route("/")
def root():
    return "Hi there!"

@app.route("/test")
def test():
    creds = {}
    if request.args.get("text") is None:
        return render_template("test_form.html")
    creds['tts'] = read_credentials("text_to_speech")
    if creds['tts'][0] == -1:
        return render_template("bad_cred.html", api="Text to speech")
    print creds['tts']
    status = tts.text_to_speech(request.args["text"], creds['tts'][0], creds['tts'][1])
    print status
    return render_template("test.html", text=request.args["text"],
                           status=status)

if __name__ == "__main__":
    app.debug = True
    app.run()
