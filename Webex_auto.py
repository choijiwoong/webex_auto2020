from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time

user=[0,0,0]
infor=[]

infile=open("Webex_datafile.txt","r")#,encoding='UTF-8')
user=infile.readline().split()
index1=0
for line in infile:
    infor.append([])
    infor[index1]=line.split()
    if 0<len(infor[index1])<7:
        infor[index1].append(-1)
        infor[index1].append(-1)
    index1+=1
    
#초반 데이터 불러오기 종료

yoil=time.localtime().tm_wday
hour=datetime.today().hour

print("yoil=",yoil,"hour=",hour)

def pre():
    elem=driver2.find_element_by_name("username")
    elem.clear()
    elem.send_keys(user[0])
    elem=driver2.find_element_by_name("password")
    elem.clear()
    elem.send_keys(user[1])
    elem.submit()

def convert(i):
    if i=='월':
        return 0
    elif i=='화':
        return 1
    elif i=='수':
        return 2
    elif i=='목':
        return 3
    elif i=='금':
        return 4
    elif i=='토':
        return 5
    elif i=='일':
        return 6
    else:
        return -1
    
boolean=0
for line in infor:
    if (yoil==convert(line[3]) and (hour==int(line[4])-1 or hour==int(line[4]))) or (yoil==convert(line[5]) and (hour==int(line[6])-1 or hour==int(line[6]))):
        print("지금은",line[0],'시간입니다.')
        boolean=1
        driver2=webdriver.Chrome(user[2])
        driver2.get(line[2])
        pre()
        driver=webdriver.Chrome(user[2])
        driver.get(line[1])
        break
            
if boolean==0:
    print("지금은 강의시간이 아닙니다.")
