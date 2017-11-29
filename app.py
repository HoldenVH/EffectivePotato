import os
import json
from utils import tts, ta, cleverbot
from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)

#cs is the variable that logs your old inputs
#it needs to be stored somewhere
csstorage = ""

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


@app.route("/tone")
def test():
    if request.args.get("text") is None:
        return render_template("test_form.html")
    # ========Read credentials========
    creds = {}
    creds['tts'] = read_credentials("text_to_speech")
    creds['ta'] = read_credentials("tone_analyzer")

    # Check if creds exist
    if creds['ta'][0] == -1:
        return render_template("bad_cred.html", api="Tone analyzer", fname="tone_analyzer")
    if creds['tts'][0] == -1:
        return render_template("bad_cred.html", api="Text to speech", fname="text_to_speech")
    #for cred in creds:
    #    if creds[cred][0] == -1:
    #
    # ========End reading credentials========

    # ========Tone analyzing========
    ta_resp = ta.analyze_tone(request.args["text"], creds['ta'][0], creds['ta'][1])
    ta_dict = json.loads(ta_resp)['document_tone']['tone_categories']
    ta_ret = ta.pretty_analysis(ta_dict)
    #print ta_dict
    emotions = ta.listify_data(ta_dict)
    print "Emotions: ", emotions
    ta_taggified_data = ta.tagify_data(request.args["text"], emotions)
    ta_in = ta_taggified_data[0]
    ta_applied_tags = ta_taggified_data[1]

    # ==== Text to speech ====
    tts_status = tts.text_to_speech(ta_in, creds['tts'][0], creds['tts'][1])
    print "TTS Status: ", tts_status

    return render_template("test.html", text=request.args["text"],
                           tts_status=tts_status,
                           ta_status=ta_resp, ta_ret=ta_ret, ta_in=ta_in,
                           ta_applied_tags=ta_applied_tags)

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/clever', methods=["POST"])
def clever():
    global csstorage
    inp = request.form['input']
    cred = read_credentials('cleverbot')[0]
    if cred == -1:
        return render_template("bad_cred.html", api="cleverbot", fname="cleverbot")
    #cs = "needs to be implemented"
    if request.method == "GET":
        return cred
    if request.method == "POST":
        processed = cleverbot.get_url(cred, inp, csstorage)
        if processed == -1:
            return "Ooops! Cleverbot api is not available!"
        csstorage = processed['cs']
        to_display = cleverbot.create_message(processed['output'])
        return to_display

    cred = read_credentials('cleverbot')[0]
    get_url(key)
    return cred

if __name__ == "__main__":
    app.debug = True
    app.run()
