from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 
bright_stars = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(bright_stars)
soup=bs(page.text,"html.parser")
startable=soup.find("table")

temp_list=[]
tablerows=startable.find_all("tr")
for tr in tablerows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    starnames.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df2=pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
df2.to_csv("bright_stars.csv")