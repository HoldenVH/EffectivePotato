# Team EffectivePotato -- Holden Higgins, Vivien Lee, Shaina Peters, Arif Roktim 
Far better than an ineffective potato

## Overview
APIs used: Cleverbot, IBM Watson text to speech, IBM Watson tone analyzer

The user inputs what they want to say to Cleverbot through the chatbox, and Cleverbot will return a response to what the user wrote. Cleverbot’s response will then be passed into the Watson text-to-speech API, ultimately allowing the user to download an audio file of Cleverbot’s response in spoken format, as well as see the response's emotion/tone breakdown data.


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
In the root of the EffectivePotato repo run:
```bash
$ git clone git@github.com:ArifRoktim/credentials.git
```

###For non-members of Team EffectivePotato
In the root of the EffectivePotato repo create a file named "credentials"
Then do the following to procure API keys

### Text to Speech API & Tone Analyzer API
Text to Speech and Tone Analyzer are both IBM Watson APIs

Credentials for Watson are availible at https://console.bluemix.net/developer/watson/services

-to get started select "Text to Speech" and "Tone Analyzer"

-click "Add Services"

-either log in or create an account for IBM cloud

-verify your email address

-go back to https://console.bluemix.net/developer/watson/existing-services

-under "Projects" select your projects

-where it says "Credentials" click "Show"

-Create file `text_to_speech`. Add the username to the first line and the password to the second line.

-Create file `tone_analyzer`. Add the username to the first line and the password to the second line.

### Cleverbot API
Cleverbot credentials are availible at https://www.cleverbot.com/api/

-to get started, go to "Prices and sign up", and choose the free trial

-add the item to your cart

-you will be prompted to create an account

-enter your information and click  "Place order"

-go to the email account you gave and verify your email

-you will now be able to go back to the cleverbot page and find your credentials under "My account"

-Create file `cleverbot`. Add the API key to the first line.
