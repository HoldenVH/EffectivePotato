import os
import utils

def read_credentials(filename):
    try:
        f = open("credentials/" + filename, "r")
        creds = f.readlines()
        for i in range(0, len(creds)):
            creds[i] = creds[i].strip()
        return creds
    except:
        return -1

if __name__ == "__main__":
    tts = read_credentials("text_to_speech")
    print tts


