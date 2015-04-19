#!/usr/bin/python

import wolframalpha
import sys
import subprocess
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.record(source, 7)                        # extract audio data from the file

app_id='8K2J4H-RL4YVWRTG7'
client = wolframalpha.Client(app_id)

try:
    query = r.recognize(audio)
    print query
except LookupError:
    print("Could not understand audio")
    subprocess.call(["mplayer", "http://translate.google.com/translate_tts?tl=en&q=I do not understand"])

res = client.query(query)

if len(res.pods) > 0:
    texts = ""
    pod = res.pods[1]
    if pod.text:
        texts = pod.text
    else:
        texts = "I have no answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    print texts
    subprocess.call(["mplayer", "http://translate.google.co.uk/translate_tts?tl=en&q=%s" % (texts)])
else:
    print "Sorry, I am not sure."
    subprocess.call(["mplayer", "http://translate.google.com/translate_tts?tl=en&q=Sorry, I am not sure"])
