#!/usr/bin/env python
# coding: utf-8

# In[74]:


from bs4 import BeautifulSoup
import requests


# In[75]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[76]:


soup = BeautifulSoup(page.content)
soup


# In[77]:


header = soup.find('span',class_="mw-headline")
header.text


# In[78]:


header= []

for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)
header


# #Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.

# In[79]:


page = requests.get('https://www.imdb.com/chart/top')
page


# In[80]:


soup = BeautifulSoup(page.content)
soup


# In[81]:


movie = soup.find('td',class_="titleColumn")
movie.text


# In[82]:


year = soup.find('span',class_="secondaryInfo")
year.text


# In[83]:


rating = soup.find('td',class_="ratingColumn imdbRating")
rating.text


# In[84]:


movie = []
for i in soup.find_all('td',class_="titleColumn"):
    movie.append(i.text.replace('\n',''))
movie


# In[85]:


mov = movie[0:100]
mov


# In[ ]:





# In[86]:


year = []

for i in soup.find_all('span',class_="secondaryInfo"):
    year.append(i.text)
year

yr = year[0:100]
yr


# In[87]:


print(len(yr))


# In[88]:


rating = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.replace('\n',''))
    
rating

rt= rating[0:100]
rt


# In[89]:


import pandas as pd
df = pd.DataFrame({'Movies':mov,'year_release':yr,'Rating':rt})
df


# In[ ]:





# In[ ]:





# #Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[90]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[91]:


soup = BeautifulSoup(page.content)
soup


# In[92]:


indianmov = soup.find('td',class_="titleColumn")
indianmov.text


# In[93]:


india = []

for i in soup.find_all('td',class_="titleColumn"):
    india.append(i.text.replace('\n',''))
    
india


# In[94]:


indianmov = india[0:100]
indianmov


# In[95]:


year = []

for i in soup.find_all('span',class_="secondaryInfo"):
    year.append(i.text)
year

yr = year[0:100]
yr


# In[96]:


rating = []

for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.replace('\n',''))
rating
rt= rating[0:100]
rt


# In[97]:


df = pd.DataFrame({'Indian_mov':indianmov,'Year':yr,'Rating':rt})
df


# In[ ]:





# In[ ]:





# #Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7vbp .

# In[98]:


page = requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
page


# In[99]:


soup = BeautifulSoup(page.content)
soup


# In[100]:



name = soup.find('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS")
name.text


# In[101]:


product = []
for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    product.append(i.text)
    
product


# In[102]:


price = []

for i in soup.find_all('h5',color="greyBase"):
    price.append(i.text)
    
price    


# In[103]:


disct = []

for i in soup.find_all('div', class_="Card__BaseCard-sc-b3n78k-0 iJCKg NewProductCard__DiscountRow-sc-j0e7tu-15 kUcVjG NewProductCard__DiscountRow-sc-j0e7tu-15 kUcVjG"):
    disct.append(i.text)
    
disct    


# In[104]:



df = pd.DataFrame({'Product':product,'Price':price,'Distcount':disct})
df


# In[ ]:





# In[ ]:





# #Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# In[105]:


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[106]:


soup = BeautifulSoup(page.content)
soup


# In[107]:


team = soup.find('span',class_="u-hide-phablet")
team.text


# In[108]:


team = []

for i in soup.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)
team

tm = team[0:10]
tm


# In[109]:


match = soup.find('td',class_="rankings-block__banner--matches")
match.text


# In[110]:


match = []

for i in soup.find_all('td',class_="rankings-block__banner--matches"):
   match.append(i.text)
match 


# In[111]:


point = soup.find('td',class_="rankings-block__banner--points")
point.text


# In[112]:


points = []

for i in soup.find_all('td',class_="rankings-block__banner--points"):
    points.append(i.text)
points


# In[113]:


new_list = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    new_list.append(i.text)
new_list
   


# In[114]:


matches = []
points = []

for i in range(0,len(new_list)-1,2):
    matches.append(new_list[i])
    points.append(new_list[i+1])
matches,points


# In[115]:


rating = soup.find('td',class_="table-body__cell u-text-right rating")
rating.text


# In[116]:


rt = []

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rt.append(i.text)
rt


# In[ ]:





# In[ ]:





# In[117]:


page = requests.get('https://coreyms.com/')
page


# In[118]:


soup = BeautifulSoup(page.content)
soup


# In[119]:


heading = soup.find('a',class_="entry-title-link")
heading.text


# In[120]:


head = []

for i in soup.find_all('a',class_="entry-title-link"):
    head.append(i.text)
head


# In[121]:


time = soup.find('time',class_="entry-time")
time.text


# In[122]:


date = []

for i in soup.find_all('time',class_="entry-time"):
    date.append(i.text)
date


# In[123]:


content = soup.find('div',class_="entry-content")
content.text


# In[124]:


content = []

for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text.replace('\n',''))
content


# In[125]:


code = soup.find('div',class_="ytp-impression-link-text")
code


# In[ ]:





# #Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, 
# Rajaji Nagar.
# 

# In[ ]:





# In[202]:


page = requests.get('https://www.nobroker.in/property/sale/mumbai/multiple?searchParam=W3sibGF0IjoyMC4zNDY4NjgyLCJsb24iOjczLjk5MTgxODEsInBsYWNlSWQiOiJDaElKSy1kUFFOZDMzanNSN3FIVkFoRWRpQ1EiLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifSx7ImxhdCI6MTkuMjI0NTI5NCwibG9uIjo3Mi44NTkzMDIsInBsYWNlSWQiOiJDaElKRlNxanZ0T3c1enNST3NoalJ6UmJQOUEiLCJwbGFjZU5hbWUiOiJKYXlhIE5hZ2FyIn0seyJsYXQiOjEyLjk3NzMwMDksImxvbiI6NzcuNTU1NTAzNywicGxhY2VJZCI6IkNoSUpueDdfcl9BOXJqc1JzdUtDdkljN1Q5USIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=mumbai&locality=Indira%20Nagar,&locality=Jaya%20Nagar,&locality=Rajajinagar')
page


