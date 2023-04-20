import speech_recognition as sr
import socket
import subprocess
import emoji
import os
import sys
import getpass
import webbrowser
import pyttsx3
engine = pyttsx3.init()
from twilio.rest import Client  ########################Capstone##Nepal###@
import random
import screen_brightness_control as sbc
import requests	
import string
import easygui
import openai
import pyautogui
import wolframalpha
ip = socket.gethostname() 

def chrome():
    subprocess.run(["xdg-open", "https://www.google.com"])	
    subprocess.run(["espeak", "Opening chrome"])
    subprocess.run(["espeak", "-v", "es", "Abriendo chrome"])

def facebook():
    subprocess.run(["xdg-open", "https://www.facebook.com"])	
    subprocess.run(["espeak", "Opening Facebook"])
def youtube():
    subprocess.run(["xdg-open", "https://www.youtube.com"])	
    subprocess.run(["espeak", "Opening youtube"])

def message ():
    engine.say("sending message now Please enter the following information.")
    engine.runAndWait()
    account_sid = 'AC782e8d5ce357d38b0988123479991591'
    auth_token = '0c395bd005a0fb5809b4d96bb3243649'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= easygui.enterbox("Please enter your message"),
    from_='+13855265358',
    to = easygui.enterbox("Please enter your phone number", default='+1'),
    )
    engine.say("sending message")
    engine.runAndWait()
    print(message.sid)    

def email():
    engine.say("sending email now. Please enter the following information")
    engine.runAndWait()
    recipient = easygui.enterbox("Enter receiver email address: ")
    subject = easygui.enterbox ("Enter subject:")
    body = easygui.enterbox("Enter message: ")

    os.system('xdg-open "mailto:' + recipient + '?subject=' + subject + '&body=' + body + '"')
def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the math book look so mad? Because it had too many problems!",
        "Why did the cookie go to the doctor? Because it was feeling crumbly!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the frog call his insurance company? He had a jump in his car!",
        "Why did the hipster burn his tongue? He drank his coffee before it was cool!",
        "Why did the elephant wear red sneakers? To hide in cherry trees!",
        "Why did the chicken cross the playground? To get to the other slide!"
        "What do you get when you cross a tyrannosaurus rex with fireworks? Dino-mite!"
        "Two goldfish are in a tank. One turns to the other and says, Do you know how to drive this thing?"
        "Why did the banana go to the doctor? Because it wasn't peeling very well!",
        "Why was the math book sad? Because it had too many problems!",
        "Why did the ghost go on a diet? Because he was feeling a little transparent!",
        "Why did the lifeguard save the banana? Because it was in a split!",
        "Why did the dinosaur cross the road? To get to the other side!",
        "Why did the scientist install a knocker on his door? He wanted to win the No-bell prize!",
        "Why did the tree go to the dentist? Because it needed a root canal!",
        "Why did the bear go to the doctor? Because it was a-polar!",
        "Why was the math book so popular? Because it had lots of problems!",
        "Why did the book go to the doctor? Because it had a bad case of the pages!",
        "Why did the snake go to the doctor? Because it needed a hiss-terectomy!",
        "Why did the car go to the doctor? Because it had a flat tire!",
        "Why did the horse go to the doctor? Because it had a little bit of a runny nose!",
        "Why did the squirrel go to the doctor? Because it was feeling a little nutty!",
        "Why did the duck go to the doctor? Because it had a bad case of the quacks!",
        "Why did the moon go to the doctor? Because it had a case of the lunar-tics!",
    ]
    joke = random.choice(jokes)
    print(joke)
    engine.say(joke)
    engine.say("Hahaha")
    engine.runAndWait()

def screen_brightness():
    engine.say("Please enter the value to adjust the brightness in numbers")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        size = int(r.recognize_google(audio))
        sbc.set_brightness(size)
        print(sbc.get_brightness())

def add_user():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols
    length=12
    pwd = random.sample(chars,length)
    passd= ''.join((pwd))
    print(passd)
     # Ask for the input
    username = input("Enter Username ")  
 
     # Asking for users password
    password = passd
        
    try:
         # executing useradd command using subprocess module
       subprocess.run(['useradd', '-p', password, username ])     
    except:
       print(f"Failed to add user.")                    
       sys.exit(1)
