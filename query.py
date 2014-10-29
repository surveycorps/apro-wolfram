#!/usr/bin/python

import wolframalpha
import sys
import subprocess
import speech_recognition as sr

class Query(self):
    def __init__(self):
	self.r = sr.Recognizer()

	app_id='8K2J4H-RL4YVWRTG7'
	self.client = wolframalpha.Client(app_id)

    def hear(self):
        with sr.Microphone() as source:
	    # extract audio data from the fil
	    audio = self.r.record(source, 7) 
	try:
	    query = self.r.recognize(audio)
	    return query
	except LookupError:
	    print("Could not understand audio")
	    subprocess.call(["mplayer", "http://translate.google.com/translate_tts?tl=en&q=I do not understand"])

    def answer(self, query):
	res = self.client.query(query)

	if len(res.pods) > 0:
	    texts = ""
	    pod = res.pods[1]
	    if pod.text:
		texts = pod.text
	    else:
		texts = "I have no answer for that"
	    # to skip ascii character in case of error
	    texts = texts.encode('ascii', 'ignore')
	    subprocess.call(["mplayer", "http://translate.google.co.uk/translate_tts?tl=en&q=%s" % (texts)])
	    return texts
	else:
	    print "Sorry, I am not sure."
	    subprocess.call(["mplayer", "http://translate.google.com/translate_tts?tl=en&q=Sorry, I am not sure"])
