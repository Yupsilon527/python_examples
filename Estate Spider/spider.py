import requests
from bs4 import BeautifulSoup
import pandas

r=requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
soup = BeautifulSoup(r.content,"html.parser")
nr_pages = int(soup.find_all("a",{"class":"Page"})[-1].text)

fdl=[]

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,nr_pages*10,10):
    new_url = base_url+str(page)+".html"
    if page==0:
        new_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"
    r=requests.get(new_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    soup = BeautifulSoup(r.content,"html.parser")
    data = soup.find_all("div",{"class":"propertyRow"})

    for item in data:
        d={}
        d["Address"] = item.find("span",{"class":"propAddressCollapse"})
        d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace(" ","").replace("\n","")

        try:
            d["Locality"] = item.find("span",{"class":"propLocalityCollapse"})
        except:
            d["Locality"]=None
        try:
            d["Beds"] = item.find("h4",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None

        try:
            d["Area"] = item.find("h4",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Half Baths"] = item.find("h4",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        try:
            d["Full Baths"] = item.find("h4",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        for cg in item.find_all("div",{"class":"columnGroup"}):
            for group,name in zip(cg.find_all("span",{"class":"featureGroup"}),cg.find_all("span",{"class":"featureName"})):
                if "Lot Size" in group.text:
                    d["Lot Size"]=name.text
        fdl.append(d)

df = pandas.DataFrame(fdl)
df.to_csv("formatdata.csv")