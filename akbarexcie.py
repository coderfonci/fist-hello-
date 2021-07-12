import requests 
import json 
def speak(str):
    from win32com.client import Dispatch
    
    speak = Dispatch("sapi.spvoice")
    speak.speak(str)

if __name__ =='__main__':
    #speak("hallo ")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=034454a0810b4c069f413c4065be63da"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["status"])
    print (news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article["title"])
        speak("moving on the next news... Listen carefully")