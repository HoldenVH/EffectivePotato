from flask import Flask, render_template, request
import urllib2, json, urllib
import requests
import shutil

app = Flask(__name__)

@app.route('/')
def root():
    if request.args.get("text") is None:
        return render_template("form.html")
    username = "60365d33-5378-4194-8fb3-2a5f1b88deb0"
    password = "Idq1K6PcNKRs"
    apiurl = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    headers = {"content-type": "application/json", "Accept": "audio/wav", "content-disposition": "attachment; filename=\"resp.wav\""}
    dictionary = {"text": request.args.get("text")}
    r = requests.get( apiurl, auth=(username,password), stream=True,
                      params=dictionary)
    with open('audio.wav', 'wb') as f:
        f.write(r.content)
    #print r.content
    #filename = "static/resp.wav"
    #with open(filename, "wb") as f:
    #    f.write(r.content)
    #    f.close()

    statuscode = r.ok
    print statuscode
    return render_template('template.html', text=request.args.get("text"),
                           r=statuscode)

if __name__ == '__main__':
    app.debug = True
    app.run()
