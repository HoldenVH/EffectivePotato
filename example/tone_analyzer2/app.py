from flask import Flask, render_template, redirect, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def root():
    #return render_template("template.html")
    print request.args
    if request.args.get("text") is None:
        return render_template("form.html")
    analysis = analyze_tone(request.args.get('text'))
    analysis = json.loads(analysis)
    return render_template("template.html",
                           text=request.args.get('text'), analysis=pretty_analysis(analysis))

def analyze_tone(text):
    username = '1a7f0e39-4e81-40e1-af64-d81da8be70be'
    password = 'zkk7Kyynyo5D'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username, password), headers=headers,
                          data=data)
        return r.text
    except:
        return False

def pretty_analysis(dict):
    str = ""
    for tone_cat in dict['document_tone']['tone_categories']:
        str += "\n"
        str += tone_cat['category_id'] + ": "
        str += "\n"
        for tone in tone_cat['tones']:
            str += json.dumps(tone)
    return str

if __name__=="__main__":
    app.debug = True;
    app.run()
