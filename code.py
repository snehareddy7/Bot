import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hi.. I am Alex")
    print("Say Something") #User should say something that has the name of Bot
    audio = r.listen(source,0,5)
    print("Stop Saying")
    try:
      text = r.recognize_google(audio)
      if 'Alex' not in text:
        print("Bot is not active")
        exit(0)
      else:
        print("How are you?")
        print("Say Something")
        audio = r.listen(source,0,5)
        print("Stop Saying")
        try:
          text = r.recognize_google(audio)
          print('You Said :'+text)
        except:
          print("Pls try to speak clearly")
        print("Are you feeling well ?")
        print("Say Something")
        audio = r.listen(source,0,5)
        print("Stop Saying")
        try:
          text = r.recognize_google(audio)
          print('You Said :'+text)
        except:
          print("Pls try to speak clearly")
    except:
      print("Pls try to speak clearly")
      exit(0)