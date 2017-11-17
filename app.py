import os
from utils import text_to_speech

def read_credentials(filename):
    try:
        f = open("credentials/" + filename, "r")
        creds = f.readlines()
        for i in range(0, len(creds)):
            creds[i] = creds[i].strip()
        return creds
    except Exception as e:
        print e
        return -1


if __name__ == "__main__":
    tts = read_credentials("text_to_speech")
    print tts
    status = text_to_speech.text_to_speech("hello jeffrey", tts[0], tts[1])
    print status

