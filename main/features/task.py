from features.communicate import speak, takecommand, log


def getTime(query):
    """Tell user the current time"""
    try:
        from bs4 import BeautifulSoup
        import requests

        query = query.replace(" ", "+")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')

        page = soup.find('div', class_='gsrt')
        page2 = soup.find('span', class_='vk_gy')

        time = page.get_text()
        location = page2.get_text()
        location = str(location).replace("Time ", "")
        speak(f"Master, It is {time}{location}.")

    except Exception as e:
        import datetime
        strTime = str(datetime.datetime.now().strftime("%I:%M %p"))
        speak(f"Master, It is {strTime} here.")
        log(e)
    
def getCalendar(query):
    """Tell user the current date or day"""
    try:
        from bs4 import BeautifulSoup
        import requests

        query = query.replace(" ", "+")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')

        page3 = soup.find('div', class_='vk_bk')
        page4 = soup.find('span', class_='vk_gy')

        day = page3.get_text()
        location = page4.get_text()
        location = str(location).replace("Date ", "")

        speak(f"It is {day}{location}")

    except Exception as e:
        import datetime
        strDate = str(datetime.datetime.now().strftime("%A, %-d %B %Y"))
        speak(f"Master, It is {strDate} here.")
        log(e)

def wishMe(start=True):
    """Wish the user"""
    import datetime
    import time
    hour = int(datetime.datetime.now().hour)
    strTime = time.strftime("%I:%M %p")

    if start == True:
        if hour >= 0 and hour < 12:
            speak(f"Good Morning! Its {strTime}")

        elif hour >= 12 and hour < 16:
            speak(f"Good Afternoon! Its {strTime}")

        else:
            speak(f"Good Evening! Its {strTime}")
        speak(f"Hello Master, How may I help you?")
    else:
        if hour >= 0 and hour < 12:
            speak(f"Good Morning Master!")

        elif hour >= 12 and hour < 16:
            speak(f"Good Afternoon Master!")

        else:
            speak(f"Good Evening Master!")

def searchGoogle(query, patterns=[""]):
    try:
        ignoreWords = patterns
        for words in ignoreWords:
            wquery = str(query).replace(words, "")
            
        print("Searching Google Chrome...")
        
        import webbrowser
        browser = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito')

        browser.open_new(f"https://www.google.com/search?q={query}")

    except Exception as e:
        log(e)

def wikiData(query, patterns=[""]):
    try:
        print("Searching WikiPedia...")

        ignoreWords = patterns
        for words in ignoreWords:
            wquery = str(query).replace(words, "")

        import wikipedia
        result = wikipedia.summary(wquery, sentences=2)
        speak(f"According to Wikipedia, {result}")
    except Exception as e:
        log(e)
        searchGoogle(query, patterns)

def googleData(query, patterns=[""]):
    try:
        print("Searching Google...")

        from bs4 import BeautifulSoup
        import requests

        ignoreWords = patterns
        for words in ignoreWords:
            wquery = str(query).replace(words, "")

        query = query.replace(" ", "+")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        klasses = ['LGOjhe', 'Z0LcW', 'IZ6rdc', 'kno-rdesc']
        results = []

        for klass in klasses:
            data = soup.find('div', class_=klass)
            if data != None:
                results.append(data)
            else:
                pass

        size = len(results)

        if size != 0:
            for data in results:
                if "." in data.get_text() or size == 1:
                    try:
                        repldata = str(data.find('span', class_='JPfdse').get_text())
                        repdata = str(data.find('g-bubble').get_text())
                    except:
                        repldata = ""
                        repdata = ""
                    data = str(data.get_text())
                    data = data.replace(repdata, repldata).replace("Description", "").replace("Wikipedia", "")
                    speak(data)
                    break
                else:
                    pass
        else:
            raise ValueError("No results found")

    except Exception as e:
        log(e)
        wikiData(query, patterns)

def youtubeData(query, patterns):
    try:
        print("Searching Youtube...")
        ignoreWords = patterns
        for words in ignoreWords:
            query = str(query).replace(words, "")
        browser = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito')
        browser.open_new(f"https://www.youtube.com/search?q={query}")
    except Exception as e:
        log(e)

