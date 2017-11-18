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
        return -1


@app.route("/")
def root():
    return "Hi there!"

@app.route("/test")
def test():
    if request.args.get("text") is None:
        return render_template("test_form.html")
    tts = read_credentials("text_to_speech")
    print tts
    status = tts.text_to_speech(request.args["text"], tts[0], tts[1])
    print status
    return render_template("test.html", text=request.args["text"],
                           status=status)

if __name__ == "__main__":
    app.debug = True
    app.run()
