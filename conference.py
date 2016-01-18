# -*- coding: utf-8 -*-
from urllib2 import *
from bs4 import BeautifulSoup
import threading


ConNameList = []
ConLocList = []
ConDateList = []

def init():
        ConNameList = []
        ConLocList = []
        ConDateList = []
        #Crawling
        url = "http://www.confsearch.org/confsearch/faces/pages/topic.jsp?topic=Security&sortMode=1&graphicView=0"
        
        response = urlopen(url)
        data = response.read()
        
        soup = BeautifulSoup(data, "html5lib")
        html_name =  soup.find_all(class_="venueAlive venueKeywords")
        for name in html_name:
                ConNameList.append(name.string)

        html_loc =  soup.find_all(class_="locationColumn")
        for loc in html_loc:
                ConLocList.append(loc.span.string)
        html_date = soup.find_all(class_="dateColumn")
        index_couter = 0
        templist = []
        for dates in html_date:
                templist.append(dates.span.string)
                if index_couter%4 == 3:
                        ConDateList.append(templist)
                index_couter+=1    
                                   
        print len(ConNameList) 
        print len(ConLocList)  
        print len(ConDateList)
        threading.Timer(7200, init).start()


def get_Confer_Info(Searchname=""):
        #Some Constant
        ENTERSTR = "\n"
        RETURNSTR = ""
        DEAD = 0
        NOTI = 1
        START = 2
        END = 3

        #List Search
                 
        for i in range(len(ConNameList)):
                if ConNameList[i].lower().find(Searchname.lower()) >= 0:
                        RETURNSTR += ConNameList[i] + " - " + ConDateList[i][DEAD] + ENTERSTR

        return RETURNSTR
#initialize
init()
