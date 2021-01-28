import time
from datetime import datetime as dt

file_path = "hosts"
#real hosts file at path --- C:\Windows\System32\drivers\etc\hosts
redirect = "127.0.0.1"
website_list = ["facebook.com","www.facebook.com","youtube.com","www.youtube.com"]

def alterhosts(bState):
    with open(file_path,"r+") as file:
        
        if bState:
            print("add content")
            content = file.read()
            for website_name in website_list:
                if website_name in content:
                    pass
                else:
                    file.write(redirect+" "+website_name+"\n")
        else:
            print("remove content")
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
                

hours = (8,16)
concluded = False

while not concluded:
    current_time = dt.now()

    print(hours[0] < current_time.hour < hours[1])
    if  hours[0] < current_time.hour < hours[1]:
        alterhosts(True)
    else:
        alterhosts(False)
        if current_time.hour>=hours[1]:
            concluded = True

    time.sleep(30) 