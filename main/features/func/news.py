from PyQt5.QtCore import *

class NewsClient(QObject):
    def __init__(self, query):
        self.query = str(query).replace("news", "").strip().replace(" ", "+")
        self.main_url = "https://newsapi.org"
        self.version = "v2"
        self.query_params = {
        "apiKey": "e885d04a980e4629af6a487991bf3981"
        }
    
    def headlines(self):
        import requests
        self.query = self.query.replace("+headlines", "").replace("+headlines", "")
        self.full_url = f"{self.main_url}/{self.version}/top-headlines"

        categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        
        for category in categories:
            if category in self.query:
                self.query_params.update({"category": category})
                break
            else:
                pass

        self.query_params.update({"q": self.query})
        res = requests.get(self.full_url, params=self.query_params)
        open_bbc_page = res.json()
    
        article = open_bbc_page["articles"]
    
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        return results
    
    def description(self):
        import requests
        self.full_url = f"{self.main_url}/{self.version}/top-headlines"

    def retrieve(self):
        if "headline" in self.query:
            return self.headlines()
        else:
            return []
        # return self.headlines()


query = input("Enter: ")
newsclient = NewsClient(query)

results = newsclient.retrieve()


i = 0
count = 0
while i != 10:
    if "<" in results[count] and ">" in results[count] or "..." in results[count]:
        i = i
    else:
        print(f"{i+1}. {results[count]}")
        i += 1
    count += 1