#https://www.geeksforgeeks.org/add-a-user-in-linux-using-python-script/


def calls():
    account_sid = 'AC782e8d5ce357d38b0988123479991591'
    auth_token = '0c395bd005a0fb5809b4d96bb3243649'
    client = Client(account_sid, auth_token)
    if "roshan" in command:
        engine.say("Calling roshan")
        call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_='+13855265358',
                        to='+14038278378',
                    )
        print(call.sid)
    elif "samip" in command:
        engine.say("Calling samip")
        call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        from_='+13855265358',
                        to='+14034023270',
                        
                    )
        print(call.sid)
def scan_ports():
    ip = socket.gethostname() 
    host = socket.gethostbyname(ip)
    print(host)
    ports = [21, 22, 23, 25, 53, 80, 135, 443 , 445]
    for port in ports:
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
            engine.say("Ports" + str(port) + "is open")
        else:
            print(f"Port {port} is closed")
        
        # close the socket
        s.close()

def article():
    openai.api_key = "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"

# Define the prompt for the article
    prompt = command

# Generate the article using the OpenAI GPT-3 API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        top_p=0.87,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )
# Extract the generated article from the OpenAI response
    article = response.choices[0].text
    print(article)
    gedit = subprocess.Popen(["gedit", "-"], stdin=subprocess.PIPE)
    gedit.communicate(article.encode())
    if len(article) > 100:
        engine.say(". ".join(article[:3]))
        

#https://www.geeksforgeeks.org/fetching-top-news-using-news-api/#	



def Search():
    engine = pyttsx3.init()
# Taking input from user
    question = command

# App id obtained by the above steps
    app_id = '9V8UQK-JJJK9W9ETH'

# Instance of wolf ram alpha
# client class
    client = wolframalpha.Client(app_id)

# Stores the response from wolf ram alpha
    res = client.query(question)

# Includes only text from the response
    answer = next(res.results).text
    engine.say(answer)
    engine.runAndWait()
    print(answer)
    
#https://www.geeksforgeeks.org/python-create-a-simple-assistant-using-wolfram-alpha-api/


# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define wake-up phrase
wake_up_phrase = "jarvis"

# Continuously listen for commands
while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=7)
    try:
        # Use speech recognition engine to convert audio to text
        command = r.recognize_google(audio)
        print("Command: " + command)
        
        # Check if wake-up phrase is detected
        if wake_up_phrase in command.lower():
            # Respond with confirmation
            engine.say("Hello sir,I'm listening.")
            engine.runAndWait()
            # Listen for command after wake-up phrase
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, phrase_time_limit=7)
            try:
                # Use speech recognition engine to convert audio to text
                command = r.recognize_google(audio)
                print("Command: " + command)
                command = r.recognize_google(audio).lower()
                print(f"Command recognized: {command}")
                if "open file explorer" in command:
                    engine.say("opening file explorer")
                    engine.runAndWait()
                    subprocess.call(["explorer"])
                elif "chrome" in command:
                    chrome()
                elif "facebook" in command:
                    facebook()
                elif "youtube" in command:
                    youtube()
                elif "shutdown" in command:
                    os.system("sudo shutdown -h now")
                elif "message" in command:
                    message()
                elif "email" in command:
                    email()
                elif "joke" in command:
                    tell_joke()
                elif "brightness" in command:
                    screen_brightness()
                elif "who" in command or "where" in command or "what" in command or "weather" in command:
                    Search()
                elif "search" in command:
                    search = command.replace("search", "")
                 # Open Google Chrome with the search query
                    engine.say("searching up " + search)
                    engine.runAndWait() 
                    webbrowser.open_new_tab('https://www.google.com/search?q=' + search)
                elif "ports" in command or "scanning" in command:
                    engine.say("Scanning ports now")
                    scan_ports()
                elif "call" in command:
                    calls()
                elif "user" in command:
                    add_user()	
                elif "article" or "blog" in command:
                    article()
            
            except sr.UnknownValueError:
                print("Could not understand audio")
                
                # Process command here..
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")

