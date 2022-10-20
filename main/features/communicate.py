import pyttsx3
import speech_recognition as sr

error_list = [""]

def log(error):
    """Log an error into the log file."""
    import time
    curr_time = time.strftime("%x %H:%M:%S", time.localtime())

    if error != "":
        try:
            error = str(error).replace("\n", ",")
            error_list.append(error)
            list_len = len(error_list)
            
            if error == error_list[list_len-1] and error == error_list[list_len-2] and error == error_list[list_len-3]:
                pass
            else:
                open('static/log.txt', 'a').write(f"[{curr_time}]   {error}\n")
        except:
            pass
    else:
        pass

def speak(audio):
    """Speaks a String."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    ignore_words = ["|", ": ", '"\"', "/", "  "]
    for words in ignore_words:
        audio = str(audio).replace(words, " ")
    print(f"Jessica: {audio}\n")
    engine.say(audio)
    engine.runAndWait()

def takecommand(self):
    """Take microphone input from the user and return a string output"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        self.right_dataEmmited.emit(1)
        # winsound.PlaySound("static/beep_short.ogg", winsound.Beep(50, 1000))
        # winsound.Beep(500, 500)
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        # audio = r.listen(source, 0, 5)
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing")
        self.right_dataEmmited.emit(2)
        r = sr.Recognizer()
        query = str(r.recognize_google(audio, language='en-in'))
        print(f"User: {query.capitalize()}\n")
    except Exception as e:
        if type(e) == str:
            log(e)
        else:
            pass
        query = "Error"

    return query.lower()
