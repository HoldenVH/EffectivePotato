import json
import requests
import urllib


def get_url(key, inp, cs=""):
    url = "http://www.cleverbot.com/getreply"
    if cs == "":
        dictionary = {"key": key, "input": inp}
    else:
        dictionary = {"key": key, "input": inp, "cs": cs}
    req = requests.get(url, params=dictionary)
    print req
    if not req.ok:
        return -1
    print req.text
    req = req.text
    rd = json.loads(req)
    csstorage = rd['cs']
    out = rd['output']
    ret = {}
    ret['url']=url
    ret['cs']=csstorage
    ret['output']=out
    return ret

if __name__ == "__main__":
    f = open("../credentials/cleverbot", "r")
    key = f.readlines()[0].strip()
    resp = get_url(key, "Hi")
    print resp

def create_message(text):
    href = "/tone?text="
    href += urllib.quote_plus(text)
    message = "<a href=\""+href+"\" target=\"_blank\">"+text+"</a>"
    print message
    return message
