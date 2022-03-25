# 測試用 
import requests as asrequset
from bs4 import BeautifulSoup
import json
import datetime
import os

#建立存檔圖片區塊

dirImgName = 'tecoImg'

if not os.path.exists(dirImgName):
    os.mkdir(dirImgName)
    print("Directory " , dirImgName ,  " Created ")
else:    
    print("Directory " , dirImgName ,  " already exists")

dirTxtName = 'tecoTxt'

if not os.path.exists(dirTxtName):
    os.mkdir(dirTxtName)
    print("Directory " , dirTxtName ,  " Created ")
else:    
    print("Directory " , dirTxtName ,  " already exists")


#爬蟲網址-科技新知

responseTXT =asrequset.get("https://technews.tw/")

teco = BeautifulSoup(responseTXT.text, "html.parser")

today = datetime.date.today().strftime("%Y%m%d")

#開啟檔案，沒有檔案則直接新建
file_object = open("tecoTxt/" + today + "爬蟲.txt", "w+")

tecoResult = teco.select('div.wrapper div.topblack div.img a')
tecoImgResult =teco.select('div.wrapper div.topblack div.img a div.height img')

#寫入圖片
q=0 
for s in tecoImgResult:
    # 操作：寫入
    q+=1
    pic=asrequset.get(s["src"])
    img2 = pic.content
    pic_out = open("tecoImg/" + today + str(q) +".png",'wb')
    pic_out.write(img2)
    pic_out.close()

#寫入文件
for s in tecoResult:
    # 操作：寫入
    data = [s["href"], s.text]
    file_object.writelines(data)
# 關閉  
file_object.close()




"""
爬蟲其他網頁資訊
url = "https://technews.tw/""
    r = requests.get(url)
    teco = BeautifulSoup(r.text,"html.parser")
    
    sel = teco.select("div.title a") #搜尋下一個想要搜尋網頁的動作
    u = soup.select("div.btn-group.btn-group-paging a") #a標籤
    print ("本頁的URL為"+url)
    url = "網站名稱"+ u[1]["href"] #下一個目標的的網址

for s in sel: #印出網址跟標題
    print(s["href"],s.text)

"""





