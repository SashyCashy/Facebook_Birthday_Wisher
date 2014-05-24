'''
Created on 13-May-2014

@author: ReDhOoT
'''

'''
Created on 04-May-2014

@author: ReDhOoT
'''

"""Automatic Birthday Wisher"""

import facebook

import mechanize

import urllib,urllib2

from bs4 import BeautifulSoup

friendList=[]

loginUrl="https://www.facebook.com/login.php?login_attempt=1"
    
webcrawler=mechanize.Browser()
    
webcrawler.set_handle_robots(False)
    
soup=BeautifulSoup(webcrawler.open(loginUrl))
    
webcrawler.select_form(nr=0)
          
webcrawler.form["email"]="*************"
    
webcrawler.form["pass"]="**************"
    
request=webcrawler.submit()
    
soup=BeautifulSoup(request.read())
    
loginUrl="https://developers.facebook.com/tools/access_token/"

page = webcrawler.open(loginUrl)

soup=BeautifulSoup(page.read())

token=soup.findAll('code')[2]

graph=facebook.GraphAPI(token.text)

profile=graph.get_object("me")

friends=graph.get_connections("me","friends")

access_token = graph.access_token

print access_token
post_data = {'access_token':access_token, 'message':'hey this is a test!'}
request_path = 'me/feed'
post_data = urllib.urlencode(post_data)
response = urllib2.urlopen('https://graph.facebook.com/%s' % request_path, post_data)



#graph.put_wall_post("Posting on my wall!")
count=0
#graph.put_object("me","feed",message="Hi");
#print "Presenting my Friends List:-"


    
    
'''
for friend in friends['data']:
            
            friends_profile=graph.get_object(friend['id'])
            #print type()
            name=friends_profile['name'].encode("utf-8")
            id=friends_profile['id'].encode("utf-8")
            #FbInfo.write(name+' '+id+'\n')
            friend_nameId=name+' '+id
            friendList.insert(count,friend_nameId)
            print name+' '+id
            count=count+1'''
            

#FbInfo.close()
def writeinFile():
    Friend = open("FriendList.txt", "w")
    for friend in friendList:
        Friend.write("%s\n" % friend)
    Friend.close()

#writeinFile()