def getWeather(query):
    try:
        from bs4 import BeautifulSoup
        import requests

        query = query.replace(" ", "+")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        temp = soup.select('#wob_tm')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()

        speak(f"It is {temp}°C ({info}) in {location}.")

    except Exception as e:
        speak("Master, Its hard to get temperature now!")
        log(e)

def getPrecipitation(query):
    try:
        from bs4 import BeautifulSoup
        import requests

        query = query.replace(" ", "+")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        ppChance = soup.select('#wob_pp')[0].getText().strip()

        # speak(f"It is {temp}°C ({info}) in {location}.")
        ppChanceInt = int(ppChance.replace("%", ""))
        if ppChanceInt >= 20 and ppChanceInt < 40:
            speak(f"Yes Master, there are some chance to precipitate.")
        elif ppChanceInt >= 40 and ppChanceInt < 60:
            speak(f"Yes Master, there is a high chance to precipitate.")
        elif ppChanceInt >= 60:
            speak(f"Yes Master, there is very high chance to precipitate.")
        else:
            speak("No Master, there is very less chance to precipitate")
        print(f"Percentage Of Precipitation (PoP): {ppChance}")

    except Exception as e:
        speak("Master, Its hard to get the Precipitation data now!")
        log(e)

def getNews(query:str):
    try:
        print("Searching news...")
        import requests

        query = query.replace(" ", "+")

        main_url = "https://newsapi.org/v2/everything"
        query_params = {
        "q": query,
        "apiKey": "e885d04a980e4629af6a487991bf3981"
        }

        if "top" in query:
            query_params.update({"sortBy": "top"})
        elif "popular" in query:
            query_params.update({"sortBy": "popularity"})
        # elif "from" in query:
        #     l = query.split("from+")
        #     parm = str(l[len(l)-1])
        #     query_params.update({"sources": parm})
        # elif "related" in query:
        #     query_params.update({"sortBy": "relevancy"})

        categoryl = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        
        for category in categoryl:
            if category in query:
                query_params.update({"category": category})
                main_url = "https://newsapi.org/v2/top-headlines"
                break
            else:
                pass

        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        article = open_bbc_page["articles"]
    
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        i = 0
        count = 0
        while i != 10:
            if "<" in results[count] and ">" in results[count] or "..." in results[count]:
                i = i
            else:
                speak(f"{i+1}. {results[count]}")
                i += 1
            count += 1

    except Exception as e:
        log(e)
        speak("Master, Its hard to get the News now!")

def playMedia(query:str):
    try:
        from googleapiclient.discovery import build

        apiKey = 'AIzaSyCLJ77KOHuRB7jLJmSn78MQtePP0O9q838'
        service = build('youtube', 'v3', developerKey=apiKey)

        request = service.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=1
        )

        response = request.execute()

        for item in response['items']:
            title = item['snippet']['title']
            videoID = item['id']['videoId']
            url = f"https://www.youtube.com/watch?v={videoID}"

        speak(f"Playing {title}")

        import webbrowser
        browser = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito')
        browser.open_new(url)
        service.close()

    except Exception as e:
        speak("Master, I'm having some problems in playing media!")
        log(e)

def getJoke():
    import pyjokes
    joke = pyjokes.get_joke('en', 'all')
    speak(joke)

def getScrnShot():
    import pyautogui
    pyautogui.hotkey('winleft', 'prtscr')
    speak("Taken Screenshot.")

def getSnip():
    import pyautogui
    pyautogui.hotkey('winleft', 'shift', 's')

def clearCache():
    try:
        speak("Clearing Cache files")
        import pathlib
        import os
        pathList = [f"{pathlib.Path.home()}/AppData/Local/Temp/", "C:/Windows/Temp/", "C:/Windows/Prefetch/"]
        for path in pathList:
            os.chdir(path)
            list = os.listdir(path)
            for file in list:
                try:
                    os.remove(f"{path}{file}")
                except Exception as e:
                    pass

    except Exception as e:
        log(e)

