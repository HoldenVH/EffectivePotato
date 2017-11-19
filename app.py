import os
import json
from utils import tts, ta
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
    if request.args.get("text") is None:
        return render_template("test_form.html")
    # ========Read credentials========
    creds = {}
    creds['tts'] = read_credentials("text_to_speech")
    creds['ta'] = read_credentials("tone_analyzer")

    # Check if creds exist
    for cred in creds:
        if creds[cred][0] == -1:
            return render_template("bad_cred.html", api="Text to speech")
    # ========End reading credentials========

    tts_status = tts.text_to_speech(request.args["text"], creds['tts'][0], creds['tts'][1])
    print tts_status
    ta_resp = ta.analyze_tone(request.args["text"], creds['ta'][0], creds['ta'][1])
    ta_dict = json.loads(ta_resp)
    ta_ret = ta.pretty_analysis(ta_dict)
    return render_template("test.html", text=request.args["text"],
                           tts_status=tts_status,
                           ta_status=ta_resp, ta_ret=ta_ret)

if __name__ == "__main__":
    app.debug = True
    app.run()
