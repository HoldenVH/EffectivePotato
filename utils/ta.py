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


def tagify_data(in_text, emotions):
    text = ""
    applied = []
    text += "<speak>"
    if "joy" in emotions:
        text += '<express-as type="GoodNews">'
        applied.append("joy")
    if "extraversion" in emotions:
        text += '<voice-transformation type="Custom" glottal_tension="+80%">'
        applied.append("extraversion")
    if "sadness" in emotions:
        text += '<express-as type="Apology">'
        applied.append("apology")
    if "tentative" in emotions:
        text += '<express-as type="Uncertainty">'
        applied.append("uncertainty")

    text += in_text

    if "tentative" in emotions:
        text += "</express-as>"
    if "sadness" in emotions:
        text += "</express-as>"
    if "extraversion" in emotions:
        text += '</voice-transformation>'
    if "joy" in emotions:
        text += "</express-as>"

    text += "</speak>"
    print "TEXT: ", text
    return [text, applied]

# 0: emotion_tone
#        0: Anger
#        1: Disgust
#        2: Fear
#        3: Joy
#        4: Sadness
#
# 1: writing_tone
#        0: Analytical
#        1: Confident
#        2: Tentative
#
# 2: social_tone
#        0: Openness
#        1: Conscientiousness
#        2: Extraversion
#        3: Agreeableness
#        4: Emotional Range
def listify_data(in_list):
    threshold = 0.33
    ret_list = []
    if in_list[0]['tones'][0]['score'] > threshold:
        ret_list.append("anger")
    if in_list[0]['tones'][1]['score'] > threshold:
        ret_list.append("disgust")
    if in_list[0]['tones'][2]['score'] > threshold:
        ret_list.append("fear")
    if in_list[0]['tones'][3]['score'] > threshold:
        ret_list.append("joy")
    if in_list[0]['tones'][4]['score'] > threshold:
        ret_list.append("sadness")
    if in_list[1]['tones'][0]['score'] > threshold:
        ret_list.append("analytical")
    if in_list[1]['tones'][1]['score'] > threshold:
        ret_list.append("confident")
    if in_list[1]['tones'][2]['score'] > threshold:
        ret_list.append("tentative")
    if in_list[2]['tones'][0]['score'] > threshold:
        ret_list.append("openness")
    if in_list[2]['tones'][1]['score'] > threshold:
        ret_list.append("conscientiousness")
    if in_list[2]['tones'][2]['score'] > threshold:
        ret_list.append("extraversion")
    if in_list[2]['tones'][3]['score'] > threshold:
        ret_list.append("agreeableness")
    return ret_list


def pretty_analysis(dictionary):
    #print dictionary
    string = '<table><tr><th>Emotion</th><th>Percent</th></tr>'
    for tone_cats in dictionary:
        for tone_cat in tone_cats['tones']:
            #print tone_cat
            string += '<tr><td>' + tone_cat['tone_name'] + '</td>' +\
                      '<td>' + str(round(tone_cat['score'] * 100, 2)) + '</td></tr>'
    string += '</table>'
    return string
