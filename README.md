# Team EffectivePotato -- Holden Higgins, Vivien Lee, Shaina Peters, Arif Roktim 
Far better than an ineffective potato

## Overview
APIs used: Cleverbot, IBM Watson text to speech, IBM Watson tone analyzer

The user inputs what they want to say to Cleverbot, and Cleverbot will return a response to what the user wrote. Cleverbot’s response will then be passed into the Watson text-to-speech API, ultimately allowing the user to download an audio file of Cleverbot’s response in spoken format.


## Dependencies
You need the requests library  
First make a virtual environment and activate it. Then install the requests library.  
```bash
$ virtualenv venv
$ . venv/bin/activate
$ pip install requests
```

## Credentials
### For members of Team EffectivePotato:
In the root of the repo run:
```bash
$ git clone git@github.com:ArifRoktim/credentials.git
```


### Text to Speech API
__Insert api key procuring instructions__  
Create file `text_to_speech`. Add the username to the first line and the password to the second line.

### Tone Analyzer API
__Insert api key procuring instructions__  
Create file `tone_analyzer`. Add the username to the first line and the password to the second line.

### Cleverbot API
__Insert api key procuring instructions__  
Create file `cleverbot`. Add the API key to the first line.