# In[203]:


soup = BeautifulSoup(page.content)
soup


# In[204]:


house = soup.find('h2',class_="heading-6 font-semi-bold nb__25Cl7")
house.text


# In[205]:


loc = soup.find('div',class_="nb__nXU01")
loc.text


# In[206]:


area = soup.find('div',class_="nb__FfHqA")
area.text


# In[207]:


area = []
for i in soup.find_all('div',class_="nb__FfHqA"):
    area.append(i.text)
area


# In[211]:


emi = []
price = []

for i in range(0,len(cost)-1,2) :
    emi.append(cost[i])
    price.append(cost[i+1])
emi,price


# In[208]:


cost = []
for i in soup.find_all('div',class_="font-semi-bold heading-6"):
    cost.append(i.text)
cost


# In[133]:


house = []

for i in soup.find_all('h2',class_="heading-6 font-semi-bold nb__25Cl7"):
    house.append(i.text)
house


# In[134]:


area = []

for i in soup.find_all('div',class_="nb__FfHqA"):
    area.append(i.text)
area


# #6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# In[135]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page


# In[136]:


soup = BeautifulSoup(page.content)
soup


# In[137]:


team = soup.find('span',class_="u-hide-phablet")
team.text


# In[138]:


match = soup.find('td',class_="rankings-block__banner--matches")
match.text


# In[139]:


ma = [match.text]
ma


# In[140]:


point = soup.find('td',class_="rankings-block__banner--points")
point.text

pnt = [point.text]
pnt


# In[141]:


rate = soup.find('td',class_="rankings-block__banner--rating u-text-right")
rate.text
rates = [rate.text.replace('\n','')]
rates


# In[142]:


team = []
for i in soup.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)
team
tm = team[0:10]
tm


# In[143]:


match = []
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    match.append(i.text)
match


# In[144]:


mat = []
pt =[]
for i in range(0,len(match)-1,2):
    mat.append(match[i])
    pt.append(match[i+1])
mat,pt


# In[145]:


matches = ma + mat
matches
matche = matches[0:10]
matche


# In[146]:


pont = pnt + pt
pont

points = pont[0:10]
points


# In[147]:


rat = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rat.append(i.text)
rat
    


# In[148]:


rt = rates + rat
rt
rates = rt[0:10]
rates


# In[149]:


df = pd.DataFrame({"Teams":tm,"Matches":matche,"Points":points,"Rating":rates})
df


# In[150]:


page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page


# In[151]:


soup = BeautifulSoup(page.content)
soup


# In[152]:


player1 = soup.find('div',class_="rankings-block__banner--name")
player1.text

player1 = [player1.text]
player1


# In[153]:


player = []
for i in soup.find_all('td',class_="table-body__cell name"):
    player.append(i.text.replace('\n',''))
player
players = player1 + player[0:9]
players


# In[154]:


team1 = soup.find('div',class_="rankings-block__banner--nationality")
tm = [team1.text.split()[0]]
tm


# In[155]:


team = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    team.append(i.text)
team
teams = tm + team[0:9]
teams


# In[156]:


rate1 = soup.find('div',class_="rankings-block__banner--rating")
rate1.text
rate1 = [rate1.text]
rate1


# In[157]:


ra = []
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ra.append(i.text)
rate = ra[0:9]
rate
rates = rate1+rate
rates


# In[158]:


df = pd.DataFrame({"Bat_players":players,"Teams":teams,"Rates":rates})
df
   


# In[159]:


player = soup.find("span",class_='u-hide-phablet')
player.text


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #Write a python program to scrape mentioned details from dineout.co.in :

# In[160]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[161]:


soup = BeautifulSoup(page.content)
soup


# In[162]:


name = soup.find('a',href="/delhi/castle-barbeque-connaught-place-central-delhi-86792")
name.text


# In[163]:


rest_name = []
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    rest_name.append(i.text)
rest_name


# In[164]:


loc = soup.find('div',class_="restnt-loc ellipsis")
loc.text


# In[165]:


loc = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    loc.append(i.text)
loc


# In[166]:


cuisin = soup.find('div',class_="detail-info")
cuisin.text.split('|')[1]


# In[167]:


cuisine = []
for i in soup.find_all('div',class_="detail-info"):
    cuisine.append(i.text.split('|')[1])
cuisine


# In[168]:


rate = soup.find('div',class_="restnt-rating rating-4")
rate.text


# In[169]:


rating = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[172]:


image_url = []
for i in soup.find_all('img',class_="no-img"):
    image_url.append(i['data-src'])
image_url


# In[174]:


df = pd.DataFrame({"Restraunt_name":rest_name,"Location":loc,"Cuisine":cuisin,"Rating":rating,"image_url":image_url})
df


# #Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/women-tshirts?ga_q=tshirts .

# In[176]:


page = requests.get('https://www.bewakoof.com/women-tshirts?ga_q=tshirts')
page


# In[177]:


soup = BeautifulSoup(page.content)
soup


# In[182]:


prdt_name = soup.find('div',class_="productCardDetail")
prdt_name.text.split('₹')[0]


# In[194]:


prdct_name = []
for i in soup.find_all('div',class_="productCardDetail"):
    prdct_name.append(i.text.split('₹'))
prdct_name


# In[ ]:





# In[ ]:




