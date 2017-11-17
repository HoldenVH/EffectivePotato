import requests
import os


def text_to_speech(text, username, password):
    apiurl = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"
    headers = {"content-type": "application/json", "Accept": "audio/wav",
               "Content-Disposition": "attachment;filename=audio.wav"}
    dictionary = {"text": text}
    r = requests.get(apiurl, auth=(username, password), stream=True,
                     params=dictionary)
    filename = "static/audio.wav"
    try:
        os.remove(filename)
        if __name__ == "__main__":
            print "Deleted file"
    except:
        if __name__ == "__main__":
            print "File doesn't exist"
    with open(filename, 'wb') as f:
        f.write(r.content)
    if __name__ == "__main__":
        print r
    return r.ok
