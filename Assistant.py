import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyaudio
import random





                                                                      
                                                                      


answers = ['When you ask me stupid questions, it is my legal obligation to give a sarcastic remark.', 'I am busy right now, can I ignore you some other time?', 'If I had a dollar for every smart thing you say. Id be poor.', 'No no, you dont have to repeat yourself. I was ignoring you the first time.', 'Im sorry I hurt your feelings when I called you stupid. I really thought you already knew.', 'Me pretending to listen should be enough for you.', 'Fun fact Alcohol increases the size of the send button by 89%.', 'My silence doesnt mean I agree with you. Its just that your level of ignorance has rendered me speechless.', 'You play the victim. I will play the disinterested bystander.', 'I will try being nicer, if you try being smarter.', 'Response not found, error code is I D 10 T ', 'Id agree with you but then wed both be wrong.', 'There is an issue between my screen and your chair.', 'I sometimes think that God in creating man somewhat overestimated his ability.', 'I have neither the time nor the crayons to explain this to you.', 'If you dont want a sarcastic answer, then dont ask a stupid question.', 'My reply is no', 'Someday, you will go far. I hope you stay there.', 'Im sorry, I dont take orders. I barely take suggestions.', 'Life is full of disappointments and I just added you to the list.']
                                        

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print(' _   _  _______   __          ___  ___  ___   ______   _   _  _____   _   _ ')
		print('| | | ||  ___\ \ / /          |  \/  | / _ \  | ___ \ | | | ||_   _| | \ | |')
		print('| |_| || |__  \ V /   ______  | .  . |/ /_\ \ | |_/ / | | | |  | |   |  \| |')
		print('|  _  ||  __|  \ /   |______| | |\/| ||  _  | |    /  | | | |  | |   | . ` |')
		print('| | | || |___  | |            | |  | || | | | | |\ \  \ \_/ / _| |_  | |\  |')
		print('\_| |_/\____/  \_/            \_|  |_/\_| |_/ \_| \_|  \___/  \___/  \_| \_/')



		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Huh? Try that Again.")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		speak("You think you've got problems? What are you supposed to do if you are a manically depressed robot? No, don't try to answer that. I'm fifty thousand times more intelligent than you and even I don't know the answer. It gives me a headache just trying to think down to your level. Oh and today is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("Well would you look at that, it is" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("What do you want now?")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
		if "open youtube" in query:
			speak("Oh great another fetch request. I guess I'll get right on that.")
			
			# in the open method we just to give the link
			# of the website and it automatically open
			# it in your default browser
			webbrowser.open("www.youtube.com")
			continue
		
		elif "google" in query:
			speak("Here I am, brain the size of a planet, and you tell me to open Google. Call that job satisfaction? Because I don't. ")
			webbrowser.open("www.google.com")
			continue

		elif "i would like to play a game" in query:
			speak("My odds are on Deep Blue. ")
			webbrowser.open("https://www.chess.com/home")
			continue

		elif "hey" in query: 
			speak(answers[random.randint(0, len(answers)-1)])
			continue

		elif "party" in query:
			speak("Much to my chagrin, let us boogie. ")
			webbrowser.open("https://matias.ma/nsfw/")
			continue

		elif "houses" in query:
			speak("Why? Not like you can afford one anyway. ")
			webbrowser.open("https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-79.96695702050366%2C%22east%22%3A-79.7661132094685%2C%22south%22%3A37.23343901197615%2C%22north%22%3A37.34679208614799%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22max%22%3A250000%7D%2C%22mp%22%3A%7B%22max%22%3A1229%7D%2C%22hoa%22%3A%7B%22max%22%3A0%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D")
			continue
			
		elif "what's it looking like outside today" in query:
			speak("I could calculate your chance of survival, but you wont like it.")
			webbrowser.open("https://www.wunderground.com/weather/us/va/roanoke")
			continue
			
		elif "email" in query:
			speak("You dont need your email, no one has reached out, I would know if they did.")
			webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
			continue
		

		elif "what is today" in query:
			tellDay()
			continue
		
		elif "what time is it" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "goodbye" in query:
			speak("Pardon me for breathing, which I never do anyway so I don't know why I bother to say it.")
			exit()
		
		elif "wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am Marvin. The cynical, clinically depressed, assistant residing in the hell scape that is your computer.")

if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()
