import json
import requests


def get_url(key, inp, cs=""):
    #info = json.loads(cs)
    #csstorage = cs
    #i = inp
    url = "http://www.cleverbot.com/getreply/"
    #url += "?key=" + key
    #url += "&input=" + i
    #if csstorage != "":
    #    url += "&cs=" + csstorage
    #url += "&callback=ProcessReply"
    if cs == "":
        dictionary = {"key": key, "input": inp}
    else:
        dictionary = {"key": key, "input": inp, "cs": cs}
    req = requests.get(url, params=dictionary)
    print req
    #par = {'key':key, 'input':i, 'cs':'csstorage','callback':'ProcessReply'}
    #print par
    #req = requests.get(url)
    #print req.url
    #rd = json.loads(req)
    #csstorage = rd['cs']
    #out = rd['output']
    #ret = {}
    #ret['url']=url
    #ret['cs']=csstorage
    #ret['output']=out
    #return ret

if __name__ == "__main__":
    f = open("../credentials/cleverbot", "r")
    key = f.readlines()[0]
    resp = get_url(key, "Hi")
    print resp
