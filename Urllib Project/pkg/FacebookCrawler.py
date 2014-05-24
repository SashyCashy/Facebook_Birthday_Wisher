'''
Created on 07-May-2014

@author: ReDhOoT
'''
import mechanize

import re

from bs4 import BeautifulSoup

bday=BeautifulSoup()
    
def writeInFile(read):
       
    
    FbInfo=open('FbInfo.txt','w')
    FbInfo.write(read)
    FbInfo.close()
    
    FbInfo=open('FbInfo.txt','r')

    data=''
    for line in FbInfo:
        data=line+data
        
    start_index=data.find('fbRemindersThickline')
    data=data[start_index:]
    
    end_index=data.find('/span')
    
    soup=BeautifulSoup(data[:end_index])
   
    global bday
    
    bday=soup.find(name='span',attrs={'class','fbRemindersTitle'})
    
    FbInfo.close()
    


    
    
    
def fbLogin():
    
    loginUrl="https://www.facebook.com/login.php?login_attempt=1"
    
    webcrawler=mechanize.Browser()
    
    webcrawler.set_handle_robots(False)
    
    soup=BeautifulSoup(webcrawler.open(loginUrl))
    
    webcrawler.select_form(nr=0)
          
    webcrawler.form["email"]="**********"
    
    webcrawler.form["pass"]="*************"
    
    request=webcrawler.submit()
    
    soup=BeautifulSoup(request.read())
    
    writeInFile(soup.prettify())
    
    FbInfo=open('FriendList.txt','r')
    
    for line in FbInfo:
        
        if line.find(bday.text.encode("utf-8"))==0:
            import ipdb
            ipdb.set_trace()
            line=line.split()
            
            break
        
    FbInfo.close()
    
    print line[2]
    
    '''page=webcrawler.open("https://www.facebook.com/"+line[2])
    
    soup=BeautifulSoup(page.read())
    
    FbInfo=open(line[0]+'.txt','w')
    FbInfo.write(soup.prettify())
    FbInfo.close()
    finder=soup.find("mentionsTextarea");
    print type(finder)
    soup=BeautifulSoup(finder)
    print soup.prettify()
    finder=soup.findAll('input')
    print finder'''
    

fbLogin()
#PostOnWall()