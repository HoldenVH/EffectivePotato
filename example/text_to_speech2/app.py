from flask import Flask, render_template, request
import urllib2, json, urllib
import requests
import shutil
import os

app = Flask(__name__)

@app.route('/')
def root():
    if request.args.get("text") is None:
        return render_template("form.html")
    username = "3f174c47-4e0a-483c-9526-20c5afe6a303"
    password = "lkfmA6YYNBzP"
    apiurl = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    headers = {"content-type": "application/json", "Accept": "audio/wav",
               "Content-Disposition": "attachment;filename=audio.wav"}
    dictionary = {"text": request.args.get("text")}
    r = requests.get( apiurl, auth=(username,password), stream=True,
                      params=dictionary)
    try:
        os.remove("static/audio.wav")
        print "Deleted file"
    except:
        print "File doesn't exist"
    filename = "static/audio.wav"
    with open(filename, 'wb') as f:
        f.write(r.content)
    #print r.content
    #filename = "static/resp.wav"
    #with open(filename, "wb") as f:
    #    f.write(r.content)
    #    f.close()

    return render_template('template.html', text=request.args.get("text"),
                           status=r.ok)

if __name__ == '__main__':
    app.debug = True
    app.run()
