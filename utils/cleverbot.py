import json
import requests

def get_url(k, inp, d=""):
    #info = json.loads(d)
    csstorage = d
    i = inp
    url = "http://www.cleverbot.com/getreply"
    url += "?key=" + k
    url += "&input=" + i
    if csstorage != "":
        url += "&cs=" + csstorage
    url += "&callback=ProcessReply"
    #req = requests.request(url)
    req = '''
    {"cs":"MXYxCTh2MQlBdldYQ0JLNkJCNU4JMUZ2MTUxMTE1NTgzOQk2NGlOby4J","interaction_count":"1","input":"","input_label":"","predicted_input":"","accuracy":"","output_label":"welcome","output":"No.","conversation_id":"WXCBK6BB5N","errorline":"Init:3737,Full:3733,Other:479,Row:18,Score:57,Id:260069711,Len:3,","database_version":"3167","software_version":"3233","time_taken":"32","random_number":"198","time_second":"39","time_minute":"30","time_hour":"5","time_day_of_week":"0","time_day":"20","time_month":"11","time_year":"2017","reaction":"","reaction_tone":"","emotion":"","emotion_tone":"","clever_accuracy":"0","clever_output":"No.","clever_match":"","CSRES30":"","time_elapsed":"0","filtered_input":"","reaction_degree":"","emotion_degree":"","reaction_values":"","emotion_values":"","callback":"","interaction_1":"","interaction_1_other":"No.","interaction_2":"","interaction_3":"","interaction_4":"","interaction_5":"","interaction_6":"","interaction_7":"","interaction_8":"","interaction_9":"","interaction_10":"","interaction_11":"","interaction_12":"","interaction_13":"","interaction_14":"","interaction_15":"","interaction_16":"","interaction_17":"","interaction_18":"","interaction_19":"","interaction_20":"","interaction_21":"","interaction_22":"","interaction_23":"","interaction_24":"","interaction_25":"","interaction_26":"","interaction_27":"","interaction_28":"","interaction_29":"","interaction_30":"","interaction_31":"","interaction_32":"","interaction_33":"","interaction_34":"","interaction_35":"","interaction_36":"","interaction_37":"","interaction_38":"","interaction_39":"","interaction_40":"","interaction_41":"","interaction_42":"","interaction_43":"","interaction_44":"","interaction_45":"","interaction_46":"","interaction_47":"","interaction_48":"","interaction_49":"","interaction_50":""}
    '''
    #par = {'key':k, 'input':i, 'cs':'csstorage','callback':'ProcessReply'}
    #print par
    #req = requests.get(url)
    #print req.url
    rd = json.loads(req)
    csstorage = rd['cs']
    out = rd['output']
    ret = {}
    ret['url']=url
    ret['cs']=csstorage
    ret['output']=out
    return ret