def getBattery():
    try:
        import psutil
        import time
        battery = psutil.sensors_battery()
        battery_usage = int(battery.percent)
        battery_plug = battery.power_plugged
        battery_hour = time.strftime("%H", time.gmtime(battery.secsleft))
        battery_min = time.strftime("%M", time.gmtime(battery.secsleft))

        if battery_hour == "01":
            battery_htime = f"an hour"
        elif battery_hour == "00":
            battery_htime = ""
        else:
            battery_htime = f"{battery_hour} hours"

        if battery_min == "01":
            battery_mtime = f"{battery_min} minute"
        elif battery_min == "00":
            battery_mtime = ""
        else:
            battery_mtime = f"{battery_min} minutes"

        battery_time = f"{battery_htime} {battery_mtime}"

        if battery_plug == True:
            speak(f"System is at {battery_usage}% and plugged in.")
        else:
            speak(f"System is at {battery_usage}% and can work for around {battery_time}.")

    except Exception as e:
        log(e)

def logOut(self):
    import os
    import time
    speak("Do you want to logout from the System?")
    confirmation = takecommand(self)
    if "yes" in confirmation:
        speak("Logging you out from the System...")
        time.sleep(5)
        os.system("shutdown - l")
    else:
        print("Jessica: Cancelled Log Out")

def shutDown(self):
    import os
    import time
    speak("Do you want to shutdown the System?")
    confirmation = takecommand(self)
    if "yes" in confirmation:
        speak("Shutting down the System...")
        print(confirmation)
        time.sleep(5)
        os.system("shutdown /s /t l")
    else:
        print(confirmation)
        print("Jessica: Cancelled Shut Down")

def winRun(query):
    import pyautogui
    pyautogui.hotkey('winleft', 'r')

    for word in query:
        pyautogui.press(word)
    pyautogui.press("enter")

def openApp(query):
    query = str(query).replace(" ", "").replace("open", "")
    import webbrowser
    ibrowser = webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito')
    browser = webbrowser.get('windows-default')
    import pyautogui
    speak("Opening...")
    try:
        if "google" in query:
            browser.open("https://www.google.com/")
        elif "youtubemusic" in query:
            browser.open("https://music.youtube.com/")
        elif "youtube" in query:
            browser.open("https://www.youtube.com/")
        elif "mail" in query or "gmail" in query:
            browser.open("https://mail.google.com/")
        elif "whatsapp" in query:
            browser.open("https://web.whatsapp.com/")
        elif "instagram" in query:
            browser.open("https://www.instagram.com/")
        elif "facebook" in query:
            browser.open("https://www.facebook.com/")
        elif "chrome" in query:
            browser.open("https://chrome://new-tab-page")
        elif "taskmanager" in query:
            winRun("Taskmgr")
        elif "commandprompt" in query or "cmd" in query:
            winRun("cmd")
        elif "explorer" in query:
            winRun("explorer")
        elif "notepad" in query:
            winRun("notepad")
        elif "controlpanel" in query:
            winRun("control")
        elif "registryeditor" in query:
            winRun("regedit")
        elif "services" in query:
            winRun("services.msc")
        elif "gpeditor" in query or "grouppolicyeditor" in query:
            winRun("gpedit.msc")
        elif "taskview" in query:
            pyautogui.hotkey('winleft', 'tab')
        elif "hiddenmenu" in query:
            pyautogui.hotkey('winleft', 'x')
        elif "windowsetting" in query or "windowssettings" in query or "windowssetting" in query:
            pyautogui.hotkey('winleft', 'i')
        else:
            ibrowser.open_new(f"https://www.google.com/search?q={query}")
    except Exception as e:
        speak("Master there is a problem!, Kindly Try Again.")
        log(e)

def quickTask(query):
    try:
        from bs4 import BeautifulSoup
        import requests

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        res = requests.get(f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome.0.69i59j0i512l3j0i22i30l6.1684j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        page = soup.find_all('input', class_='vXQmIe')
        valueList = []

        for selection in page:
            value = selection.attrs['value']
            value = str(value).replace("e", " times 10 to the power ")
            valueList.append(value)

        page = soup.find_all('select', class_='OR9QXc')
        unitList = []

        for selection in page:
            unit = selection.find("option", {"selected":"1"}).get_text()
            unit = str(unit).replace("/", "per")
            unitList.append(unit)

        speak(f"Master, {valueList[0]} {unitList[0]} is {valueList[1]} {unitList[1]}")

    except Exception as e:
        log(e)