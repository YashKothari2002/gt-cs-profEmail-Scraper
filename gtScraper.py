import requests
from bs4 import BeautifulSoup as bs
import json
import time
import re



def findEmails(area):

    URL = 'https://ic.gatech.edu/person/faculty'
    URL2 = 'https://ic.gatech.edu'

    print("HELLO")
    # time.sleep(600)

    req = requests.get(URL)
    print("HELLO")
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div',attrs={'class','row clearfix'})

    get_URL = []

    for i in range (len(titles)):
        if(titles[i].a.text == "Faculty"):
            temp = titles[i]
            print(temp)
            # for j in range (len(temp)):
            #     print(temp)
            #     print("BREAK")

            temp = str(temp)
            soup1 = bs(temp, 'html.parser')
            
            
            allLinks = soup1.find_all('a')

            for j in (allLinks):
                get_URL.append(URL2 + j.get('href'))
                
    res = []

    [res.append(x) for x in get_URL if x not in res]

    res = res[4:]
    emailList = []

    for i in range (len(res)):
        req2 = requests.get(res[i])
        # time.sleep(20)
        soup2 = bs(req2.text, 'html.parser')
        
        temp2 = soup2.find_all('div', attrs = {'class', 'row clearfix'})

        temp2 = str(temp2)
        soup3 = bs(temp2, 'html.parser')
        
        temp3 = soup3.find_all('div', attrs = {'class', 'group-person-wrapper'})
        
        print(temp3[0].a)
        
        
        resAr = soup3.find_all('div', attrs = {'class', 'field-item even'})
        
        varCheck = -1
        for i in resAr:
            if area in i.text:
                print(area + " IS COOL")
                varCheck = 1            
            else:
                continue
            
        if varCheck != -1:
            try:
                emailList.append(temp3[0].a.text)
            except:
                continue
            
        
        # print(email1.a)
        
        # soup4 = bs(email1, 'html.parser')
        
        
        # print(soup4)
        
        print("HELLO")

    print(emailList)
    return emailList
