import requests
import json


def analyze_tone(text, username, password):
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-18'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username, password),
                          headers=headers, data=data)
        return r.text
    except Exception as e:
        print e
        return False


def pretty_analysis(dictionary):
    print dictionary
    string = ""
    for tone_cats in dictionary['document_tone']['tone_categories']:
        string += "\n"
        string += tone_cats['category_id'] + ": "
        string += "\n"
        for tone_cat in tone_cats['tones']:
            for tone in tone_cat:
                string += "\t\t" + tone + ": "
                if isinstance(tone_cat[tone], unicode):
                    string +=  tone_cat[tone]
                else:
                    string += str(tone_cat[tone])
            string += "\n"
    return string
