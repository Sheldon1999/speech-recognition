# this script is able to check connectivity of the device 
# according to that it uses Google services(if online)
# and CMU Sphinx (if offline)
import speech_recognition as sr
print("###welcome to the 🗣️ speech-recognition-command-line-utility🗣️ .###\nChoose one of the following option to proceed :")
print("->enter[1] to test speech recognition")
print("->enter[2] to see tutorial")
print("->enter[3] to see about-us ")
while True :
	choice = input("Your Choice :")
	if choice == "1" or choice == "2" or choice == "3" :
		break
	else :
		print("please enter the correct choice !")
if choice == "1" :
	print("You have choosen speech recognition.\n#Initiating speech recognition ...")
	print("Now checking the internet connectivity of your device ...🤖️🤖️")
	import socket
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
	r = sr.Recognizer()
	corpus = []
	if isOnline == True :
		while True :
			with sr.Microphone() as source:
				print("Say")
				audio = r.listen(source)
			try:
			    # for testing purposes, we're just using the default API key
			    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			    # instead of `r.recognize_google(audio)`
				told = r.recognize_google(audio)
				print("you said : " + told)
				corpus.append(str(told))
			except sr.UnknownValueError:
				print("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Google Speech Recognition service; {0}".format(e))

	else :
		while True :
			with sr.Microphone() as source:
				print("something!")
				audio = r.listen(source)
			try:
				told = r.recognize_sphinx(audio)
				print("you said : " + told)
				corpus.append(str(told))
			except sr.UnknownValueError:
				print("Sphinx could not understand audio")
			except sr.RequestError as e:
				print("Sphinx error; {0}".format(e))
	print("do you wish to print out the sentences you have spoken yet ?? ")
	print("if YES -> enter[Y] below")
	printAll = str(input("your choice : ")).upper()
	if printAll == "Y" :
		i = 0
		for sen in corpus :
			print(i,"-> ",sen)
			i = i + 1
