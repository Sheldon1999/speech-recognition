# this script is able to check connectivity of the device 
# according to that it uses Google services(if online)
# and CMU Sphinx (if offline)

import speech_recognition as sr
import os
from pocketsphinx import LiveSpeech, get_model_path
import socket

print("###welcome to the 🗣️ speech-recognition-command-line-utility🗣️ ###")
print("#Initiating speech recognition ...")
print("\nNow checking the internet connectivity of your device ...🤖️🤖️")

REMOTE_SERVER = "www.google.com"
isOnline = False
try:
	host = socket.gethostbyname(REMOTE_SERVER)
	s = socket.create_connection((host, 80), 2)
	s.close()
	print("Voilaa !! device found online.🤗️🤗️🤗️🤗️")
	print("here we are going to use 📢️ google-speech-recognition📢️ ,hence please make sure that internet speed is good enough to listen and change.")
	isOnline = True
except:
	print("Your Device is offline !!😑️😑️")
	print("here we are going to use CMU-Sphinx,its accuracy is not so good so please try to say a single word and wait for the response.")

#corpus to gather the sentences.
corpus = []

if isOnline == True :
	#device found online
	#using google speech recognition here
	print("\nenter [e] to say something and [s]to stop in your choice\n")
	while True :
		r = sr.Recognizer()
		while True :
			ch = input("\nYour Choice :")
			if ch.lower() == "s" or ch.lower() == "e" :
				break
			else :
				print("please enter the correct choice !")
		if ch.lower() == "s" :
			break
		with sr.Microphone() as source:
			print("\nSay")
			audio = r.listen(source)
		try:
			told = r.recognize_google(audio)
			print("you said : " + told)
			corpus.append(str(told))
		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

else :
	#device found offline
	#using pocketsphinx here
	speech = LiveSpeech(
		verbose=False,
		sampling_rate=16000,
		buffer_size=2048,
		no_search=False,
		full_utt=False,
		#added my model here.
		#you can also add your model here.
		#enter name of your model
		hmm='en-in',
		#enter name of lm file
		lm='en-in.lm.bin',
		#enter name of dict file
		dic='cmudict-en-in.dict'
	)
	print("\n Note: enter ctrl+c to stop listening.\n\n start saying something :")
	for phrase in speech:
		print(phrase)
		corpus.append(str(phrase))

print("\ndo you wish to print out the sentences you have spoken yet ?? ")
print("if YES -> enter[Y] below")
printAll = str(input("your choice : ")).upper()
if printAll == "Y" :
	i = 1
	for sen in corpus :
		print(i,"-> ",sen)
		i = i + 1