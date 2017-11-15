from flask import Flask, render_template, request
import urllib2, json, urllib
import requests

app = Flask(__name__)

@app.route('/')
def root():
    if request.args.get("text") is None:
        return render_template("form.html")
    username = "60365d33-5378-4194-8fb3-2a5f1b88deb0"
    password = "Idq1K6PcNKRs"
    apiurl = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    headers = {"content-type": "application/json", "Accept": "audio/wav" }
    dictionary = {"text": request.args.get("text")}
    r = requests.get( apiurl, auth=(username,password),
                      params=dictionary)
    #print r.content
    with open("static/resp.wav", "wb") as f:
        f.write(r.content)
        f.close()
    statuscode = r.ok
    print statuscode
    return render_template('template.html', text=request.args.get("text"),
                           r=statuscode)

if __name__ == '__main__':
    app.debug = True
    app.run()
