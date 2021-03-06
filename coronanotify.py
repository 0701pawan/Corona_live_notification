import requests
from plyer import notification
from bs4 import BeautifulSoup
import time

#### The below function helps us notification on bottom left side of the system ####

def notifyMe(title, message):
    notification.notify(
        title = title,
        message =message,
        app_icon="C:\\Users\\User\\Downloads\\do.ico",
        timeout= 8
    )

#### The below functions help us fetch the raw live data from "https://www.mohfw.gov.in/" website####
def getData(url):
    r=requests.get(url)
    return r.text


if __name__=="__main__":
    myHtml=getData("https://www.mohfw.gov.in/")

    ### Here we manupulated that data to get that into a list form###
    soup = BeautifulSoup(myHtml, 'html.parser')
    myData=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myData+=tr.get_text()
    myData=myData[1:]
    itemList= myData.split("\n\n")

    states=['Jharkhand','Odisha','Uttar Pradesh']
### Here we check the state is in list or not , if it is found then the details of the state is get printed 
    for item in itemList[0:32]:
        dataList=item.split("\n")
        if dataList[1] in states:
            title="Cases of covid-19"
            sms=f"State:{dataList[1]}\nCases:{dataList[2]}\nCured:{dataList[3]}\nDeath:{dataList[4]}"
            notifyMe(title,sms)
            time.sleep(8)
