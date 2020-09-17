from bs4 import BeautifulSoup
import requests

def open_content():
    import random 
    c = random.randint(0, 10)  
    f = open('content/'+str(c)+'.txt' , 'r')
    a = f.read()
    f.close()
    return {"response":{"text":a}} 

def parse(text):
    url = 'https://yandex.ru/search/?text=' + text
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all("li",{"class":"serp-item"})
    response ={"response":[]}
    for i in items:
        response["response"].append({"text":i.text,"url":i.contents[0]})
    return response
